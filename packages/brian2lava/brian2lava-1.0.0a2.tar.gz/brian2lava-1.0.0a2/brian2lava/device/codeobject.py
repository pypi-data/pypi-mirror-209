from brian2.synapses.synapses import SynapticPathway
from brian2.core.functions import Function
from brian2.core.variables import ArrayVariable


def code_object(
        self,
        owner,
        name,
        abstract_code,
        variables,
        template_name,
        variable_indices,
        codeobj_class=None,
        template_kwds=None,
        override_conditional_write=None,
        compiler_kwds=None
    ):
    """
    Defines a code object.

    Parameters
    ----------
    TODO

    Returns
    -------
    codeobj
    """
    
    # Log when a code object is added
    self.logger.diagnostic(f'Add code_object {name}')
    self.logger.diagnostic(f'Variables gotten from previous steps, {[varname for varname,var in list(variables.items())]}')
    # Init template keywords if none were given
    if template_kwds is None:
        template_kwds = dict()
    
    # We define nan as a generic int which hopefully will never appear in a real simulation
    # This is used in synaptic transmission to determine if a synapse is active or not.
    template_kwds["nan"] = -92233720329451

    # In case a variable is set with initial values, we extract the related variable name
    # The variable name is extracted from the abstract code line (before the equal sign)
    # The name is used to get a unique name for the method that initializes the variable
    if template_name in self.init_template_functions:
        # With this we bypass the instructions in the brian base device:
        # (brian2.devices.device -> 328-336)
        # This is because for initialization variables we want to use a different
        # naming convention.
        # Note that this requires renaming the {{variables}} in the template to add the '_init' suffix
        for varname, var in variables.items():
            if isinstance(var, ArrayVariable):
                pointer_name = self.get_array_name(var, prefix = 'self.init')
                if var.scalar:
                    pointer_name += "[0]"
                template_kwds[varname + '_init'] = pointer_name
                if hasattr(var, "resize"):
                    dyn_array_name = self.get_array_name(var, prefix = 'self.init', access_data=False)
                    template_kwds[f"_dynamic_{varname}_init"] = dyn_array_name
        # TODO: This functionality could be used in the other generators (for variable initializations)
    
    # In order to properly use synapses we need to be able to access the pathways
    # before they are added to the synapses._pathway variable. Since this variable
    # is only used for this special case, we don't need to store all of the pathways
    # but only the current one, which will then be read by the lava_generator.
    if template_name == 'synapses':
        self._pathway = template_kwds['pathway']
    # Call code_object method from Brian2 parent device
    codeobj = self.super.code_object(
        owner,
        name,
        abstract_code,
        variables,
        template_name,
        variable_indices,
        codeobj_class=codeobj_class,
        template_kwds=template_kwds,
        override_conditional_write=override_conditional_write,
        compiler_kwds=compiler_kwds
    )

    # Store code objects in device
    self.code_objects[codeobj.name] = codeobj
    
    return codeobj

    
    




