from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/management-api-gnmi.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_management_api_gnmi = resolve('management_api_gnmi')
    l_0_octa = resolve('octa')
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
    try:
        t_4 = environment.tests['defined']
    except KeyError:
        @internalcode
        def t_4(*unused):
            raise TemplateRuntimeError("No test named 'defined' found.")
    pass
    if t_3((undefined(name='management_api_gnmi') if l_0_management_api_gnmi is missing else l_0_management_api_gnmi)):
        pass
        yield '\n### Management API GNMI\n\n#### Management API GNMI Summary\n'
        if t_4(environment.getattr((undefined(name='management_api_gnmi') if l_0_management_api_gnmi is missing else l_0_management_api_gnmi), 'enable_vrfs')):
            pass
            if t_4(environment.getattr((undefined(name='management_api_gnmi') if l_0_management_api_gnmi is missing else l_0_management_api_gnmi), 'octa')):
                pass
                l_0_octa = 'enabled'
                context.vars['octa'] = l_0_octa
                context.exported_vars.add('octa')
            else:
                pass
                l_0_octa = 'disabled'
                context.vars['octa'] = l_0_octa
                context.exported_vars.add('octa')
            yield '\n| VRF with GNMI | OCTA |\n| ------------- | ---- |\n'
            for l_1_vrf in t_2(environment.getattr((undefined(name='management_api_gnmi') if l_0_management_api_gnmi is missing else l_0_management_api_gnmi), 'enable_vrfs')):
                _loop_vars = {}
                pass
                yield '| '
                yield str(environment.getattr(l_1_vrf, 'name'))
                yield ' | '
                yield str((undefined(name='octa') if l_0_octa is missing else l_0_octa))
                yield ' |\n'
            l_1_vrf = missing
        if t_3(environment.getattr((undefined(name='management_api_gnmi') if l_0_management_api_gnmi is missing else l_0_management_api_gnmi), 'transport')):
            pass
            yield '\n| Transport | SSL Profile | VRF | Notification Timestamp | ACL |\n| --------- | ----------- | --- | ---------------------- | --- |\n'
            if t_3(environment.getattr(environment.getattr((undefined(name='management_api_gnmi') if l_0_management_api_gnmi is missing else l_0_management_api_gnmi), 'transport'), 'grpc')):
                pass
                for l_1_transport in environment.getattr(environment.getattr((undefined(name='management_api_gnmi') if l_0_management_api_gnmi is missing else l_0_management_api_gnmi), 'transport'), 'grpc'):
                    l_1_transport_name = resolve('transport_name')
                    l_1_ssl_profile = resolve('ssl_profile')
                    l_1_vrf = resolve('vrf')
                    l_1_notif = resolve('notif')
                    l_1_acl = resolve('acl')
                    _loop_vars = {}
                    pass
                    if t_3(environment.getattr(l_1_transport, 'name')):
                        pass
                        l_1_transport_name = environment.getattr(l_1_transport, 'name')
                        _loop_vars['transport_name'] = l_1_transport_name
                        l_1_ssl_profile = t_1(environment.getattr(l_1_transport, 'ssl_profile'), '-')
                        _loop_vars['ssl_profile'] = l_1_ssl_profile
                        l_1_vrf = t_1(environment.getattr(l_1_transport, 'vrf'), '-')
                        _loop_vars['vrf'] = l_1_vrf
                        l_1_notif = t_1(environment.getattr(l_1_transport, 'notification_timestamp'), 'last-change-time')
                        _loop_vars['notif'] = l_1_notif
                        l_1_acl = t_1(environment.getattr(l_1_transport, 'ip_access_group'), '-')
                        _loop_vars['acl'] = l_1_acl
                        yield '| '
                        yield str((undefined(name='transport_name') if l_1_transport_name is missing else l_1_transport_name))
                        yield ' | '
                        yield str((undefined(name='ssl_profile') if l_1_ssl_profile is missing else l_1_ssl_profile))
                        yield ' | '
                        yield str((undefined(name='vrf') if l_1_vrf is missing else l_1_vrf))
                        yield ' | '
                        yield str((undefined(name='notif') if l_1_notif is missing else l_1_notif))
                        yield ' | '
                        yield str((undefined(name='acl') if l_1_acl is missing else l_1_acl))
                        yield ' |\n'
                l_1_transport = l_1_transport_name = l_1_ssl_profile = l_1_vrf = l_1_notif = l_1_acl = missing
        if t_3(environment.getattr((undefined(name='management_api_gnmi') if l_0_management_api_gnmi is missing else l_0_management_api_gnmi), 'provider')):
            pass
            yield '\nProvider '
            yield str(environment.getattr((undefined(name='management_api_gnmi') if l_0_management_api_gnmi is missing else l_0_management_api_gnmi), 'provider'))
            yield ' is configured.\n'
        yield '\n#### Management API gnmi configuration\n\n```eos\n'
        template = environment.get_template('eos/management-api-gnmi.j2', 'documentation/management-api-gnmi.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {'octa': l_0_octa})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '2=37&8=40&9=42&10=44&12=49&17=53&18=57&22=62&26=65&27=67&28=75&29=77&30=79&31=81&32=83&33=85&34=88&39=99&41=102&47=105'