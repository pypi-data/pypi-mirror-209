from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/mac-security.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_mac_security = resolve('mac_security')
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
    if t_2((undefined(name='mac_security') if l_0_mac_security is missing else l_0_mac_security)):
        pass
        yield '!\nmac security\n'
        if (t_2(environment.getattr(environment.getattr((undefined(name='mac_security') if l_0_mac_security is missing else l_0_mac_security), 'license'), 'license_name')) and t_2(environment.getattr(environment.getattr((undefined(name='mac_security') if l_0_mac_security is missing else l_0_mac_security), 'license'), 'license_key'))):
            pass
            yield '   license '
            yield str(environment.getattr(environment.getattr((undefined(name='mac_security') if l_0_mac_security is missing else l_0_mac_security), 'license'), 'license_name'))
            yield ' '
            yield str(environment.getattr(environment.getattr((undefined(name='mac_security') if l_0_mac_security is missing else l_0_mac_security), 'license'), 'license_key'))
            yield '\n'
        if t_2(environment.getattr((undefined(name='mac_security') if l_0_mac_security is missing else l_0_mac_security), 'fips_restrictions'), True):
            pass
            yield '   fips restrictions\n'
        yield '   !\n'
        for l_1_profile in t_1(environment.getattr((undefined(name='mac_security') if l_0_mac_security is missing else l_0_mac_security), 'profiles'), 'name'):
            _loop_vars = {}
            pass
            yield '   profile '
            yield str(environment.getattr(l_1_profile, 'name'))
            yield '\n'
            if t_2(environment.getattr(l_1_profile, 'cipher')):
                pass
                yield '      cipher '
                yield str(environment.getattr(l_1_profile, 'cipher'))
                yield '\n'
            for l_2_connection_key in t_1(environment.getattr(l_1_profile, 'connection_keys'), 'id'):
                l_2_key_cli = resolve('key_cli')
                _loop_vars = {}
                pass
                if t_2(environment.getattr(l_2_connection_key, 'encrypted_key')):
                    pass
                    l_2_key_cli = str_join(('key ', environment.getattr(l_2_connection_key, 'id'), ' 7 ', environment.getattr(l_2_connection_key, 'encrypted_key'), ))
                    _loop_vars['key_cli'] = l_2_key_cli
                    if t_2(environment.getattr(l_2_connection_key, 'fallback')):
                        pass
                        l_2_key_cli = str_join(((undefined(name='key_cli') if l_2_key_cli is missing else l_2_key_cli), ' fallback', ))
                        _loop_vars['key_cli'] = l_2_key_cli
                    yield '      '
                    yield str((undefined(name='key_cli') if l_2_key_cli is missing else l_2_key_cli))
                    yield '\n'
            l_2_connection_key = l_2_key_cli = missing
            if t_2(environment.getattr(environment.getattr(l_1_profile, 'mka'), 'key_server_priority')):
                pass
                yield '      mka key-server priority '
                yield str(environment.getattr(environment.getattr(l_1_profile, 'mka'), 'key_server_priority'))
                yield '\n'
            if t_2(environment.getattr(environment.getattr(environment.getattr(l_1_profile, 'mka'), 'session'), 'rekey_period')):
                pass
                yield '      mka session rekey-period '
                yield str(environment.getattr(environment.getattr(environment.getattr(l_1_profile, 'mka'), 'session'), 'rekey_period'))
                yield '\n'
            if t_2(environment.getattr(l_1_profile, 'sci'), True):
                pass
                yield '      sci\n'
            if t_2(environment.getattr(environment.getattr(l_1_profile, 'l2_protocols'), 'ethernet_flow_control')):
                pass
                yield '      l2-protocol ethernet-flow-control '
                yield str(environment.getattr(environment.getattr(environment.getattr(l_1_profile, 'l2_protocols'), 'ethernet_flow_control'), 'mode'))
                yield '\n'
            if t_2(environment.getattr(environment.getattr(l_1_profile, 'l2_protocols'), 'lldp')):
                pass
                yield '      l2-protocol lldp '
                yield str(environment.getattr(environment.getattr(environment.getattr(l_1_profile, 'l2_protocols'), 'lldp'), 'mode'))
                yield '\n'
        l_1_profile = missing

blocks = {}
debug_info = '2=24&5=27&6=30&8=34&12=38&13=42&14=44&15=47&17=49&18=53&19=55&20=57&21=59&23=62&26=65&27=68&29=70&30=73&32=75&35=78&36=81&38=83&39=86'