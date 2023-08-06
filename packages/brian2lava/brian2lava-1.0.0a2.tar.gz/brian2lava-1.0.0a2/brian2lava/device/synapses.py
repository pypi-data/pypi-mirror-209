from collections import defaultdict
from collections.abc import Sequence, MutableMapping, Mapping
import functools
import weakref
import re
import numbers

import numpy as np

from brian2.core.base import weakproxy_with_fallback
from brian2.core.base import device_override
from brian2.core.namespace import get_local_namespace
from brian2.core.variables import (DynamicArrayVariable, Variables)
from brian2.codegen.codeobject import create_runner_codeobj
from brian2.codegen.translation import get_identifiers_recursively
from brian2.devices.device import get_device
from brian2.equations.equations import (Equations,
                                        DIFFERENTIAL_EQUATION, SUBEXPRESSION,
                                        PARAMETER,
                                        check_subexpressions, EquationError)
from brian2.groups.group import Group, CodeRunner, get_dtype
from brian2.groups.neurongroup import (extract_constant_subexpressions,
                                       SubexpressionUpdater,
                                       check_identifier_pre_post)
from brian2.parsing.expressions import is_boolean_expression, parse_expression_dimensions
from brian2.stateupdaters.base import (StateUpdateMethod,
                                       UnsupportedEquationsException)
from brian2.stateupdaters.exact import linear, independent
from brian2.units.fundamentalunits import (Quantity, DIMENSIONLESS, DimensionMismatchError,
                                           fail_for_dimension_mismatch)
from brian2.units.allunits import second
from brian2.utils.logger import get_logger
from brian2.utils.stringtools import get_identifiers, word_substitute
from brian2.utils.arrays import calc_repeats
from brian2.core.spikesource import SpikeSource
from brian2.synapses.parse_synaptic_generator_syntax import parse_synapse_generator
from brian2.parsing.bast import brian_ast
from brian2.parsing.rendering import NodeRenderer
from brian2 import Synapses, Function
MAX_SYNAPSES = 2147483647


def spike_queue(self, source_start, source_end):
    """
    TODO

    Parameters
    ----------
    source_start
        TODO
    source_end
        TODO
    
    Returns
    -------
    `SpikeQueue`
        TODO
    """

    # TODO REMOVE! In brian2lava there is no need for a spike queue.
    # Use the C++ version of the SpikeQueue when available
    try:
        from brian2.synapses.cythonspikequeue import SpikeQueue
        self.logger.diagnostic('Using the C++ SpikeQueue', once=True)
    except ImportError:
        from brian2.synapses.spikequeue import SpikeQueue
        self.logger.diagnostic('Using the Python SpikeQueue', once=True)

    return SpikeQueue(source_start=source_start, source_end=source_end)


def synapses_connect(
        self, synapses, condition=None, i=None, j=None, p=1., n=1,
        skip_if_invalid=False, namespace=None, level=0
    ):
    """
    Connects synapses.

    This method overwrites the `connect` function from Brian.

    Parameters
    ----------
    synapses : `Synapses`
        Equals the `self` of the original `connect` function from Brian,
        which is an instance of the `Synapses` class.
    condition : str, bool, optional
        A boolean or string expression that evaluates to a boolean.
        The expression can depend on indices ``i`` and ``j`` and on
        pre- and post-synaptic variables. Can be combined with
        arguments ``n``, and ``p`` but not ``i`` or ``j``.
    i : int, ndarray of int, str, optional
        The presynaptic neuron indices  It can be an index or array of
        indices if combined with the ``j`` argument, or it can be a string
        generator expression.
    j : int, ndarray of int, str, optional
        The postsynaptic neuron indices. It can be an index or array of
        indices if combined with the ``i`` argument, or it can be a string
        generator expression.
    p : float, str, optional
        The probability to create ``n`` synapses wherever the ``condition``
        evaluates to true. Cannot be used with generator syntax for ``j``.
    n : int, str, optional
        The number of synapses to create per pre/post connection pair.
        Defaults to 1.
    skip_if_invalid : bool, optional
        If set to True, rather than raising an error if you try to
        create an invalid/out of range pair (i, j) it will just
        quietly skip those synapses.
    namespace : dict-like, optional
        A namespace that will be used in addition to the group-specific
        namespaces (if defined). If not specified, the locals
        and globals around the run function will be used.
    level : int, optional
        How deep to go up the stack frame to look for the locals/global
        (see ``namespace`` argument).
    """
    # First, add the spiking synapses variable to the lava_variables
    self._add_spiking_synapses_vars(synapses)
    # Check types
    synapses._verify_connect_argument_types(condition, i, j, n, p)

    synapses._connect_called = True

    # Get namespace information
    if namespace is None:
        namespace = get_local_namespace(level=level + 2)

    try:  # wrap everything to catch IndexError
        # which connection case are we in?
        # 1: Connection condition
        if condition is None and i is None and j is None:
            condition = True
        if condition is not None:
            if i is not None or j is not None:
                raise ValueError("Cannot combine condition with i or j "
                                    "arguments")
            if condition is False or condition == 'False':
                # Nothing to do
                return
            j = synapses._condition_to_generator_expression(condition, p, namespace)
            self.logger.debug("Using synapses from generator")
            synapses._add_synapses_generator(j, n, skip_if_invalid=skip_if_invalid,
                                            namespace=namespace, level=level + 2,
                                            over_presynaptic=True)
        # 2: connection indices
        elif (i is not None and j is not None) and not (isinstance(i, str) or isinstance(j, str)):
            if skip_if_invalid:
                raise ValueError("Can only use skip_if_invalid with string "
                                    "syntax")
            i, j, n = synapses._verify_connect_array_arguments(i, j, n)
            self.logger.debug("Using synapses from arrays")
            synapses._add_synapses_from_arrays(i, j, n, p, namespace=namespace)
        # 3: Generator expression over post-synaptic cells (i='...')
        elif isinstance(i, str):
            i = synapses._finalize_generator_expression(i, j, p, 'i', 'j')
            self.logger.debug("Using synapses from generator")
            synapses._add_synapses_generator(i, n, skip_if_invalid=skip_if_invalid,
                                            namespace=namespace, level=level + 2,
                                            over_presynaptic=False)
        # 4: Generator expression over pre-synaptic cells (i='...')
        elif isinstance(j, str):
            j = synapses._finalize_generator_expression(j, i, p, 'j', 'i')
            self.logger.debug("Using synapses from generator")
            synapses._add_synapses_generator(j, n, skip_if_invalid=skip_if_invalid,
                                            namespace=namespace, level=level + 2,
                                            over_presynaptic=True)
        else:
            raise ValueError("Must specify at least one of condition, i or "
                                "j arguments")
    except IndexError as e:
        raise IndexError("Tried to create synapse indices outside valid "
                            "range. Original error message: " + str(e))


def _add_spiking_synapses_vars(self,synapses):
    """
    Adds a variable to the lava_variables which will store the spiking synapses from the last
    timestep. The vector is then used to update the synaptic variables in the run_lrn function if
    the synapses are plastic.
    """
    
    for pathway in synapses._pathways:
        prepost = pathway.prepost
        name = f"lava_spiking_synapses_{prepost}"
        size = 1

        # This needs to be a dynamic array as its shape will change during the simulation
        synapses.variables.add_dynamic_array(name,size,dtype = "int")

        # Register this variable so that it will be correctly resized during the initialization.
        synapses.register_variable(synapses.variables[name])


def determine_lava_ports(self, pathway, variables):
    """
    Extracts the synaptic variables to be sent to the neurongroups and determine the Lava ports required for that.

    Parameters
    ----------
    pathway
        Synaptic pathways.
    variables
        The variables contained in the code used by the pathway.
    """
    # Support for subgroups will come in the future
    if 'subgroup' in pathway.source.name or 'subgroup' in pathway.target.name:
        msg = f"""
        Encountered a Subgroup object in the connection from {pathway.source.name} to {pathway.target.name}.
        Subgroups are not supported yet. Subgroups are defined by indexing a NeuronGroup (e.g. P = NG[0:10]).
        If you are using this method to connect synapses we suggest using alternative methods such as
        the expression S.connect('i<10',p = p), which has been tested.
        """
        raise NotImplementedError(msg)
    synaptic_vars = []
    # TODO: this is probably not needed in case the update only requires synaptic variables,
    # then you wouldn't need to send them to the neuronGroup. But for now let's just make
    # the easiest scenario
    for varname,var in variables.items():
        if isinstance(var, Function) or not isinstance(var.owner, Synapses):
            continue
        synaptic_vars.append(varname)

    # Var names are kept in their original form, but the ports are separated depending on the pathway
    for varname in synaptic_vars:
        portname = pathway.synapses.name +'_'+ pathway.prepost +'_'+ varname
        self.lava_ports[portname] = {
            'varname': varname, # Required by code generation
            'portname': portname,
            'pathway': pathway,
            'sender' : pathway.source.name,
            'receiver': pathway.target.name
        }

    ports = '\n\t'.join([port  for port in self.lava_ports])
    msg = f"""Saved ports for synaptic transmission from synapses {pathway.synapses.name} to {pathway.target.name}:
    Ports required:
    {ports}
    """
    self.logger.diagnostic(msg)