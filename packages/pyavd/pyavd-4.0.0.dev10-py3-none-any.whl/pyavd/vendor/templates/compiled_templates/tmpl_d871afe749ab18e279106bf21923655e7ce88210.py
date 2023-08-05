from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/dot1x.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_dot1x = resolve('dot1x')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_1((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x)):
        pass
        yield '!\n'
        if t_1(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'system_auth_control'), True):
            pass
            yield 'dot1x system-auth-control\n'
        if t_1(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'protocol_lldp_bypass'), True):
            pass
            yield 'dot1x protocol lldp bypass\n'
        if t_1(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'dynamic_authorization'), True):
            pass
            yield 'dot1x dynamic-authorization\n'
        if (environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'mac_based_authentication') or t_1(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'radius_av_pair'))):
            pass
            yield 'dot1x\n'
            if t_1(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'mac_based_authentication')):
                pass
                if t_1(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'mac_based_authentication'), 'delay')):
                    pass
                    yield '   mac based authentication delay '
                    yield str(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'mac_based_authentication'), 'delay'))
                    yield ' seconds\n'
                if t_1(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'mac_based_authentication'), 'hold_period')):
                    pass
                    yield '   mac based authentication hold period '
                    yield str(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'mac_based_authentication'), 'hold_period'))
                    yield ' seconds\n'
            if t_1(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'radius_av_pair')):
                pass
                if t_1(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'radius_av_pair'), 'service_type'), True):
                    pass
                    yield '   radius av-pair service-type\n'
                if t_1(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'radius_av_pair'), 'framed_mtu')):
                    pass
                    yield '   radius av-pair framed-mtu '
                    yield str(environment.getattr(environment.getattr((undefined(name='dot1x') if l_0_dot1x is missing else l_0_dot1x), 'radius_av_pair'), 'framed_mtu'))
                    yield '\n'

blocks = {}
debug_info = '2=18&4=21&7=24&10=27&13=30&15=33&16=35&17=38&19=40&20=43&23=45&24=47&27=50&28=53'