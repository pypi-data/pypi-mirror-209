from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/pim-sparse-mode-interfaces.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_pim_interfaces = resolve('pim_interfaces')
    try:
        t_1 = environment.filters['arista.avd.default']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.default' found.")
    try:
        t_2 = environment.filters['length']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No filter named 'length' found.")
    pass
    if (t_2((undefined(name='pim_interfaces') if l_0_pim_interfaces is missing else l_0_pim_interfaces)) > 0):
        pass
        yield '\n#### PIM Sparse Mode enabled interfaces\n\n| Interface Name | VRF Name | IP Version | DR Priority | Local Interface |\n| -------------- | -------- | ---------- | ----------- | --------------- |\n'
        for l_1_interface in (undefined(name='pim_interfaces') if l_0_pim_interfaces is missing else l_0_pim_interfaces):
            l_1_vrf = l_1_ip_version = l_1_dr_priority = l_1_local_interface = missing
            _loop_vars = {}
            pass
            l_1_vrf = t_1(environment.getattr(l_1_interface, 'vrf'), '-')
            _loop_vars['vrf'] = l_1_vrf
            l_1_ip_version = 'IPv4'
            _loop_vars['ip_version'] = l_1_ip_version
            l_1_dr_priority = t_1(environment.getattr(environment.getattr(environment.getattr(l_1_interface, 'pim'), 'ipv4'), 'dr_priority'), '-')
            _loop_vars['dr_priority'] = l_1_dr_priority
            l_1_local_interface = t_1(environment.getattr(environment.getattr(environment.getattr(l_1_interface, 'pim'), 'ipv4'), 'local_interface'), '-')
            _loop_vars['local_interface'] = l_1_local_interface
            yield '| '
            yield str(environment.getattr(l_1_interface, 'name'))
            yield ' | '
            yield str((undefined(name='vrf') if l_1_vrf is missing else l_1_vrf))
            yield ' | '
            yield str((undefined(name='ip_version') if l_1_ip_version is missing else l_1_ip_version))
            yield ' | '
            yield str((undefined(name='dr_priority') if l_1_dr_priority is missing else l_1_dr_priority))
            yield ' | '
            yield str((undefined(name='local_interface') if l_1_local_interface is missing else l_1_local_interface))
            yield ' |\n'
        l_1_interface = l_1_vrf = l_1_ip_version = l_1_dr_priority = l_1_local_interface = missing

blocks = {}
debug_info = '3=24&9=27&10=31&11=33&12=35&13=37&14=40'