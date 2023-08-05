from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/cvx.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_cvx = resolve('cvx')
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
    if t_3((undefined(name='cvx') if l_0_cvx is missing else l_0_cvx)):
        pass
        yield '!\ncvx\n'
        if t_3(environment.getattr((undefined(name='cvx') if l_0_cvx is missing else l_0_cvx), 'shutdown'), True):
            pass
            yield '   shutdown\n'
        elif t_3(environment.getattr((undefined(name='cvx') if l_0_cvx is missing else l_0_cvx), 'shutdown'), False):
            pass
            yield '   no shutdown\n'
        for l_1_peer_host in t_2(environment.getattr((undefined(name='cvx') if l_0_cvx is missing else l_0_cvx), 'peer_hosts')):
            _loop_vars = {}
            pass
            yield '   peer host '
            yield str(l_1_peer_host)
            yield '\n'
        l_1_peer_host = missing
        if t_3(environment.getattr((undefined(name='cvx') if l_0_cvx is missing else l_0_cvx), 'services')):
            pass
            if t_3(environment.getattr(environment.getattr((undefined(name='cvx') if l_0_cvx is missing else l_0_cvx), 'services'), 'mcs')):
                pass
                yield '   service mcs\n'
                if t_3(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='cvx') if l_0_cvx is missing else l_0_cvx), 'services'), 'mcs'), 'redis'), 'password')):
                    pass
                    yield '      redis password '
                    yield str(t_1(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='cvx') if l_0_cvx is missing else l_0_cvx), 'services'), 'mcs'), 'redis'), 'password_type'), '7'))
                    yield ' '
                    yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='cvx') if l_0_cvx is missing else l_0_cvx), 'services'), 'mcs'), 'redis'), 'password'))
                    yield '\n'
                if t_3(environment.getattr(environment.getattr(environment.getattr((undefined(name='cvx') if l_0_cvx is missing else l_0_cvx), 'services'), 'mcs'), 'shutdown'), False):
                    pass
                    yield '      no shutdown\n'
                elif t_3(environment.getattr(environment.getattr(environment.getattr((undefined(name='cvx') if l_0_cvx is missing else l_0_cvx), 'services'), 'mcs'), 'shutdown'), True):
                    pass
                    yield '      shutdown\n'
            if t_3(environment.getattr(environment.getattr((undefined(name='cvx') if l_0_cvx is missing else l_0_cvx), 'services'), 'vxlan')):
                pass
                yield '   service vxlan\n'
                if t_3(environment.getattr(environment.getattr(environment.getattr((undefined(name='cvx') if l_0_cvx is missing else l_0_cvx), 'services'), 'vxlan'), 'shutdown'), False):
                    pass
                    yield '      no shutdown\n'
                elif t_3(environment.getattr(environment.getattr(environment.getattr((undefined(name='cvx') if l_0_cvx is missing else l_0_cvx), 'services'), 'vxlan'), 'shutdown'), True):
                    pass
                    yield '      shutdown\n'
                if t_3(environment.getattr(environment.getattr(environment.getattr((undefined(name='cvx') if l_0_cvx is missing else l_0_cvx), 'services'), 'vxlan'), 'vtep_mac_learning')):
                    pass
                    yield '      vtep mac-learning '
                    yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='cvx') if l_0_cvx is missing else l_0_cvx), 'services'), 'vxlan'), 'vtep_mac_learning'))
                    yield '\n'

blocks = {}
debug_info = '2=30&5=33&7=36&10=39&11=43&13=46&14=48&16=51&17=54&19=58&21=61&25=64&27=67&29=70&32=73&33=76'