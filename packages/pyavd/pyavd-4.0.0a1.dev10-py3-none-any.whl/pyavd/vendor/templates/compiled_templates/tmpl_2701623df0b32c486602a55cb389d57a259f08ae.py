from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/management-api-gnmi.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_management_api_gnmi = resolve('management_api_gnmi')
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
    try:
        t_3 = environment.tests['defined']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No test named 'defined' found.")
    pass
    if t_2((undefined(name='management_api_gnmi') if l_0_management_api_gnmi is missing else l_0_management_api_gnmi)):
        pass
        yield '!\nmanagement api gnmi\n'
        for l_1_vrf in t_1(environment.getattr((undefined(name='management_api_gnmi') if l_0_management_api_gnmi is missing else l_0_management_api_gnmi), 'enable_vrfs')):
            _loop_vars = {}
            pass
            if (environment.getattr(l_1_vrf, 'name') == 'default'):
                pass
                yield '   transport grpc default\n'
            else:
                pass
                yield '   transport grpc '
                yield str(environment.getattr(l_1_vrf, 'name'))
                yield '\n'
                if t_2(environment.getattr(l_1_vrf, 'access_group')):
                    pass
                    yield '      ip access-group '
                    yield str(environment.getattr(l_1_vrf, 'access_group'))
                    yield '\n'
                yield '      vrf '
                yield str(environment.getattr(l_1_vrf, 'name'))
                yield '\n'
        l_1_vrf = missing
        if t_3(environment.getattr((undefined(name='management_api_gnmi') if l_0_management_api_gnmi is missing else l_0_management_api_gnmi), 'octa')):
            pass
            yield '   provider eos-native\n'
        if t_2(environment.getattr((undefined(name='management_api_gnmi') if l_0_management_api_gnmi is missing else l_0_management_api_gnmi), 'transport')):
            pass
            if t_2(environment.getattr(environment.getattr((undefined(name='management_api_gnmi') if l_0_management_api_gnmi is missing else l_0_management_api_gnmi), 'transport'), 'grpc')):
                pass
                for l_1_transport in environment.getattr(environment.getattr((undefined(name='management_api_gnmi') if l_0_management_api_gnmi is missing else l_0_management_api_gnmi), 'transport'), 'grpc'):
                    _loop_vars = {}
                    pass
                    if t_2(environment.getattr(l_1_transport, 'name')):
                        pass
                        yield '   transport grpc '
                        yield str(environment.getattr(l_1_transport, 'name'))
                        yield '\n'
                        if t_2(environment.getattr(l_1_transport, 'ssl_profile')):
                            pass
                            yield '      ssl profile '
                            yield str(environment.getattr(l_1_transport, 'ssl_profile'))
                            yield '\n'
                        if t_2(environment.getattr(l_1_transport, 'vrf')):
                            pass
                            yield '      vrf '
                            yield str(environment.getattr(l_1_transport, 'vrf'))
                            yield '\n'
                        if t_2(environment.getattr(l_1_transport, 'ip_access_group')):
                            pass
                            yield '      ip access-group '
                            yield str(environment.getattr(l_1_transport, 'ip_access_group'))
                            yield '\n'
                        if t_2(environment.getattr(l_1_transport, 'notification_timestamp')):
                            pass
                            yield '      notification timestamp '
                            yield str(environment.getattr(l_1_transport, 'notification_timestamp'))
                            yield '\n'
                l_1_transport = missing
        if t_2(environment.getattr((undefined(name='management_api_gnmi') if l_0_management_api_gnmi is missing else l_0_management_api_gnmi), 'provider')):
            pass
            yield '   provider '
            yield str(environment.getattr((undefined(name='management_api_gnmi') if l_0_management_api_gnmi is missing else l_0_management_api_gnmi), 'provider'))
            yield '\n'

blocks = {}
debug_info = '2=30&5=33&6=36&9=42&10=44&11=47&13=50&16=53&19=56&20=58&21=60&22=63&23=66&24=68&25=71&27=73&28=76&30=78&31=81&33=83&34=86&40=89&41=92'