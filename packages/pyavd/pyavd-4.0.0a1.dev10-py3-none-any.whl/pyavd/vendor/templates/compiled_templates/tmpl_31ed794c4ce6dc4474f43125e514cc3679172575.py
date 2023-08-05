from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/system.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_system = resolve('system')
    try:
        t_1 = environment.filters['arista.avd.default']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.default' found.")
    try:
        t_2 = environment.filters['arista.avd.natural_sort']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.natural_sort' found.")
    try:
        t_3 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_3(environment.getattr((undefined(name='system') if l_0_system is missing else l_0_system), 'control_plane')):
        pass
        yield '\n### System Control-Plane\n'
        if (t_3(environment.getattr(environment.getattr(environment.getattr((undefined(name='system') if l_0_system is missing else l_0_system), 'control_plane'), 'tcp_mss'), 'ipv4')) or t_3(environment.getattr(environment.getattr(environment.getattr((undefined(name='system') if l_0_system is missing else l_0_system), 'control_plane'), 'tcp_mss'), 'ipv6'))):
            pass
            yield '\n##### TCP MSS Ceiling\n\n| Protocol | Segment Size |\n| -------- | -------------|\n'
            if t_3(environment.getattr(environment.getattr(environment.getattr((undefined(name='system') if l_0_system is missing else l_0_system), 'control_plane'), 'tcp_mss'), 'ipv4')):
                pass
                yield '| IPv4 | '
                yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='system') if l_0_system is missing else l_0_system), 'control_plane'), 'tcp_mss'), 'ipv4'))
                yield ' |\n'
            if t_3(environment.getattr(environment.getattr(environment.getattr((undefined(name='system') if l_0_system is missing else l_0_system), 'control_plane'), 'tcp_mss'), 'ipv6')):
                pass
                yield '| IPv6 | '
                yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='system') if l_0_system is missing else l_0_system), 'control_plane'), 'tcp_mss'), 'ipv6'))
                yield ' |\n'
        if (t_3(environment.getattr(environment.getattr((undefined(name='system') if l_0_system is missing else l_0_system), 'control_plane'), 'ipv4_access_groups')) or t_3(environment.getattr(environment.getattr((undefined(name='system') if l_0_system is missing else l_0_system), 'control_plane'), 'ipv6_access_groups'))):
            pass
            yield '\n##### Control-Plane Access-Groups\n\n| Protocol | VRF | Access-list |\n| -------- | --- | ------------|\n'
            for l_1_acl_set in t_2(environment.getattr(environment.getattr((undefined(name='system') if l_0_system is missing else l_0_system), 'control_plane'), 'ipv4_access_groups')):
                _loop_vars = {}
                pass
                yield '| IPv4 | '
                yield str(t_1(environment.getattr(l_1_acl_set, 'vrf'), 'default'))
                yield ' | '
                yield str(environment.getattr(l_1_acl_set, 'acl_name'))
                yield ' |\n'
            l_1_acl_set = missing
            for l_1_acl_set in t_2(environment.getattr(environment.getattr((undefined(name='system') if l_0_system is missing else l_0_system), 'control_plane'), 'ipv6_access_groups')):
                _loop_vars = {}
                pass
                yield '| IPv6 | '
                yield str(t_1(environment.getattr(l_1_acl_set, 'vrf'), 'default'))
                yield ' | '
                yield str(environment.getattr(l_1_acl_set, 'acl_name'))
                yield ' |\n'
            l_1_acl_set = missing
        yield '\n#### System Control-Plane Configuration\n\n```eos\n'
        template = environment.get_template('eos/system.j2', 'documentation/system.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '2=30&5=33&11=36&12=39&14=41&15=44&18=46&25=49&26=53&29=58&30=62&37=68'