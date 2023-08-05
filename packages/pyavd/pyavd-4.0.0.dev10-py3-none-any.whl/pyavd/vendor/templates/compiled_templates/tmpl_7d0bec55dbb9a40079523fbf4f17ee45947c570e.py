from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/ethernet-interfaces.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_ethernet_interfaces = resolve('ethernet_interfaces')
    l_0_POE_CLASS_MAP = missing
    try:
        t_1 = environment.filters['arista.avd.convert_dicts']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.convert_dicts' found.")
    try:
        t_2 = environment.filters['arista.avd.default']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.default' found.")
    try:
        t_3 = environment.filters['arista.avd.natural_sort']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.natural_sort' found.")
    try:
        t_4 = environment.filters['float']
    except KeyError:
        @internalcode
        def t_4(*unused):
            raise TemplateRuntimeError("No filter named 'float' found.")
    try:
        t_5 = environment.filters['format']
    except KeyError:
        @internalcode
        def t_5(*unused):
            raise TemplateRuntimeError("No filter named 'format' found.")
    try:
        t_6 = environment.filters['indent']
    except KeyError:
        @internalcode
        def t_6(*unused):
            raise TemplateRuntimeError("No filter named 'indent' found.")
    try:
        t_7 = environment.filters['length']
    except KeyError:
        @internalcode
        def t_7(*unused):
            raise TemplateRuntimeError("No filter named 'length' found.")
    try:
        t_8 = environment.filters['list']
    except KeyError:
        @internalcode
        def t_8(*unused):
            raise TemplateRuntimeError("No filter named 'list' found.")
    try:
        t_9 = environment.filters['replace']
    except KeyError:
        @internalcode
        def t_9(*unused):
            raise TemplateRuntimeError("No filter named 'replace' found.")
    try:
        t_10 = environment.filters['selectattr']
    except KeyError:
        @internalcode
        def t_10(*unused):
            raise TemplateRuntimeError("No filter named 'selectattr' found.")
    try:
        t_11 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_11(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    l_0_POE_CLASS_MAP = {0: '15.40', 1: '4.00', 2: '7.00', 3: '15.40', 4: '30.00', 5: '45.00', 6: '60.00', 7: '75.00', 8: '90.00'}
    context.vars['POE_CLASS_MAP'] = l_0_POE_CLASS_MAP
    context.exported_vars.add('POE_CLASS_MAP')
    for l_1_ethernet_interface in t_3((undefined(name='ethernet_interfaces') if l_0_ethernet_interfaces is missing else l_0_ethernet_interfaces), 'name'):
        l_1_port_channel_interface_name = resolve('port_channel_interface_name')
        l_1_port_channel_interfaces = resolve('port_channel_interfaces')
        l_1_print_ethernet = resolve('print_ethernet')
        l_1_encapsulation_cli = resolve('encapsulation_cli')
        l_1_dfe_algo_cli = resolve('dfe_algo_cli')
        l_1_dfe_hold_time_cli = resolve('dfe_hold_time_cli')
        l_1_host_mode_cli = resolve('host_mode_cli')
        l_1_auth_cli = resolve('auth_cli')
        l_1_auth_failure_fallback_mba = resolve('auth_failure_fallback_mba')
        l_1_address_locking_cli = resolve('address_locking_cli')
        l_1_poe_link_down_action_cli = resolve('poe_link_down_action_cli')
        l_1_poe_limit_cli = resolve('poe_limit_cli')
        _loop_vars = {}
        pass
        if (t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'channel_group'), 'id')) and t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'channel_group'), 'mode'))):
            pass
            l_1_port_channel_interface_name = str_join(('Port-Channel', environment.getattr(environment.getattr(l_1_ethernet_interface, 'channel_group'), 'id'), ))
            _loop_vars['port_channel_interface_name'] = l_1_port_channel_interface_name
            if (t_7(t_8(context.eval_ctx, t_10(context, t_10(context, t_1(t_2((undefined(name='port_channel_interfaces') if l_1_port_channel_interfaces is missing else l_1_port_channel_interfaces), []), 'name'), 'name', 'arista.avd.defined', (undefined(name='port_channel_interface_name') if l_1_port_channel_interface_name is missing else l_1_port_channel_interface_name)), 'lacp_fallback_mode', 'arista.avd.defined', 'individual'))) > 0):
                pass
                l_1_print_ethernet = True
                _loop_vars['print_ethernet'] = l_1_print_ethernet
        else:
            pass
            l_1_print_ethernet = True
            _loop_vars['print_ethernet'] = l_1_print_ethernet
        yield '!\ninterface '
        yield str(environment.getattr(l_1_ethernet_interface, 'name'))
        yield '\n'
        if t_11((undefined(name='print_ethernet') if l_1_print_ethernet is missing else l_1_print_ethernet), True):
            pass
            if t_11(environment.getattr(l_1_ethernet_interface, 'profile')):
                pass
                yield '   profile '
                yield str(environment.getattr(l_1_ethernet_interface, 'profile'))
                yield '\n'
        if t_11(environment.getattr(l_1_ethernet_interface, 'description')):
            pass
            yield '   description '
            yield str(environment.getattr(l_1_ethernet_interface, 'description'))
            yield '\n'
        if t_11(environment.getattr(l_1_ethernet_interface, 'shutdown'), True):
            pass
            yield '   shutdown\n'
        elif t_11(environment.getattr(l_1_ethernet_interface, 'shutdown'), False):
            pass
            yield '   no shutdown\n'
        if t_11(environment.getattr(l_1_ethernet_interface, 'load_interval')):
            pass
            yield '   load-interval '
            yield str(environment.getattr(l_1_ethernet_interface, 'load_interval'))
            yield '\n'
        if t_11((undefined(name='print_ethernet') if l_1_print_ethernet is missing else l_1_print_ethernet), True):
            pass
            if t_11(environment.getattr(l_1_ethernet_interface, 'mtu')):
                pass
                yield '   mtu '
                yield str(environment.getattr(l_1_ethernet_interface, 'mtu'))
                yield '\n'
        if t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'logging'), 'event')):
            pass
            if t_11(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'logging'), 'event'), 'link_status'), True):
                pass
                yield '   logging event link-status\n'
            elif t_11(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'logging'), 'event'), 'link_status'), False):
                pass
                yield '   no logging event link-status\n'
            if t_11(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'logging'), 'event'), 'congestion_drops'), True):
                pass
                yield '   logging event congestion-drops\n'
            elif t_11(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'logging'), 'event'), 'congestion_drops'), False):
                pass
                yield '   no logging event congestion-drops\n'
        if t_11((undefined(name='print_ethernet') if l_1_print_ethernet is missing else l_1_print_ethernet), True):
            pass
            if t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'flowcontrol'), 'received')):
                pass
                yield '   flowcontrol receive '
                yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'flowcontrol'), 'received'))
                yield '\n'
        if t_11(environment.getattr(l_1_ethernet_interface, 'speed')):
            pass
            yield '   speed '
            yield str(environment.getattr(l_1_ethernet_interface, 'speed'))
            yield '\n'
        if t_11((undefined(name='print_ethernet') if l_1_print_ethernet is missing else l_1_print_ethernet), True):
            pass
            if t_11(environment.getattr(l_1_ethernet_interface, 'l2_mtu')):
                pass
                yield '   l2 mtu '
                yield str(environment.getattr(l_1_ethernet_interface, 'l2_mtu'))
                yield '\n'
        if t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'bgp'), 'session_tracker')):
            pass
            yield '   bgp session tracker '
            yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'bgp'), 'session_tracker'))
            yield '\n'
        if t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'mac_security'), 'profile')):
            pass
            yield '   mac security profile '
            yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'mac_security'), 'profile'))
            yield '\n'
        if t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'error_correction_encoding'), 'enabled'), False):
            pass
            yield '   no error-correction encoding\n'
        else:
            pass
            if t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'error_correction_encoding'), 'fire_code'), True):
                pass
                yield '   error-correction encoding fire-code\n'
            elif t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'error_correction_encoding'), 'fire_code'), False):
                pass
                yield '   no error-correction encoding fire-code\n'
            if t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'error_correction_encoding'), 'reed_solomon'), True):
                pass
                yield '   error-correction encoding reed-solomon\n'
            elif t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'error_correction_encoding'), 'reed_solomon'), False):
                pass
                yield '   no error-correction encoding reed-solomon\n'
        if t_11((undefined(name='print_ethernet') if l_1_print_ethernet is missing else l_1_print_ethernet), True):
            pass
            if (t_11(environment.getattr(l_1_ethernet_interface, 'mode'), 'access') or t_11(environment.getattr(l_1_ethernet_interface, 'mode'), 'dot1q-tunnel')):
                pass
                if t_11(environment.getattr(l_1_ethernet_interface, 'vlans')):
                    pass
                    yield '   switchport access vlan '
                    yield str(environment.getattr(l_1_ethernet_interface, 'vlans'))
                    yield '\n'
            if (t_11(environment.getattr(l_1_ethernet_interface, 'mode')) and (environment.getattr(l_1_ethernet_interface, 'mode') in ['trunk', 'trunk phone'])):
                pass
                if t_11(environment.getattr(l_1_ethernet_interface, 'native_vlan_tag'), True):
                    pass
                    yield '   switchport trunk native vlan tag\n'
                elif t_11(environment.getattr(l_1_ethernet_interface, 'native_vlan')):
                    pass
                    yield '   switchport trunk native vlan '
                    yield str(environment.getattr(l_1_ethernet_interface, 'native_vlan'))
                    yield '\n'
            if t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'phone'), 'vlan')):
                pass
                yield '   switchport phone vlan '
                yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'phone'), 'vlan'))
                yield '\n'
            if t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'phone'), 'trunk')):
                pass
                yield '   switchport phone trunk '
                yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'phone'), 'trunk'))
                yield '\n'
            for l_2_vlan_translation in t_3(environment.getattr(l_1_ethernet_interface, 'vlan_translations')):
                l_2_vlan_translation_cli = resolve('vlan_translation_cli')
                _loop_vars = {}
                pass
                if (t_11(environment.getattr(l_2_vlan_translation, 'from')) and t_11(environment.getattr(l_2_vlan_translation, 'to'))):
                    pass
                    l_2_vlan_translation_cli = 'switchport vlan translation'
                    _loop_vars['vlan_translation_cli'] = l_2_vlan_translation_cli
                    if (t_2(environment.getattr(l_2_vlan_translation, 'direction')) in ['in', 'out']):
                        pass
                        l_2_vlan_translation_cli = str_join(((undefined(name='vlan_translation_cli') if l_2_vlan_translation_cli is missing else l_2_vlan_translation_cli), ' ', environment.getattr(l_2_vlan_translation, 'direction'), ))
                        _loop_vars['vlan_translation_cli'] = l_2_vlan_translation_cli
                    l_2_vlan_translation_cli = str_join(((undefined(name='vlan_translation_cli') if l_2_vlan_translation_cli is missing else l_2_vlan_translation_cli), ' ', environment.getattr(l_2_vlan_translation, 'from'), ))
                    _loop_vars['vlan_translation_cli'] = l_2_vlan_translation_cli
                    l_2_vlan_translation_cli = str_join(((undefined(name='vlan_translation_cli') if l_2_vlan_translation_cli is missing else l_2_vlan_translation_cli), ' ', environment.getattr(l_2_vlan_translation, 'to'), ))
                    _loop_vars['vlan_translation_cli'] = l_2_vlan_translation_cli
                    yield '   '
                    yield str((undefined(name='vlan_translation_cli') if l_2_vlan_translation_cli is missing else l_2_vlan_translation_cli))
                    yield '\n'
            l_2_vlan_translation = l_2_vlan_translation_cli = missing
            if t_11(environment.getattr(l_1_ethernet_interface, 'mode'), 'trunk'):
                pass
                if t_11(environment.getattr(l_1_ethernet_interface, 'vlans')):
                    pass
                    yield '   switchport trunk allowed vlan '
                    yield str(environment.getattr(l_1_ethernet_interface, 'vlans'))
                    yield '\n'
            if t_11(environment.getattr(l_1_ethernet_interface, 'mode')):
                pass
                yield '   switchport mode '
                yield str(environment.getattr(l_1_ethernet_interface, 'mode'))
                yield '\n'
            for l_2_trunk_group in t_3(environment.getattr(l_1_ethernet_interface, 'trunk_groups')):
                _loop_vars = {}
                pass
                yield '   switchport trunk group '
                yield str(l_2_trunk_group)
                yield '\n'
            l_2_trunk_group = missing
            if t_11(environment.getattr(l_1_ethernet_interface, 'type'), 'routed'):
                pass
                yield '   no switchport\n'
            elif (t_2(environment.getattr(l_1_ethernet_interface, 'type')) in ['l3dot1q', 'l2dot1q']):
                pass
                if (t_11(environment.getattr(l_1_ethernet_interface, 'vlan_id')) and (environment.getattr(l_1_ethernet_interface, 'type') == 'l2dot1q')):
                    pass
                    yield '   vlan id '
                    yield str(environment.getattr(l_1_ethernet_interface, 'vlan_id'))
                    yield '\n'
                if t_11(environment.getattr(l_1_ethernet_interface, 'encapsulation_dot1q_vlan')):
                    pass
                    yield '   encapsulation dot1q vlan '
                    yield str(environment.getattr(l_1_ethernet_interface, 'encapsulation_dot1q_vlan'))
                    yield '\n'
                elif t_11(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'client'), 'dot1q'), 'vlan')):
                    pass
                    l_1_encapsulation_cli = str_join(('client dot1q ', environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'client'), 'dot1q'), 'vlan'), ))
                    _loop_vars['encapsulation_cli'] = l_1_encapsulation_cli
                    if t_11(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'network'), 'dot1q'), 'vlan')):
                        pass
                        l_1_encapsulation_cli = str_join(((undefined(name='encapsulation_cli') if l_1_encapsulation_cli is missing else l_1_encapsulation_cli), ' network dot1q ', environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'network'), 'dot1q'), 'vlan'), ))
                        _loop_vars['encapsulation_cli'] = l_1_encapsulation_cli
                    elif t_11(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'network'), 'client'), True):
                        pass
                        l_1_encapsulation_cli = str_join(((undefined(name='encapsulation_cli') if l_1_encapsulation_cli is missing else l_1_encapsulation_cli), ' network client', ))
                        _loop_vars['encapsulation_cli'] = l_1_encapsulation_cli
                elif (t_11(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'client'), 'dot1q'), 'inner')) and t_11(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'client'), 'dot1q'), 'outer'))):
                    pass
                    l_1_encapsulation_cli = str_join(('client dot1q outer ', environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'client'), 'dot1q'), 'outer'), ' inner ', environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'client'), 'dot1q'), 'inner'), ))
                    _loop_vars['encapsulation_cli'] = l_1_encapsulation_cli
                    if (t_11(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'network'), 'dot1q'), 'inner')) and t_11(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'network'), 'dot1q'), 'outer'))):
                        pass
                        l_1_encapsulation_cli = str_join(((undefined(name='encapsulation_cli') if l_1_encapsulation_cli is missing else l_1_encapsulation_cli), ' network dot1q outer ', environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'network'), 'dot1q'), 'inner'), ' inner ', environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'network'), 'dot1q'), 'outer'), ))
                        _loop_vars['encapsulation_cli'] = l_1_encapsulation_cli
                    elif t_11(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'network'), 'dot1q'), 'client'), True):
                        pass
                        l_1_encapsulation_cli = str_join(((undefined(name='encapsulation_cli') if l_1_encapsulation_cli is missing else l_1_encapsulation_cli), ' network client', ))
                        _loop_vars['encapsulation_cli'] = l_1_encapsulation_cli
                elif t_11(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'encapsulation_vlan'), 'client'), 'unmatched'), True):
                    pass
                    l_1_encapsulation_cli = 'client unmatched'
                    _loop_vars['encapsulation_cli'] = l_1_encapsulation_cli
                if t_11((undefined(name='encapsulation_cli') if l_1_encapsulation_cli is missing else l_1_encapsulation_cli)):
                    pass
                    yield '   encapsulation vlan\n      '
                    yield str((undefined(name='encapsulation_cli') if l_1_encapsulation_cli is missing else l_1_encapsulation_cli))
                    yield '\n'
            else:
                pass
                yield '   switchport\n'
            if t_11(environment.getattr(l_1_ethernet_interface, 'trunk_private_vlan_secondary'), True):
                pass
                yield '   switchport trunk private-vlan secondary\n'
            elif t_11(environment.getattr(l_1_ethernet_interface, 'trunk_private_vlan_secondary'), False):
                pass
                yield '   no switchport trunk private-vlan secondary\n'
            if t_11(environment.getattr(l_1_ethernet_interface, 'pvlan_mapping')):
                pass
                yield '   switchport pvlan mapping '
                yield str(environment.getattr(l_1_ethernet_interface, 'pvlan_mapping'))
                yield '\n'
            if t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'l2_protocol'), 'encapsulation_dot1q_vlan')):
                pass
                yield '   l2-protocol encapsulation dot1q vlan '
                yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'l2_protocol'), 'encapsulation_dot1q_vlan'))
                yield '\n'
            if t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'l2_protocol'), 'forwarding_profile')):
                pass
                yield '   l2-protocol forwarding profile '
                yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'l2_protocol'), 'forwarding_profile'))
                yield '\n'
            if t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'flow_tracker'), 'sampled')):
                pass
                yield '   flow tracker sampled '
                yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'flow_tracker'), 'sampled'))
                yield '\n'
            if t_11(environment.getattr(l_1_ethernet_interface, 'evpn_ethernet_segment')):
                pass
                yield '   evpn ethernet-segment\n'
                if t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'evpn_ethernet_segment'), 'identifier')):
                    pass
                    yield '      identifier '
                    yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'evpn_ethernet_segment'), 'identifier'))
                    yield '\n'
                if t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'evpn_ethernet_segment'), 'redundancy')):
                    pass
                    yield '      redundancy '
                    yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'evpn_ethernet_segment'), 'redundancy'))
                    yield '\n'
                if t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'evpn_ethernet_segment'), 'designated_forwarder_election')):
                    pass
                    if t_11(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'evpn_ethernet_segment'), 'designated_forwarder_election'), 'algorithm'), 'modulus'):
                        pass
                        yield '      designated-forwarder election algorithm modulus\n'
                    elif (t_11(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'evpn_ethernet_segment'), 'designated_forwarder_election'), 'algorithm'), 'preference') and t_11(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'evpn_ethernet_segment'), 'designated_forwarder_election'), 'preference_value'))):
                        pass
                        l_1_dfe_algo_cli = str_join(('designated-forwarder election algorithm preference ', environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'evpn_ethernet_segment'), 'designated_forwarder_election'), 'preference_value'), ))
                        _loop_vars['dfe_algo_cli'] = l_1_dfe_algo_cli
                        if t_11(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'evpn_ethernet_segment'), 'designated_forwarder_election'), 'dont_preempt'), True):
                            pass
                            l_1_dfe_algo_cli = str_join(((undefined(name='dfe_algo_cli') if l_1_dfe_algo_cli is missing else l_1_dfe_algo_cli), ' dont-preempt', ))
                            _loop_vars['dfe_algo_cli'] = l_1_dfe_algo_cli
                        yield '      '
                        yield str((undefined(name='dfe_algo_cli') if l_1_dfe_algo_cli is missing else l_1_dfe_algo_cli))
                        yield '\n'
                    if t_11(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'evpn_ethernet_segment'), 'designated_forwarder_election'), 'hold_time')):
                        pass
                        l_1_dfe_hold_time_cli = str_join(('designated-forwarder election hold-time ', environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'evpn_ethernet_segment'), 'designated_forwarder_election'), 'hold_time'), ))
                        _loop_vars['dfe_hold_time_cli'] = l_1_dfe_hold_time_cli
                        if t_11(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'evpn_ethernet_segment'), 'designated_forwarder_election'), 'subsequent_hold_time')):
                            pass
                            l_1_dfe_hold_time_cli = str_join(((undefined(name='dfe_hold_time_cli') if l_1_dfe_hold_time_cli is missing else l_1_dfe_hold_time_cli), ' subsequent-hold-time ', environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'evpn_ethernet_segment'), 'designated_forwarder_election'), 'subsequent_hold_time'), ))
                            _loop_vars['dfe_hold_time_cli'] = l_1_dfe_hold_time_cli
                        yield '      '
                        yield str((undefined(name='dfe_hold_time_cli') if l_1_dfe_hold_time_cli is missing else l_1_dfe_hold_time_cli))
                        yield '\n'
                    if t_11(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'evpn_ethernet_segment'), 'designated_forwarder_election'), 'candidate_reachability_required'), True):
                        pass
                        yield '      designated-forwarder election candidate reachability required\n'
                    elif t_11(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'evpn_ethernet_segment'), 'designated_forwarder_election'), 'candidate_reachability_required'), False):
                        pass
                        yield '      no designated-forwarder election candidate reachability required\n'
                if t_11(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'evpn_ethernet_segment'), 'mpls'), 'tunnel_flood_filter_time')):
                    pass
                    yield '      mpls tunnel flood filter time '
                    yield str(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'evpn_ethernet_segment'), 'mpls'), 'tunnel_flood_filter_time'))
                    yield '\n'
                if t_11(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'evpn_ethernet_segment'), 'mpls'), 'shared_index')):
                    pass
                    yield '      mpls shared index '
                    yield str(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'evpn_ethernet_segment'), 'mpls'), 'shared_index'))
                    yield '\n'
                if t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'evpn_ethernet_segment'), 'route_target')):
                    pass
                    yield '      route-target import '
                    yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'evpn_ethernet_segment'), 'route_target'))
                    yield '\n'
            if t_11(environment.getattr(l_1_ethernet_interface, 'dot1x')):
                pass
                if t_11(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'pae'), 'mode')):
                    pass
                    yield '   dot1x pae '
                    yield str(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'pae'), 'mode'))
                    yield '\n'
                if t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'authentication_failure')):
                    pass
                    if (t_11(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'authentication_failure'), 'action'), 'allow') and t_11(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'authentication_failure'), 'allow_vlan'))):
                        pass
                        yield '   dot1x authentication failure action traffic allow vlan '
                        yield str(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'authentication_failure'), 'allow_vlan'))
                        yield '\n'
                    elif t_11(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'authentication_failure'), 'action'), 'drop'):
                        pass
                        yield '   dot1x authentication failure action traffic drop\n'
                if t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'reauthentication'), True):
                    pass
                    yield '   dot1x reauthentication\n'
                if t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'port_control')):
                    pass
                    yield '   dot1x port-control '
                    yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'port_control'))
                    yield '\n'
                if t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'port_control_force_authorized_phone'), True):
                    pass
                    yield '   dot1x port-control force-authorized phone\n'
                elif t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'port_control_force_authorized_phone'), False):
                    pass
                    yield '   no dot1x port-control force-authorized phone\n'
                if t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'host_mode')):
                    pass
                    if t_11(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'host_mode'), 'mode'), 'single-host'):
                        pass
                        yield '   dot1x host-mode single-host\n'
                    elif t_11(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'host_mode'), 'mode'), 'multi-host'):
                        pass
                        l_1_host_mode_cli = 'dot1x host-mode multi-host'
                        _loop_vars['host_mode_cli'] = l_1_host_mode_cli
                        if t_11(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'host_mode'), 'multi_host_authenticated'), True):
                            pass
                            l_1_host_mode_cli = str_join(((undefined(name='host_mode_cli') if l_1_host_mode_cli is missing else l_1_host_mode_cli), ' authenticated', ))
                            _loop_vars['host_mode_cli'] = l_1_host_mode_cli
                        yield '   '
                        yield str((undefined(name='host_mode_cli') if l_1_host_mode_cli is missing else l_1_host_mode_cli))
                        yield '\n'
                if t_11(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'mac_based_authentication'), 'enabled'), True):
                    pass
                    if t_11(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'mac_based_authentication'), 'host_mode_common'), True):
                        pass
                        yield '   dot1x mac based authentication host-mode common\n'
                        if t_11(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'mac_based_authentication'), 'always'), True):
                            pass
                            yield '   dot1x mac based authentication always\n'
                    else:
                        pass
                        l_1_auth_cli = 'dot1x mac based authentication'
                        _loop_vars['auth_cli'] = l_1_auth_cli
                        if t_11(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'mac_based_authentication'), 'always'), True):
                            pass
                            l_1_auth_cli = str_join(((undefined(name='auth_cli') if l_1_auth_cli is missing else l_1_auth_cli), ' always', ))
                            _loop_vars['auth_cli'] = l_1_auth_cli
                        yield '   '
                        yield str((undefined(name='auth_cli') if l_1_auth_cli is missing else l_1_auth_cli))
                        yield '\n'
                if t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'timeout')):
                    pass
                    if t_11(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'timeout'), 'quiet_period')):
                        pass
                        yield '   dot1x timeout quiet-period '
                        yield str(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'timeout'), 'quiet_period'))
                        yield '\n'
                    if t_11(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'timeout'), 'reauth_timeout_ignore'), True):
                        pass
                        yield '   dot1x timeout reauth-timeout-ignore always\n'
                    if t_11(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'timeout'), 'tx_period')):
                        pass
                        yield '   dot1x timeout tx-period '
                        yield str(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'timeout'), 'tx_period'))
                        yield '\n'
                    if t_11(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'timeout'), 'reauth_period')):
                        pass
                        yield '   dot1x timeout reauth-period '
                        yield str(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'timeout'), 'reauth_period'))
                        yield '\n'
                    if t_11(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'timeout'), 'idle_host')):
                        pass
                        yield '   dot1x timeout idle-host '
                        yield str(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'timeout'), 'idle_host'))
                        yield ' seconds\n'
                if t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'reauthorization_request_limit')):
                    pass
                    yield '   dot1x reauthorization request limit '
                    yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'reauthorization_request_limit'))
                    yield '\n'
                if t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'eapol')):
                    pass
                    if t_11(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'eapol'), 'disabled'), True):
                        pass
                        yield '   dot1x eapol disabled\n'
                    elif t_11(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'eapol'), 'authentication_failure_fallback_mba'), 'enabled'), True):
                        pass
                        l_1_auth_failure_fallback_mba = 'dot1x eapol authentication failure fallback mba'
                        _loop_vars['auth_failure_fallback_mba'] = l_1_auth_failure_fallback_mba
                        if t_11(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'eapol'), 'authentication_failure_fallback_mba'), 'timeout')):
                            pass
                            l_1_auth_failure_fallback_mba = str_join(((undefined(name='auth_failure_fallback_mba') if l_1_auth_failure_fallback_mba is missing else l_1_auth_failure_fallback_mba), ' timeout ', environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'dot1x'), 'eapol'), 'authentication_failure_fallback_mba'), 'timeout'), ))
                            _loop_vars['auth_failure_fallback_mba'] = l_1_auth_failure_fallback_mba
                        yield '   '
                        yield str((undefined(name='auth_failure_fallback_mba') if l_1_auth_failure_fallback_mba is missing else l_1_auth_failure_fallback_mba))
                        yield '\n'
            if t_11(environment.getattr(l_1_ethernet_interface, 'snmp_trap_link_change'), False):
                pass
                yield '   no snmp trap link-change\n'
            elif t_11(environment.getattr(l_1_ethernet_interface, 'snmp_trap_link_change'), True):
                pass
                yield '   snmp trap link-change\n'
            if (t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'address_locking'), 'ipv4'), True) or t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'address_locking'), 'ipv6'), True)):
                pass
                l_1_address_locking_cli = 'address locking'
                _loop_vars['address_locking_cli'] = l_1_address_locking_cli
                if t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'address_locking'), 'ipv4'), True):
                    pass
                    l_1_address_locking_cli = ((undefined(name='address_locking_cli') if l_1_address_locking_cli is missing else l_1_address_locking_cli) + ' ipv4')
                    _loop_vars['address_locking_cli'] = l_1_address_locking_cli
                if t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'address_locking'), 'ipv6'), True):
                    pass
                    l_1_address_locking_cli = ((undefined(name='address_locking_cli') if l_1_address_locking_cli is missing else l_1_address_locking_cli) + ' ipv6')
                    _loop_vars['address_locking_cli'] = l_1_address_locking_cli
                yield '   '
                yield str((undefined(name='address_locking_cli') if l_1_address_locking_cli is missing else l_1_address_locking_cli))
                yield '\n'
            if t_11(environment.getattr(l_1_ethernet_interface, 'vrf')):
                pass
                yield '   vrf '
                yield str(environment.getattr(l_1_ethernet_interface, 'vrf'))
                yield '\n'
            if t_11(environment.getattr(l_1_ethernet_interface, 'ip_proxy_arp'), True):
                pass
                yield '   ip proxy-arp\n'
            if t_11(environment.getattr(l_1_ethernet_interface, 'ip_address')):
                pass
                yield '   ip address '
                yield str(environment.getattr(l_1_ethernet_interface, 'ip_address'))
                yield '\n'
                if t_11(environment.getattr(l_1_ethernet_interface, 'ip_address_secondaries')):
                    pass
                    for l_2_ip_address_secondary in environment.getattr(l_1_ethernet_interface, 'ip_address_secondaries'):
                        _loop_vars = {}
                        pass
                        yield '   ip address '
                        yield str(l_2_ip_address_secondary)
                        yield ' secondary\n'
                    l_2_ip_address_secondary = missing
                for l_2_ip_helper in t_3(environment.getattr(l_1_ethernet_interface, 'ip_helpers'), 'ip_helper'):
                    l_2_ip_helper_cli = missing
                    _loop_vars = {}
                    pass
                    l_2_ip_helper_cli = str_join(('ip helper-address ', environment.getattr(l_2_ip_helper, 'ip_helper'), ))
                    _loop_vars['ip_helper_cli'] = l_2_ip_helper_cli
                    if t_11(environment.getattr(l_2_ip_helper, 'vrf')):
                        pass
                        l_2_ip_helper_cli = str_join(((undefined(name='ip_helper_cli') if l_2_ip_helper_cli is missing else l_2_ip_helper_cli), ' vrf ', environment.getattr(l_2_ip_helper, 'vrf'), ))
                        _loop_vars['ip_helper_cli'] = l_2_ip_helper_cli
                    if t_11(environment.getattr(l_2_ip_helper, 'source_interface')):
                        pass
                        l_2_ip_helper_cli = str_join(((undefined(name='ip_helper_cli') if l_2_ip_helper_cli is missing else l_2_ip_helper_cli), ' source-interface ', environment.getattr(l_2_ip_helper, 'source_interface'), ))
                        _loop_vars['ip_helper_cli'] = l_2_ip_helper_cli
                    yield '   '
                    yield str((undefined(name='ip_helper_cli') if l_2_ip_helper_cli is missing else l_2_ip_helper_cli))
                    yield '\n'
                l_2_ip_helper = l_2_ip_helper_cli = missing
            if ((t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'bfd'), 'interval')) and t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'bfd'), 'min_rx'))) and t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'bfd'), 'multiplier'))):
                pass
                yield '   bfd interval '
                yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'bfd'), 'interval'))
                yield ' min-rx '
                yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'bfd'), 'min_rx'))
                yield ' multiplier '
                yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'bfd'), 'multiplier'))
                yield '\n'
            if t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'bfd'), 'echo'), True):
                pass
                yield '   bfd echo\n'
            elif t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'bfd'), 'echo'), False):
                pass
                yield '   no bfd echo\n'
            if t_11(environment.getattr(l_1_ethernet_interface, 'ipv6_enable'), True):
                pass
                yield '   ipv6 enable\n'
            if t_11(environment.getattr(l_1_ethernet_interface, 'ipv6_address')):
                pass
                yield '   ipv6 address '
                yield str(environment.getattr(l_1_ethernet_interface, 'ipv6_address'))
                yield '\n'
            if t_11(environment.getattr(l_1_ethernet_interface, 'ipv6_address_link_local')):
                pass
                yield '   ipv6 address '
                yield str(environment.getattr(l_1_ethernet_interface, 'ipv6_address_link_local'))
                yield ' link-local\n'
            if t_11(environment.getattr(l_1_ethernet_interface, 'ipv6_nd_ra_disabled'), True):
                pass
                yield '   ipv6 nd ra disabled\n'
            if t_11(environment.getattr(l_1_ethernet_interface, 'ipv6_nd_managed_config_flag'), True):
                pass
                yield '   ipv6 nd managed-config-flag\n'
            if t_11(environment.getattr(l_1_ethernet_interface, 'ipv6_nd_prefixes')):
                pass
                for l_2_prefix in environment.getattr(l_1_ethernet_interface, 'ipv6_nd_prefixes'):
                    l_2_ipv6_nd_prefix_cli = missing
                    _loop_vars = {}
                    pass
                    l_2_ipv6_nd_prefix_cli = str_join(('ipv6 nd prefix ', environment.getattr(l_2_prefix, 'ipv6_prefix'), ))
                    _loop_vars['ipv6_nd_prefix_cli'] = l_2_ipv6_nd_prefix_cli
                    if t_11(environment.getattr(l_2_prefix, 'valid_lifetime')):
                        pass
                        l_2_ipv6_nd_prefix_cli = str_join(((undefined(name='ipv6_nd_prefix_cli') if l_2_ipv6_nd_prefix_cli is missing else l_2_ipv6_nd_prefix_cli), ' ', environment.getattr(l_2_prefix, 'valid_lifetime'), ))
                        _loop_vars['ipv6_nd_prefix_cli'] = l_2_ipv6_nd_prefix_cli
                        if t_11(environment.getattr(l_2_prefix, 'preferred_lifetime')):
                            pass
                            l_2_ipv6_nd_prefix_cli = str_join(((undefined(name='ipv6_nd_prefix_cli') if l_2_ipv6_nd_prefix_cli is missing else l_2_ipv6_nd_prefix_cli), ' ', environment.getattr(l_2_prefix, 'preferred_lifetime'), ))
                            _loop_vars['ipv6_nd_prefix_cli'] = l_2_ipv6_nd_prefix_cli
                    if t_11(environment.getattr(l_2_prefix, 'no_autoconfig_flag'), True):
                        pass
                        l_2_ipv6_nd_prefix_cli = str_join(((undefined(name='ipv6_nd_prefix_cli') if l_2_ipv6_nd_prefix_cli is missing else l_2_ipv6_nd_prefix_cli), ' no-autoconfig', ))
                        _loop_vars['ipv6_nd_prefix_cli'] = l_2_ipv6_nd_prefix_cli
                    yield '   '
                    yield str((undefined(name='ipv6_nd_prefix_cli') if l_2_ipv6_nd_prefix_cli is missing else l_2_ipv6_nd_prefix_cli))
                    yield '\n'
                l_2_prefix = l_2_ipv6_nd_prefix_cli = missing
        for l_2_destination in t_3(environment.getattr(l_1_ethernet_interface, 'ipv6_dhcp_relay_destinations'), 'address'):
            l_2_destination_cli = missing
            _loop_vars = {}
            pass
            l_2_destination_cli = str_join(('ipv6 dhcp relay destination ', environment.getattr(l_2_destination, 'address'), ))
            _loop_vars['destination_cli'] = l_2_destination_cli
            if t_11(environment.getattr(l_2_destination, 'vrf')):
                pass
                l_2_destination_cli = str_join(((undefined(name='destination_cli') if l_2_destination_cli is missing else l_2_destination_cli), ' vrf ', environment.getattr(l_2_destination, 'vrf'), ))
                _loop_vars['destination_cli'] = l_2_destination_cli
            if t_11(environment.getattr(l_2_destination, 'local_interface')):
                pass
                l_2_destination_cli = str_join(((undefined(name='destination_cli') if l_2_destination_cli is missing else l_2_destination_cli), ' local-interface ', environment.getattr(l_2_destination, 'local_interface'), ))
                _loop_vars['destination_cli'] = l_2_destination_cli
            elif t_11(environment.getattr(l_2_destination, 'source_address')):
                pass
                l_2_destination_cli = str_join(((undefined(name='destination_cli') if l_2_destination_cli is missing else l_2_destination_cli), ' source-address ', environment.getattr(l_2_destination, 'source_address'), ))
                _loop_vars['destination_cli'] = l_2_destination_cli
            if t_11(environment.getattr(l_2_destination, 'link_address')):
                pass
                l_2_destination_cli = str_join(((undefined(name='destination_cli') if l_2_destination_cli is missing else l_2_destination_cli), ' link-address ', environment.getattr(l_2_destination, 'link_address'), ))
                _loop_vars['destination_cli'] = l_2_destination_cli
            yield '   '
            yield str((undefined(name='destination_cli') if l_2_destination_cli is missing else l_2_destination_cli))
            yield '\n'
        l_2_destination = l_2_destination_cli = missing
        if (t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'channel_group'), 'id')) and t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'channel_group'), 'mode'))):
            pass
            yield '   channel-group '
            yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'channel_group'), 'id'))
            yield ' mode '
            yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'channel_group'), 'mode'))
            yield '\n'
            if t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'lacp_timer'), 'mode')):
                pass
                yield '   lacp timer '
                yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'lacp_timer'), 'mode'))
                yield '\n'
            if t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'lacp_timer'), 'multiplier')):
                pass
                yield '   lacp timer multiplier '
                yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'lacp_timer'), 'multiplier'))
                yield '\n'
            if t_11(environment.getattr(l_1_ethernet_interface, 'lacp_port_priority')):
                pass
                yield '   lacp port-priority '
                yield str(environment.getattr(l_1_ethernet_interface, 'lacp_port_priority'))
                yield '\n'
        if t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'lldp'), 'transmit'), False):
            pass
            yield '   no lldp transmit\n'
        if t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'lldp'), 'receive'), False):
            pass
            yield '   no lldp receive\n'
        if t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'lldp'), 'ztp_vlan')):
            pass
            yield '   lldp tlv transmit ztp vlan '
            yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'lldp'), 'ztp_vlan'))
            yield '\n'
        if t_11((undefined(name='print_ethernet') if l_1_print_ethernet is missing else l_1_print_ethernet), True):
            pass
            if t_11(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'mpls'), 'ldp'), 'igp_sync'), True):
                pass
                yield '   mpls ldp igp sync\n'
            if t_11(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'mpls'), 'ldp'), 'interface'), True):
                pass
                yield '   mpls ldp interface\n'
            elif t_11(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'mpls'), 'ldp'), 'interface'), False):
                pass
                yield '   no mpls ldp interface\n'
            if t_11(environment.getattr(l_1_ethernet_interface, 'access_group_in')):
                pass
                yield '   ip access-group '
                yield str(environment.getattr(l_1_ethernet_interface, 'access_group_in'))
                yield ' in\n'
            if t_11(environment.getattr(l_1_ethernet_interface, 'access_group_out')):
                pass
                yield '   ip access-group '
                yield str(environment.getattr(l_1_ethernet_interface, 'access_group_out'))
                yield ' out\n'
            if t_11(environment.getattr(l_1_ethernet_interface, 'ipv6_access_group_in')):
                pass
                yield '   ipv6 access-group '
                yield str(environment.getattr(l_1_ethernet_interface, 'ipv6_access_group_in'))
                yield ' in\n'
            if t_11(environment.getattr(l_1_ethernet_interface, 'ipv6_access_group_out')):
                pass
                yield '   ipv6 access-group '
                yield str(environment.getattr(l_1_ethernet_interface, 'ipv6_access_group_out'))
                yield ' out\n'
            if t_11(environment.getattr(l_1_ethernet_interface, 'mac_access_group_in')):
                pass
                yield '   mac access-group '
                yield str(environment.getattr(l_1_ethernet_interface, 'mac_access_group_in'))
                yield ' in\n'
            if t_11(environment.getattr(l_1_ethernet_interface, 'mac_access_group_out')):
                pass
                yield '   mac access-group '
                yield str(environment.getattr(l_1_ethernet_interface, 'mac_access_group_out'))
                yield ' out\n'
            if t_11(environment.getattr(l_1_ethernet_interface, 'multicast')):
                pass
                if t_11(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'multicast'), 'ipv4'), 'boundaries')):
                    pass
                    for l_2_boundary in environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'multicast'), 'ipv4'), 'boundaries'):
                        l_2_boundary_cli = missing
                        _loop_vars = {}
                        pass
                        l_2_boundary_cli = str_join(('multicast ipv4 boundary ', environment.getattr(l_2_boundary, 'boundary'), ))
                        _loop_vars['boundary_cli'] = l_2_boundary_cli
                        if t_11(environment.getattr(l_2_boundary, 'out'), True):
                            pass
                            l_2_boundary_cli = str_join(((undefined(name='boundary_cli') if l_2_boundary_cli is missing else l_2_boundary_cli), ' out', ))
                            _loop_vars['boundary_cli'] = l_2_boundary_cli
                        yield '   '
                        yield str((undefined(name='boundary_cli') if l_2_boundary_cli is missing else l_2_boundary_cli))
                        yield '\n'
                    l_2_boundary = l_2_boundary_cli = missing
                if t_11(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'multicast'), 'ipv6'), 'boundaries')):
                    pass
                    for l_2_boundary in environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'multicast'), 'ipv6'), 'boundaries'):
                        _loop_vars = {}
                        pass
                        yield '   multicast ipv6 boundary '
                        yield str(environment.getattr(l_2_boundary, 'boundary'))
                        yield ' out\n'
                    l_2_boundary = missing
                if t_11(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'multicast'), 'ipv4'), 'static'), True):
                    pass
                    yield '   multicast ipv4 static\n'
                if t_11(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'multicast'), 'ipv6'), 'static'), True):
                    pass
                    yield '   multicast ipv6 static\n'
            if t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'mpls'), 'ip'), True):
                pass
                yield '   mpls ip\n'
            elif t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'mpls'), 'ip'), False):
                pass
                yield '   no mpls ip\n'
            if t_11(environment.getattr(l_1_ethernet_interface, 'ospf_cost')):
                pass
                yield '   ip ospf cost '
                yield str(environment.getattr(l_1_ethernet_interface, 'ospf_cost'))
                yield '\n'
            if t_11(environment.getattr(l_1_ethernet_interface, 'ospf_network_point_to_point'), True):
                pass
                yield '   ip ospf network point-to-point\n'
            if t_11(environment.getattr(l_1_ethernet_interface, 'ospf_authentication'), 'simple'):
                pass
                yield '   ip ospf authentication\n'
            elif t_11(environment.getattr(l_1_ethernet_interface, 'ospf_authentication'), 'message-digest'):
                pass
                yield '   ip ospf authentication message-digest\n'
            if t_11(environment.getattr(l_1_ethernet_interface, 'ospf_authentication_key')):
                pass
                yield '   ip ospf authentication-key 7 '
                yield str(environment.getattr(l_1_ethernet_interface, 'ospf_authentication_key'))
                yield '\n'
            if t_11(environment.getattr(l_1_ethernet_interface, 'ospf_area')):
                pass
                yield '   ip ospf area '
                yield str(environment.getattr(l_1_ethernet_interface, 'ospf_area'))
                yield '\n'
            for l_2_ospf_message_digest_key in t_3(environment.getattr(l_1_ethernet_interface, 'ospf_message_digest_keys'), 'id'):
                _loop_vars = {}
                pass
                if (t_11(environment.getattr(l_2_ospf_message_digest_key, 'hash_algorithm')) and t_11(environment.getattr(l_2_ospf_message_digest_key, 'key'))):
                    pass
                    yield '   ip ospf message-digest-key '
                    yield str(environment.getattr(l_2_ospf_message_digest_key, 'id'))
                    yield ' '
                    yield str(environment.getattr(l_2_ospf_message_digest_key, 'hash_algorithm'))
                    yield ' 7 '
                    yield str(environment.getattr(l_2_ospf_message_digest_key, 'key'))
                    yield '\n'
            l_2_ospf_message_digest_key = missing
            if t_11(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'pim'), 'ipv4'), 'sparse_mode'), True):
                pass
                yield '   pim ipv4 sparse-mode\n'
            if t_11(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'pim'), 'ipv4'), 'dr_priority')):
                pass
                yield '   pim ipv4 dr-priority '
                yield str(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'pim'), 'ipv4'), 'dr_priority'))
                yield '\n'
            if t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'poe'), 'priority')):
                pass
                yield '   poe priority '
                yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'poe'), 'priority'))
                yield '\n'
            if t_11(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'poe'), 'reboot'), 'action')):
                pass
                yield '   poe reboot action '
                yield str(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'poe'), 'reboot'), 'action'))
                yield '\n'
            if t_11(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'poe'), 'link_down'), 'action')):
                pass
                l_1_poe_link_down_action_cli = str_join(('poe link down action ', environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'poe'), 'link_down'), 'action'), ))
                _loop_vars['poe_link_down_action_cli'] = l_1_poe_link_down_action_cli
                if t_11(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'poe'), 'link_down'), 'power_off_delay')):
                    pass
                    l_1_poe_link_down_action_cli = str_join(((undefined(name='poe_link_down_action_cli') if l_1_poe_link_down_action_cli is missing else l_1_poe_link_down_action_cli), ' ', environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'poe'), 'link_down'), 'power_off_delay'), ))
                    _loop_vars['poe_link_down_action_cli'] = l_1_poe_link_down_action_cli
                yield '   '
                yield str((undefined(name='poe_link_down_action_cli') if l_1_poe_link_down_action_cli is missing else l_1_poe_link_down_action_cli))
                yield '\n'
            if t_11(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'poe'), 'shutdown'), 'action')):
                pass
                yield '   poe shutdown action '
                yield str(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'poe'), 'shutdown'), 'action'))
                yield '\n'
            if t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'poe'), 'disabled'), True):
                pass
                yield '   poe disabled\n'
            if t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'poe'), 'limit')):
                pass
                if t_11(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'poe'), 'limit'), 'class')):
                    pass
                    l_1_poe_limit_cli = str_join(('poe limit ', environment.getitem((undefined(name='POE_CLASS_MAP') if l_0_POE_CLASS_MAP is missing else l_0_POE_CLASS_MAP), environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'poe'), 'limit'), 'class')), ' watts', ))
                    _loop_vars['poe_limit_cli'] = l_1_poe_limit_cli
                elif t_11(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'poe'), 'limit'), 'watts')):
                    pass
                    l_1_poe_limit_cli = str_join(('poe limit ', t_5('%.2f', t_4(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'poe'), 'limit'), 'watts'))), ' watts', ))
                    _loop_vars['poe_limit_cli'] = l_1_poe_limit_cli
                if (t_11((undefined(name='poe_limit_cli') if l_1_poe_limit_cli is missing else l_1_poe_limit_cli)) and t_11(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'poe'), 'limit'), 'fixed'), True)):
                    pass
                    l_1_poe_limit_cli = str_join(((undefined(name='poe_limit_cli') if l_1_poe_limit_cli is missing else l_1_poe_limit_cli), ' fixed', ))
                    _loop_vars['poe_limit_cli'] = l_1_poe_limit_cli
                yield '   '
                yield str((undefined(name='poe_limit_cli') if l_1_poe_limit_cli is missing else l_1_poe_limit_cli))
                yield '\n'
            if t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'poe'), 'negotiation_lldp'), False):
                pass
                yield '   poe negotiation lldp disabled\n'
            if t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'poe'), 'legacy_detect'), True):
                pass
                yield '   poe legacy detect\n'
            if t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'qos'), 'trust')):
                pass
                if (environment.getattr(environment.getattr(l_1_ethernet_interface, 'qos'), 'trust') == 'disabled'):
                    pass
                    yield '   no qos trust\n'
                else:
                    pass
                    yield '   qos trust '
                    yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'qos'), 'trust'))
                    yield '\n'
            if t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'qos'), 'cos')):
                pass
                yield '   qos cos '
                yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'qos'), 'cos'))
                yield '\n'
            if t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'qos'), 'dscp')):
                pass
                yield '   qos dscp '
                yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'qos'), 'dscp'))
                yield '\n'
            if t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'shape'), 'rate')):
                pass
                yield '   shape rate '
                yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'shape'), 'rate'))
                yield '\n'
            if t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'priority_flow_control'), 'enabled'), True):
                pass
                yield '   priority-flow-control on\n'
            elif t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'priority_flow_control'), 'enabled'), False):
                pass
                yield '   no priority-flow-control\n'
            for l_2_priority_block in t_3(environment.getattr(environment.getattr(l_1_ethernet_interface, 'priority_flow_control'), 'priorities')):
                _loop_vars = {}
                pass
                if t_11(environment.getattr(l_2_priority_block, 'priority')):
                    pass
                    if t_11(environment.getattr(l_2_priority_block, 'no_drop'), True):
                        pass
                        yield '   priority-flow-control priority '
                        yield str(environment.getattr(l_2_priority_block, 'priority'))
                        yield ' no-drop\n'
                    elif t_11(environment.getattr(l_2_priority_block, 'no_drop'), False):
                        pass
                        yield '   priority-flow-control priority '
                        yield str(environment.getattr(l_2_priority_block, 'priority'))
                        yield ' drop\n'
            l_2_priority_block = missing
            for l_2_section in t_3(environment.getattr(l_1_ethernet_interface, 'storm_control')):
                _loop_vars = {}
                pass
                if t_11(environment.getattr(environment.getitem(environment.getattr(l_1_ethernet_interface, 'storm_control'), l_2_section), 'level')):
                    pass
                    if t_11(environment.getattr(environment.getitem(environment.getattr(l_1_ethernet_interface, 'storm_control'), l_2_section), 'unit'), 'pps'):
                        pass
                        yield '   storm-control '
                        yield str(t_9(context.eval_ctx, l_2_section, '_', '-'))
                        yield ' level pps '
                        yield str(environment.getattr(environment.getitem(environment.getattr(l_1_ethernet_interface, 'storm_control'), l_2_section), 'level'))
                        yield '\n'
                    else:
                        pass
                        yield '   storm-control '
                        yield str(t_9(context.eval_ctx, l_2_section, '_', '-'))
                        yield ' level '
                        yield str(environment.getattr(environment.getitem(environment.getattr(l_1_ethernet_interface, 'storm_control'), l_2_section), 'level'))
                        yield '\n'
            l_2_section = missing
            if t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'ptp'), 'enable'), True):
                pass
                yield '   ptp enable\n'
            if t_11(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'ptp'), 'sync_message'), 'interval')):
                pass
                yield '   ptp sync-message interval '
                yield str(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'ptp'), 'sync_message'), 'interval'))
                yield '\n'
            if t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'ptp'), 'delay_mechanism')):
                pass
                yield '   ptp delay-mechanism '
                yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'ptp'), 'delay_mechanism'))
                yield '\n'
            if t_11(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'ptp'), 'announce'), 'interval')):
                pass
                yield '   ptp announce interval '
                yield str(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'ptp'), 'announce'), 'interval'))
                yield '\n'
            if t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'ptp'), 'transport')):
                pass
                yield '   ptp transport '
                yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'ptp'), 'transport'))
                yield '\n'
            if t_11(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'ptp'), 'announce'), 'timeout')):
                pass
                yield '   ptp announce timeout '
                yield str(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'ptp'), 'announce'), 'timeout'))
                yield '\n'
            if t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'ptp'), 'delay_req')):
                pass
                yield '   ptp delay-req interval '
                yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'ptp'), 'delay_req'))
                yield '\n'
            if t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'ptp'), 'role')):
                pass
                yield '   ptp role '
                yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'ptp'), 'role'))
                yield '\n'
            if t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'ptp'), 'vlan')):
                pass
                yield '   ptp vlan '
                yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'ptp'), 'vlan'))
                yield '\n'
            if t_11(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'service_policy'), 'pbr'), 'input')):
                pass
                yield '   service-policy type pbr input '
                yield str(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'service_policy'), 'pbr'), 'input'))
                yield '\n'
            if t_11(environment.getattr(l_1_ethernet_interface, 'service_profile')):
                pass
                yield '   service-profile '
                yield str(environment.getattr(l_1_ethernet_interface, 'service_profile'))
                yield '\n'
            if t_11(environment.getattr(l_1_ethernet_interface, 'isis_enable')):
                pass
                yield '   isis enable '
                yield str(environment.getattr(l_1_ethernet_interface, 'isis_enable'))
                yield '\n'
            if t_11(environment.getattr(l_1_ethernet_interface, 'isis_circuit_type')):
                pass
                yield '   isis circuit-type '
                yield str(environment.getattr(l_1_ethernet_interface, 'isis_circuit_type'))
                yield '\n'
            if t_11(environment.getattr(l_1_ethernet_interface, 'isis_metric')):
                pass
                yield '   isis metric '
                yield str(environment.getattr(l_1_ethernet_interface, 'isis_metric'))
                yield '\n'
            if t_11(environment.getattr(l_1_ethernet_interface, 'isis_passive'), True):
                pass
                yield '   isis passive\n'
            if t_11(environment.getattr(l_1_ethernet_interface, 'isis_hello_padding'), False):
                pass
                yield '   no isis hello padding\n'
            elif t_11(environment.getattr(l_1_ethernet_interface, 'isis_hello_padding'), True):
                pass
                yield '   isis hello padding\n'
            if t_11(environment.getattr(l_1_ethernet_interface, 'isis_network_point_to_point'), True):
                pass
                yield '   isis network point-to-point\n'
            if (t_11(environment.getattr(l_1_ethernet_interface, 'isis_authentication_mode')) and (environment.getattr(l_1_ethernet_interface, 'isis_authentication_mode') in ['text', 'md5'])):
                pass
                yield '   isis authentication mode '
                yield str(environment.getattr(l_1_ethernet_interface, 'isis_authentication_mode'))
                yield '\n'
            if t_11(environment.getattr(l_1_ethernet_interface, 'isis_authentication_key')):
                pass
                yield '   isis authentication key 7 '
                yield str(environment.getattr(l_1_ethernet_interface, 'isis_authentication_key'))
                yield '\n'
            if t_11(environment.getattr(l_1_ethernet_interface, 'spanning_tree_portfast'), 'edge'):
                pass
                yield '   spanning-tree portfast\n'
            elif t_11(environment.getattr(l_1_ethernet_interface, 'spanning_tree_portfast'), 'network'):
                pass
                yield '   spanning-tree portfast network\n'
            if (t_11(environment.getattr(l_1_ethernet_interface, 'spanning_tree_bpduguard')) and (environment.getattr(l_1_ethernet_interface, 'spanning_tree_bpduguard') in [True, 'True', 'enabled'])):
                pass
                yield '   spanning-tree bpduguard enable\n'
            elif t_11(environment.getattr(l_1_ethernet_interface, 'spanning_tree_bpduguard'), 'disabled'):
                pass
                yield '   spanning-tree bpduguard disable\n'
            if (t_11(environment.getattr(l_1_ethernet_interface, 'spanning_tree_bpdufilter')) and (environment.getattr(l_1_ethernet_interface, 'spanning_tree_bpdufilter') in [True, 'True', 'enabled'])):
                pass
                yield '   spanning-tree bpdufilter enable\n'
            elif t_11(environment.getattr(l_1_ethernet_interface, 'spanning_tree_bpdufilter'), 'disabled'):
                pass
                yield '   spanning-tree bpdufilter disable\n'
            if t_11(environment.getattr(l_1_ethernet_interface, 'spanning_tree_guard')):
                pass
                if (environment.getattr(l_1_ethernet_interface, 'spanning_tree_guard') == 'disabled'):
                    pass
                    yield '   spanning-tree guard none\n'
                else:
                    pass
                    yield '   spanning-tree guard '
                    yield str(environment.getattr(l_1_ethernet_interface, 'spanning_tree_guard'))
                    yield '\n'
            if t_11(environment.getattr(l_1_ethernet_interface, 'sflow')):
                pass
                if t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'sflow'), 'enable'), True):
                    pass
                    yield '   sflow enable\n'
                elif t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'sflow'), 'enable'), False):
                    pass
                    yield '   no sflow enable\n'
                if t_11(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'sflow'), 'egress'), 'enable'), True):
                    pass
                    yield '   sflow egress enable\n'
                elif t_11(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'sflow'), 'egress'), 'enable'), False):
                    pass
                    yield '   no sflow egress enable\n'
                if t_11(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'sflow'), 'egress'), 'unmodified_enable'), True):
                    pass
                    yield '   sflow egress unmodified enable\n'
                elif t_11(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'sflow'), 'egress'), 'unmodified_enable'), False):
                    pass
                    yield '   no sflow egress unmodified enable\n'
            if t_11(environment.getattr(l_1_ethernet_interface, 'vmtracer'), True):
                pass
                yield '   vmtracer vmware-esx\n'
        if t_11(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'transceiver'), 'media'), 'override')):
            pass
            yield '   transceiver media override '
            yield str(environment.getattr(environment.getattr(environment.getattr(l_1_ethernet_interface, 'transceiver'), 'media'), 'override'))
            yield '\n'
        for l_2_link_tracking_group in t_3(environment.getattr(l_1_ethernet_interface, 'link_tracking_groups')):
            _loop_vars = {}
            pass
            if (t_11(environment.getattr(l_2_link_tracking_group, 'name')) and t_11(environment.getattr(l_2_link_tracking_group, 'direction'))):
                pass
                yield '   link tracking group '
                yield str(environment.getattr(l_2_link_tracking_group, 'name'))
                yield ' '
                yield str(environment.getattr(l_2_link_tracking_group, 'direction'))
                yield '\n'
        l_2_link_tracking_group = missing
        if t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'traffic_policy'), 'input')):
            pass
            yield '   traffic-policy input '
            yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'traffic_policy'), 'input'))
            yield '\n'
        if t_11(environment.getattr(environment.getattr(l_1_ethernet_interface, 'traffic_policy'), 'output')):
            pass
            yield '   traffic-policy output '
            yield str(environment.getattr(environment.getattr(l_1_ethernet_interface, 'traffic_policy'), 'output'))
            yield '\n'
        if t_11(environment.getattr(l_1_ethernet_interface, 'eos_cli')):
            pass
            yield '   '
            yield str(t_6(environment.getattr(l_1_ethernet_interface, 'eos_cli'), 3, False))
            yield '\n'
    l_1_ethernet_interface = l_1_port_channel_interface_name = l_1_port_channel_interfaces = l_1_print_ethernet = l_1_encapsulation_cli = l_1_dfe_algo_cli = l_1_dfe_hold_time_cli = l_1_host_mode_cli = l_1_auth_cli = l_1_auth_failure_fallback_mba = l_1_address_locking_cli = l_1_poe_link_down_action_cli = l_1_poe_limit_cli = missing

blocks = {}
debug_info = '2=79&3=82&4=97&5=99&6=101&11=103&14=107&17=110&18=112&19=114&20=117&23=119&24=122&26=124&28=127&31=130&32=133&34=135&35=137&36=140&39=142&40=144&42=147&45=150&47=153&51=156&52=158&53=161&56=163&57=166&59=168&60=170&61=173&64=175&65=178&67=180&68=183&70=185&73=190&75=193&78=196&80=199&84=202&85=204&86=206&87=209&90=211&91=213&93=216&94=219&97=221&98=224&100=226&101=229&103=231&104=235&105=237&106=239&107=241&109=243&110=245&111=248&114=251&115=253&116=256&119=258&120=261&122=263&123=267&125=270&127=273&128=275&130=278&132=280&133=283&134=285&135=287&136=289&137=291&138=293&139=295&141=297&142=299&143=301&144=303&145=305&146=307&148=309&149=311&151=313&153=316&158=321&160=324&163=327&164=330&166=332&167=335&169=337&170=340&172=342&173=345&175=347&177=350&178=353&180=355&181=358&183=360&184=362&186=365&187=367&188=369&189=371&191=374&193=376&194=378&195=380&196=382&198=385&200=387&202=390&206=393&207=396&209=398&210=401&212=403&213=406&216=408&217=410&218=413&220=415&221=417&223=420&224=422&228=425&231=428&232=431&234=433&236=436&239=439&240=441&242=444&243=446&244=448&245=450&247=453&250=455&251=457&253=460&257=465&258=467&259=469&261=472&264=474&265=476&266=479&268=481&271=484&272=487&274=489&275=492&277=494&278=497&281=499&282=502&284=504&285=506&287=509&288=511&289=513&290=515&292=518&296=520&298=523&301=526&302=528&303=530&304=532&306=534&307=536&309=539&311=541&312=544&314=546&317=549&318=552&319=554&320=556&321=560&324=563&325=567&326=569&327=571&329=573&330=575&332=578&335=581&338=584&340=590&342=593&345=596&348=599&349=602&351=604&352=607&354=609&357=612&360=615&361=617&362=621&363=623&364=625&365=627&366=629&369=631&370=633&372=636&376=639&377=643&378=645&379=647&381=649&382=651&383=653&384=655&386=657&387=659&389=662&391=665&392=668&393=672&394=675&396=677&397=680&399=682&400=685&403=687&406=690&409=693&410=696&412=698&413=700&416=703&418=706&421=709&422=712&424=714&425=717&427=719&428=722&430=724&431=727&433=729&434=732&436=734&437=737&439=739&440=741&441=743&442=747&443=749&444=751&446=754&449=757&450=759&451=763&454=766&457=769&461=772&463=775&466=778&467=781&469=783&472=786&474=789&477=792&478=795&480=797&481=800&483=802&484=805&485=808&488=815&491=818&492=821&494=823&495=826&497=828&498=831&500=833&501=835&502=837&503=839&505=842&507=844&508=847&510=849&513=852&514=854&515=856&516=858&517=860&519=862&520=864&522=867&524=869&527=872&530=875&531=877&534=883&537=885&538=888&540=890&541=893&543=895&544=898&546=900&548=903&551=906&552=909&553=911&554=914&555=916&556=919&560=922&561=925&562=927&563=930&565=937&569=942&572=945&573=948&575=950&576=953&578=955&579=958&581=960&582=963&584=965&585=968&587=970&588=973&590=975&591=978&593=980&594=983&596=985&597=988&599=990&600=993&602=995&603=998&605=1000&606=1003&608=1005&609=1008&611=1010&614=1013&616=1016&619=1019&622=1022&624=1025&626=1027&627=1030&629=1032&631=1035&634=1038&636=1041&639=1044&641=1047&644=1050&645=1052&648=1058&651=1060&652=1062&654=1065&657=1068&659=1071&662=1074&664=1077&668=1080&672=1083&673=1086&675=1088&676=1091&677=1094&680=1099&681=1102&683=1104&684=1107&686=1109&687=1112'