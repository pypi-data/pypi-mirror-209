from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/radius-servers.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_radius_servers = resolve('radius_servers')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_1((undefined(name='radius_servers') if l_0_radius_servers is missing else l_0_radius_servers)):
        pass
        yield '!\n'
        for l_1_radius_server in (undefined(name='radius_servers') if l_0_radius_servers is missing else l_0_radius_servers):
            l_1_radius_cli = resolve('radius_cli')
            _loop_vars = {}
            pass
            if t_1(environment.getattr(l_1_radius_server, 'host')):
                pass
                l_1_radius_cli = str_join(('radius-server host ', environment.getattr(l_1_radius_server, 'host'), ))
                _loop_vars['radius_cli'] = l_1_radius_cli
            if (t_1(environment.getattr(l_1_radius_server, 'vrf')) and (environment.getattr(l_1_radius_server, 'vrf') != 'default')):
                pass
                l_1_radius_cli = str_join(((undefined(name='radius_cli') if l_1_radius_cli is missing else l_1_radius_cli), ' vrf ', environment.getattr(l_1_radius_server, 'vrf'), ))
                _loop_vars['radius_cli'] = l_1_radius_cli
            if t_1(environment.getattr(l_1_radius_server, 'key')):
                pass
                l_1_radius_cli = str_join(((undefined(name='radius_cli') if l_1_radius_cli is missing else l_1_radius_cli), ' key 7 ', environment.getattr(l_1_radius_server, 'key'), ))
                _loop_vars['radius_cli'] = l_1_radius_cli
            yield str((undefined(name='radius_cli') if l_1_radius_cli is missing else l_1_radius_cli))
            yield '\n'
        l_1_radius_server = l_1_radius_cli = missing

blocks = {}
debug_info = '2=18&4=21&5=25&6=27&8=29&9=31&11=33&12=35&14=37'