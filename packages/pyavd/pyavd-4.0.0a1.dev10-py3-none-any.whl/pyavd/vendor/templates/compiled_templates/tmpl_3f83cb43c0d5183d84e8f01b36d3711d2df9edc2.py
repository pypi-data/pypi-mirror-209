from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/ip-name-servers.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_ip_name_servers = resolve('ip_name_servers')
    l_0_name_server = resolve('name_server')
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
    for l_1_name_server in t_1((undefined(name='ip_name_servers') if l_0_ip_name_servers is missing else l_0_ip_name_servers), 'ip_address'):
        l_1_name_server_cli = missing
        _loop_vars = {}
        pass
        l_1_name_server_cli = 'ip name-server'
        _loop_vars['name_server_cli'] = l_1_name_server_cli
        if t_2(environment.getattr(l_1_name_server, 'vrf')):
            pass
            l_1_name_server_cli = str_join(((undefined(name='name_server_cli') if l_1_name_server_cli is missing else l_1_name_server_cli), ' vrf ', environment.getattr(l_1_name_server, 'vrf'), ))
            _loop_vars['name_server_cli'] = l_1_name_server_cli
        l_1_name_server_cli = str_join(((undefined(name='name_server_cli') if l_1_name_server_cli is missing else l_1_name_server_cli), ' ', environment.getattr(l_1_name_server, 'ip_address'), ))
        _loop_vars['name_server_cli'] = l_1_name_server_cli
        if t_2(environment.getattr(l_1_name_server, 'priority')):
            pass
            l_1_name_server_cli = str_join(((undefined(name='name_server_cli') if l_1_name_server_cli is missing else l_1_name_server_cli), ' priority ', environment.getattr(l_1_name_server, 'priority'), ))
            _loop_vars['name_server_cli'] = l_1_name_server_cli
        yield str((undefined(name='name_server_cli') if l_1_name_server_cli is missing else l_1_name_server_cli))
        yield '\n'
    l_1_name_server = l_1_name_server_cli = missing
    for l_1_node in t_1(environment.getattr((undefined(name='name_server') if l_0_name_server is missing else l_0_name_server), 'nodes')):
        _loop_vars = {}
        pass
        if t_2(environment.getattr(environment.getattr((undefined(name='name_server') if l_0_name_server is missing else l_0_name_server), 'source'), 'vrf')):
            pass
            yield 'ip name-server vrf '
            yield str(environment.getattr(environment.getattr((undefined(name='name_server') if l_0_name_server is missing else l_0_name_server), 'source'), 'vrf'))
            yield ' '
            yield str(l_1_node)
            yield '\n'
        else:
            pass
            yield 'ip name-server '
            yield str(l_1_node)
            yield '\n'
    l_1_node = missing

blocks = {}
debug_info = '2=25&3=29&4=31&5=33&7=35&8=37&9=39&11=41&14=44&15=47&16=50&18=57'