from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/tacacs-servers.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_tacacs_servers = resolve('tacacs_servers')
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
    if t_3((undefined(name='tacacs_servers') if l_0_tacacs_servers is missing else l_0_tacacs_servers)):
        pass
        yield '!\n'
        for l_1_host in t_2(environment.getattr((undefined(name='tacacs_servers') if l_0_tacacs_servers is missing else l_0_tacacs_servers), 'hosts')):
            l_1_host_cli = resolve('host_cli')
            _loop_vars = {}
            pass
            if t_3(environment.getattr(l_1_host, 'host')):
                pass
                l_1_host_cli = str_join(('tacacs-server host ', environment.getattr(l_1_host, 'host'), ))
                _loop_vars['host_cli'] = l_1_host_cli
            if t_3(environment.getattr(l_1_host, 'single_connection'), True):
                pass
                l_1_host_cli = str_join(((undefined(name='host_cli') if l_1_host_cli is missing else l_1_host_cli), ' single-connection', ))
                _loop_vars['host_cli'] = l_1_host_cli
            if t_3(environment.getattr(l_1_host, 'vrf')):
                pass
                if (environment.getattr(l_1_host, 'vrf') != 'default'):
                    pass
                    l_1_host_cli = str_join(((undefined(name='host_cli') if l_1_host_cli is missing else l_1_host_cli), ' vrf ', environment.getattr(l_1_host, 'vrf'), ))
                    _loop_vars['host_cli'] = l_1_host_cli
            if t_3(environment.getattr(l_1_host, 'timeout')):
                pass
                l_1_host_cli = str_join(((undefined(name='host_cli') if l_1_host_cli is missing else l_1_host_cli), ' timeout ', environment.getattr(l_1_host, 'timeout'), ))
                _loop_vars['host_cli'] = l_1_host_cli
            if t_3(environment.getattr(l_1_host, 'key')):
                pass
                l_1_host_cli = str_join(((undefined(name='host_cli') if l_1_host_cli is missing else l_1_host_cli), ' key ', t_1(environment.getattr(l_1_host, 'key_type'), '7'), ' ', environment.getattr(l_1_host, 'key'), ))
                _loop_vars['host_cli'] = l_1_host_cli
            yield str((undefined(name='host_cli') if l_1_host_cli is missing else l_1_host_cli))
            yield '\n'
        l_1_host = l_1_host_cli = missing
        if t_3(environment.getattr((undefined(name='tacacs_servers') if l_0_tacacs_servers is missing else l_0_tacacs_servers), 'policy_unknown_mandatory_attribute_ignore'), True):
            pass
            yield 'tacacs-server policy unknown-mandatory-attribute ignore\n'

blocks = {}
debug_info = '2=30&4=33&5=37&6=39&8=41&9=43&11=45&12=47&13=49&16=51&17=53&19=55&20=57&22=59&24=62'