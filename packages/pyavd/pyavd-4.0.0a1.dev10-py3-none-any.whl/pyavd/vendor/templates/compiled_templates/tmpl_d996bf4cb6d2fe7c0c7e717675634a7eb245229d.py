from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/loopback-interfaces.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_loopback_interfaces = resolve('loopback_interfaces')
    try:
        t_1 = environment.filters['arista.avd.natural_sort']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.natural_sort' found.")
    try:
        t_2 = environment.filters['indent']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No filter named 'indent' found.")
    try:
        t_3 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    for l_1_loopback_interface in t_1((undefined(name='loopback_interfaces') if l_0_loopback_interfaces is missing else l_0_loopback_interfaces), 'name'):
        _loop_vars = {}
        pass
        yield '!\ninterface '
        yield str(environment.getattr(l_1_loopback_interface, 'name'))
        yield '\n'
        if t_3(environment.getattr(l_1_loopback_interface, 'description')):
            pass
            yield '   description '
            yield str(environment.getattr(l_1_loopback_interface, 'description'))
            yield '\n'
        if t_3(environment.getattr(l_1_loopback_interface, 'shutdown'), True):
            pass
            yield '   shutdown\n'
        elif t_3(environment.getattr(l_1_loopback_interface, 'shutdown'), False):
            pass
            yield '   no shutdown\n'
        if t_3(environment.getattr(l_1_loopback_interface, 'vrf')):
            pass
            yield '   vrf '
            yield str(environment.getattr(l_1_loopback_interface, 'vrf'))
            yield '\n'
        if t_3(environment.getattr(l_1_loopback_interface, 'ip_proxy_arp'), True):
            pass
            yield '   ip proxy-arp\n'
        if t_3(environment.getattr(l_1_loopback_interface, 'ip_address')):
            pass
            yield '   ip address '
            yield str(environment.getattr(l_1_loopback_interface, 'ip_address'))
            yield '\n'
            for l_2_ip_address_secondary in t_1(environment.getattr(l_1_loopback_interface, 'ip_address_secondaries')):
                _loop_vars = {}
                pass
                yield '   ip address '
                yield str(l_2_ip_address_secondary)
                yield ' secondary\n'
            l_2_ip_address_secondary = missing
        if t_3(environment.getattr(l_1_loopback_interface, 'ipv6_enable'), True):
            pass
            yield '   ipv6 enable\n'
        if t_3(environment.getattr(l_1_loopback_interface, 'ipv6_address')):
            pass
            yield '   ipv6 address '
            yield str(environment.getattr(l_1_loopback_interface, 'ipv6_address'))
            yield '\n'
        if t_3(environment.getattr(l_1_loopback_interface, 'ospf_area')):
            pass
            yield '   ip ospf area '
            yield str(environment.getattr(l_1_loopback_interface, 'ospf_area'))
            yield '\n'
        if t_3(environment.getattr(l_1_loopback_interface, 'isis_enable')):
            pass
            yield '   isis enable '
            yield str(environment.getattr(l_1_loopback_interface, 'isis_enable'))
            yield '\n'
        if t_3(environment.getattr(l_1_loopback_interface, 'isis_passive'), True):
            pass
            yield '   isis passive\n'
        if t_3(environment.getattr(l_1_loopback_interface, 'isis_metric')):
            pass
            yield '   isis metric '
            yield str(environment.getattr(l_1_loopback_interface, 'isis_metric'))
            yield '\n'
        if t_3(environment.getattr(l_1_loopback_interface, 'isis_network_point_to_point'), True):
            pass
            yield '   isis network point-to-point\n'
        if t_3(environment.getattr(environment.getattr(environment.getattr(l_1_loopback_interface, 'mpls'), 'ldp'), 'interface'), True):
            pass
            yield '   mpls ldp interface\n'
        elif t_3(environment.getattr(environment.getattr(environment.getattr(l_1_loopback_interface, 'mpls'), 'ldp'), 'interface'), False):
            pass
            yield '   no mpls ldp interface\n'
        if t_3(environment.getattr(environment.getattr(l_1_loopback_interface, 'node_segment'), 'ipv4_index')):
            pass
            yield '   node-segment ipv4 index '
            yield str(environment.getattr(environment.getattr(l_1_loopback_interface, 'node_segment'), 'ipv4_index'))
            yield '\n'
        if t_3(environment.getattr(environment.getattr(l_1_loopback_interface, 'node_segment'), 'ipv6_index')):
            pass
            yield '   node-segment ipv6 index '
            yield str(environment.getattr(environment.getattr(l_1_loopback_interface, 'node_segment'), 'ipv6_index'))
            yield '\n'
        if t_3(environment.getattr(l_1_loopback_interface, 'eos_cli')):
            pass
            yield '   '
            yield str(t_2(environment.getattr(l_1_loopback_interface, 'eos_cli'), 3, False))
            yield '\n'
    l_1_loopback_interface = missing

blocks = {}
debug_info = '2=30&4=34&5=36&6=39&8=41&10=44&13=47&14=50&16=52&19=55&20=58&21=60&22=64&25=67&28=70&29=73&31=75&32=78&34=80&35=83&37=85&40=88&41=91&43=93&46=96&48=99&51=102&52=105&54=107&55=110&57=112&58=115'