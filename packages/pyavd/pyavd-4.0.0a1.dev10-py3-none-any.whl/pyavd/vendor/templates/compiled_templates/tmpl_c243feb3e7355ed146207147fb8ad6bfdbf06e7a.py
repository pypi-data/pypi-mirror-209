from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/ip-http-client-source-interfaces.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_ip_http_client_source_interfaces = resolve('ip_http_client_source_interfaces')
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
    for l_1_ip_http_client_source_interface in t_1((undefined(name='ip_http_client_source_interfaces') if l_0_ip_http_client_source_interfaces is missing else l_0_ip_http_client_source_interfaces)):
        l_1_ip_http_client_cli = missing
        _loop_vars = {}
        pass
        yield '!\n'
        l_1_ip_http_client_cli = 'ip http client'
        _loop_vars['ip_http_client_cli'] = l_1_ip_http_client_cli
        if t_2(environment.getattr(l_1_ip_http_client_source_interface, 'name')):
            pass
            l_1_ip_http_client_cli = str_join(((undefined(name='ip_http_client_cli') if l_1_ip_http_client_cli is missing else l_1_ip_http_client_cli), ' local-interface ', environment.getattr(l_1_ip_http_client_source_interface, 'name'), ))
            _loop_vars['ip_http_client_cli'] = l_1_ip_http_client_cli
        if t_2(environment.getattr(l_1_ip_http_client_source_interface, 'vrf')):
            pass
            l_1_ip_http_client_cli = str_join(((undefined(name='ip_http_client_cli') if l_1_ip_http_client_cli is missing else l_1_ip_http_client_cli), ' vrf ', environment.getattr(l_1_ip_http_client_source_interface, 'vrf'), ))
            _loop_vars['ip_http_client_cli'] = l_1_ip_http_client_cli
        yield str((undefined(name='ip_http_client_cli') if l_1_ip_http_client_cli is missing else l_1_ip_http_client_cli))
        yield '\n'
    l_1_ip_http_client_source_interface = l_1_ip_http_client_cli = missing

blocks = {}
debug_info = '2=24&4=29&5=31&6=33&8=35&9=37&11=39'