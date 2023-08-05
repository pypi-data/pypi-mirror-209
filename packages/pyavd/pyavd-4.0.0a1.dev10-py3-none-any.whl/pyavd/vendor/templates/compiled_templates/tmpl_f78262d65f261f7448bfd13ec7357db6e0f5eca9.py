from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/radius-server.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_radius_server = resolve('radius_server')
    l_0_attribute_32_include_in_access_cli = resolve('attribute_32_include_in_access_cli')
    l_0_dynamic_authorization_cli = resolve('dynamic_authorization_cli')
    try:
        t_1 = environment.filters['arista.avd.default']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.default' found.")
    try:
        t_2 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_2((undefined(name='radius_server') if l_0_radius_server is missing else l_0_radius_server)):
        pass
        yield '!\n'
        if t_2(environment.getattr((undefined(name='radius_server') if l_0_radius_server is missing else l_0_radius_server), 'attribute_32_include_in_access_req')):
            pass
            l_0_attribute_32_include_in_access_cli = 'radius-server attribute 32 include-in-access-req'
            context.vars['attribute_32_include_in_access_cli'] = l_0_attribute_32_include_in_access_cli
            context.exported_vars.add('attribute_32_include_in_access_cli')
            if t_2(environment.getattr(environment.getattr((undefined(name='radius_server') if l_0_radius_server is missing else l_0_radius_server), 'attribute_32_include_in_access_req'), 'hostname'), True):
                pass
                l_0_attribute_32_include_in_access_cli = str_join(((undefined(name='attribute_32_include_in_access_cli') if l_0_attribute_32_include_in_access_cli is missing else l_0_attribute_32_include_in_access_cli), ' hostname', ))
                context.vars['attribute_32_include_in_access_cli'] = l_0_attribute_32_include_in_access_cli
                context.exported_vars.add('attribute_32_include_in_access_cli')
            elif t_2(environment.getattr(environment.getattr((undefined(name='radius_server') if l_0_radius_server is missing else l_0_radius_server), 'attribute_32_include_in_access_req'), 'format')):
                pass
                l_0_attribute_32_include_in_access_cli = str_join(((undefined(name='attribute_32_include_in_access_cli') if l_0_attribute_32_include_in_access_cli is missing else l_0_attribute_32_include_in_access_cli), ' format ', environment.getattr(environment.getattr((undefined(name='radius_server') if l_0_radius_server is missing else l_0_radius_server), 'attribute_32_include_in_access'), 'format'), ))
                context.vars['attribute_32_include_in_access_cli'] = l_0_attribute_32_include_in_access_cli
                context.exported_vars.add('attribute_32_include_in_access_cli')
            yield str((undefined(name='attribute_32_include_in_access_cli') if l_0_attribute_32_include_in_access_cli is missing else l_0_attribute_32_include_in_access_cli))
            yield '\n'
        if t_2(environment.getattr((undefined(name='radius_server') if l_0_radius_server is missing else l_0_radius_server), 'dynamic_authorization')):
            pass
            l_0_dynamic_authorization_cli = 'radius-server dynamic-authorization'
            context.vars['dynamic_authorization_cli'] = l_0_dynamic_authorization_cli
            context.exported_vars.add('dynamic_authorization_cli')
            if t_2(environment.getattr(environment.getattr((undefined(name='radius_server') if l_0_radius_server is missing else l_0_radius_server), 'dynamic_authorization'), 'port')):
                pass
                l_0_dynamic_authorization_cli = str_join(((undefined(name='dynamic_authorization_cli') if l_0_dynamic_authorization_cli is missing else l_0_dynamic_authorization_cli), ' port ', environment.getattr(environment.getattr((undefined(name='radius_server') if l_0_radius_server is missing else l_0_radius_server), 'dynamic_authorization'), 'port'), ))
                context.vars['dynamic_authorization_cli'] = l_0_dynamic_authorization_cli
                context.exported_vars.add('dynamic_authorization_cli')
            if t_2(environment.getattr(environment.getattr((undefined(name='radius_server') if l_0_radius_server is missing else l_0_radius_server), 'dynamic_authorization'), 'tls_ssl_profile')):
                pass
                l_0_dynamic_authorization_cli = str_join(((undefined(name='dynamic_authorization_cli') if l_0_dynamic_authorization_cli is missing else l_0_dynamic_authorization_cli), ' tls ssl-profile ', environment.getattr(environment.getattr((undefined(name='radius_server') if l_0_radius_server is missing else l_0_radius_server), 'dynamic_authorization'), 'tls_ssl_profile'), ))
                context.vars['dynamic_authorization_cli'] = l_0_dynamic_authorization_cli
                context.exported_vars.add('dynamic_authorization_cli')
            yield str((undefined(name='dynamic_authorization_cli') if l_0_dynamic_authorization_cli is missing else l_0_dynamic_authorization_cli))
            yield '\n'
        for l_1_radius_host in t_1(environment.getattr((undefined(name='radius_server') if l_0_radius_server is missing else l_0_radius_server), 'hosts'), []):
            l_1_radius_cli = missing
            _loop_vars = {}
            pass
            l_1_radius_cli = str_join(('radius-server host ', environment.getattr(l_1_radius_host, 'host'), ))
            _loop_vars['radius_cli'] = l_1_radius_cli
            if (t_2(environment.getattr(l_1_radius_host, 'vrf')) and (environment.getattr(l_1_radius_host, 'vrf') != 'default')):
                pass
                l_1_radius_cli = str_join(((undefined(name='radius_cli') if l_1_radius_cli is missing else l_1_radius_cli), ' vrf ', environment.getattr(l_1_radius_host, 'vrf'), ))
                _loop_vars['radius_cli'] = l_1_radius_cli
            if t_2(environment.getattr(l_1_radius_host, 'timeout')):
                pass
                l_1_radius_cli = str_join(((undefined(name='radius_cli') if l_1_radius_cli is missing else l_1_radius_cli), ' timeout ', environment.getattr(l_1_radius_host, 'timeout'), ))
                _loop_vars['radius_cli'] = l_1_radius_cli
            if t_2(environment.getattr(l_1_radius_host, 'retransmit')):
                pass
                l_1_radius_cli = str_join(((undefined(name='radius_cli') if l_1_radius_cli is missing else l_1_radius_cli), ' retransmit ', environment.getattr(l_1_radius_host, 'retransmit'), ))
                _loop_vars['radius_cli'] = l_1_radius_cli
            if t_2(environment.getattr(l_1_radius_host, 'key')):
                pass
                l_1_radius_cli = str_join(((undefined(name='radius_cli') if l_1_radius_cli is missing else l_1_radius_cli), ' key 7 ', environment.getattr(l_1_radius_host, 'key'), ))
                _loop_vars['radius_cli'] = l_1_radius_cli
            yield str((undefined(name='radius_cli') if l_1_radius_cli is missing else l_1_radius_cli))
            yield '\n'
        l_1_radius_host = l_1_radius_cli = missing

blocks = {}
debug_info = '3=26&5=29&6=31&7=34&8=36&9=39&10=41&12=44&14=46&15=48&16=51&17=53&19=56&20=58&22=61&24=63&25=67&26=69&27=71&29=73&30=75&32=77&33=79&35=81&36=83&38=85'