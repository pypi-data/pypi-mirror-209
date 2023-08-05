from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/management-api-http.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_management_api_http = resolve('management_api_http')
    try:
        t_1 = environment.filters['arista.avd.natural_sort']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.natural_sort' found.")
    try:
        t_2 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_2((undefined(name='management_api_http') if l_0_management_api_http is missing else l_0_management_api_http)):
        pass
        yield '!\nmanagement api http-commands\n'
        if t_2(environment.getattr((undefined(name='management_api_http') if l_0_management_api_http is missing else l_0_management_api_http), 'enable_https'), True):
            pass
            yield '   protocol https\n'
            if t_2(environment.getattr((undefined(name='management_api_http') if l_0_management_api_http is missing else l_0_management_api_http), 'https_ssl_profile')):
                pass
                yield '   protocol https ssl profile '
                yield str(environment.getattr((undefined(name='management_api_http') if l_0_management_api_http is missing else l_0_management_api_http), 'https_ssl_profile'))
                yield '\n'
        elif t_2(environment.getattr((undefined(name='management_api_http') if l_0_management_api_http is missing else l_0_management_api_http), 'enable_https'), False):
            pass
            yield '   no protocol https\n'
        if t_2(environment.getattr((undefined(name='management_api_http') if l_0_management_api_http is missing else l_0_management_api_http), 'enable_http'), True):
            pass
            yield '   protocol http\n'
        elif t_2(environment.getattr((undefined(name='management_api_http') if l_0_management_api_http is missing else l_0_management_api_http), 'enable_http'), False):
            pass
            yield '   no protocol http\n'
        if t_2(environment.getattr((undefined(name='management_api_http') if l_0_management_api_http is missing else l_0_management_api_http), 'default_services'), True):
            pass
            yield '   default-services\n'
        elif t_2(environment.getattr((undefined(name='management_api_http') if l_0_management_api_http is missing else l_0_management_api_http), 'default_services'), False):
            pass
            yield '   no default-services\n'
        yield '   no shutdown\n'
        for l_1_vrf in t_1(environment.getattr((undefined(name='management_api_http') if l_0_management_api_http is missing else l_0_management_api_http), 'enable_vrfs'), 'name'):
            _loop_vars = {}
            pass
            yield '   !\n   vrf '
            yield str(environment.getattr(l_1_vrf, 'name'))
            yield '\n      no shutdown\n'
            if t_2(environment.getattr(l_1_vrf, 'access_group')):
                pass
                yield '      ip access-group '
                yield str(environment.getattr(l_1_vrf, 'access_group'))
                yield '\n'
            if t_2(environment.getattr(l_1_vrf, 'ipv6_access_group')):
                pass
                yield '      ipv6 access-group '
                yield str(environment.getattr(l_1_vrf, 'ipv6_access_group'))
                yield '\n'
        l_1_vrf = missing
        if (t_2(environment.getattr(environment.getattr((undefined(name='management_api_http') if l_0_management_api_http is missing else l_0_management_api_http), 'protocol_https_certificate'), 'certificate')) and t_2(environment.getattr(environment.getattr((undefined(name='management_api_http') if l_0_management_api_http is missing else l_0_management_api_http), 'protocol_https_certificate'), 'private_key'))):
            pass
            yield '   protocol_https_certificate\n   '
            yield str(environment.getattr(environment.getattr((undefined(name='management_api_http') if l_0_management_api_http is missing else l_0_management_api_http), 'protocol_https_certificate'), 'certificate'))
            yield '\n   EOF\n   '
            yield str(environment.getattr(environment.getattr((undefined(name='management_api_http') if l_0_management_api_http is missing else l_0_management_api_http), 'protocol_https_certificate'), 'private_key'))
            yield '\n   EOF\n'

blocks = {}
debug_info = '2=24&5=27&7=30&8=33&10=35&13=38&15=41&18=44&20=47&24=51&26=55&28=57&29=60&31=62&32=65&35=68&37=71&39=73'