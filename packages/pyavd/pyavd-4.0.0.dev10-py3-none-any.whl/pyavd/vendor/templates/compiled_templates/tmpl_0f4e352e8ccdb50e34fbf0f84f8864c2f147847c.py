from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/vlan-interfaces.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_vlan_interfaces = resolve('vlan_interfaces')
    l_0_namespace = resolve('namespace')
    l_0_vlan_interface_pvlan = resolve('vlan_interface_pvlan')
    l_0_vlan_interfaces_ipv6 = resolve('vlan_interfaces_ipv6')
    l_0_vlan_interfaces_vrrp_details = resolve('vlan_interfaces_vrrp_details')
    l_0_vlan_interface_isis = resolve('vlan_interface_isis')
    l_0_multicast_interfaces = resolve('multicast_interfaces')
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
        t_3 = environment.filters['join']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No filter named 'join' found.")
    try:
        t_4 = environment.filters['length']
    except KeyError:
        @internalcode
        def t_4(*unused):
            raise TemplateRuntimeError("No filter named 'length' found.")
    try:
        t_5 = environment.filters['map']
    except KeyError:
        @internalcode
        def t_5(*unused):
            raise TemplateRuntimeError("No filter named 'map' found.")
    try:
        t_6 = environment.filters['selectattr']
    except KeyError:
        @internalcode
        def t_6(*unused):
            raise TemplateRuntimeError("No filter named 'selectattr' found.")
    try:
        t_7 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_7(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    try:
        t_8 = environment.tests['defined']
    except KeyError:
        @internalcode
        def t_8(*unused):
            raise TemplateRuntimeError("No test named 'defined' found.")
    pass
    if t_7((undefined(name='vlan_interfaces') if l_0_vlan_interfaces is missing else l_0_vlan_interfaces)):
        pass
        yield '\n### VLAN Interfaces\n\n#### VLAN Interfaces Summary\n\n| Interface | Description | VRF |  MTU | Shutdown |\n| --------- | ----------- | --- | ---- | -------- |\n'
        for l_1_vlan_interface in t_2((undefined(name='vlan_interfaces') if l_0_vlan_interfaces is missing else l_0_vlan_interfaces), 'name'):
            l_1_description = l_1_vrf = l_1_mtu = l_1_shutdown = missing
            _loop_vars = {}
            pass
            l_1_description = t_1(environment.getattr(l_1_vlan_interface, 'description'), '-')
            _loop_vars['description'] = l_1_description
            l_1_vrf = t_1(environment.getattr(l_1_vlan_interface, 'vrf'), 'default')
            _loop_vars['vrf'] = l_1_vrf
            l_1_mtu = t_1(environment.getattr(l_1_vlan_interface, 'mtu'), '-')
            _loop_vars['mtu'] = l_1_mtu
            l_1_shutdown = t_1(environment.getattr(l_1_vlan_interface, 'shutdown'), '-')
            _loop_vars['shutdown'] = l_1_shutdown
            yield '| '
            yield str(environment.getattr(l_1_vlan_interface, 'name'))
            yield ' | '
            yield str((undefined(name='description') if l_1_description is missing else l_1_description))
            yield ' | '
            yield str((undefined(name='vrf') if l_1_vrf is missing else l_1_vrf))
            yield ' | '
            yield str((undefined(name='mtu') if l_1_mtu is missing else l_1_mtu))
            yield ' | '
            yield str((undefined(name='shutdown') if l_1_shutdown is missing else l_1_shutdown))
            yield ' |\n'
        l_1_vlan_interface = l_1_description = l_1_vrf = l_1_mtu = l_1_shutdown = missing
        l_0_vlan_interface_pvlan = context.call((undefined(name='namespace') if l_0_namespace is missing else l_0_namespace))
        context.vars['vlan_interface_pvlan'] = l_0_vlan_interface_pvlan
        context.exported_vars.add('vlan_interface_pvlan')
        if not isinstance(l_0_vlan_interface_pvlan, Namespace):
            raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
        l_0_vlan_interface_pvlan['configured'] = False
        for l_1_vlan_interface in t_2((undefined(name='vlan_interfaces') if l_0_vlan_interfaces is missing else l_0_vlan_interfaces), 'name'):
            _loop_vars = {}
            pass
            if t_7(environment.getattr(l_1_vlan_interface, 'pvlan_mapping')):
                pass
                if not isinstance(l_0_vlan_interface_pvlan, Namespace):
                    raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                l_0_vlan_interface_pvlan['configured'] = True
                break
        l_1_vlan_interface = missing
        if (environment.getattr((undefined(name='vlan_interface_pvlan') if l_0_vlan_interface_pvlan is missing else l_0_vlan_interface_pvlan), 'configured') == True):
            pass
            yield '\n##### Private VLAN\n\n| Interface | PVLAN Mapping |\n| --------- | ------------- |\n'
            for l_1_vlan_interface in t_2((undefined(name='vlan_interfaces') if l_0_vlan_interfaces is missing else l_0_vlan_interfaces), 'name'):
                _loop_vars = {}
                pass
                if t_7(environment.getattr(l_1_vlan_interface, 'pvlan_mapping')):
                    pass
                    yield '| '
                    yield str(environment.getattr(l_1_vlan_interface, 'name'))
                    yield ' | '
                    yield str(environment.getattr(l_1_vlan_interface, 'pvlan_mapping'))
                    yield ' |\n'
            l_1_vlan_interface = missing
        yield '\n##### IPv4\n\n| Interface | VRF | IP Address | IP Address Virtual | IP Router Virtual Address | VRRP | ACL In | ACL Out |\n| --------- | --- | ---------- | ------------------ | ------------------------- | ---- | ------ | ------- |\n'
        for l_1_vlan_interface in t_2((undefined(name='vlan_interfaces') if l_0_vlan_interfaces is missing else l_0_vlan_interfaces), 'name'):
            l_1_row_vrf = l_1_row_ip_addr = l_1_row_ip_vaddr = l_1_row_varp = l_1_row_vrrp = l_1_row_acl_in = l_1_row_acl_out = missing
            _loop_vars = {}
            pass
            l_1_row_vrf = t_1(environment.getattr(l_1_vlan_interface, 'vrf'), 'default')
            _loop_vars['row_vrf'] = l_1_row_vrf
            l_1_row_ip_addr = t_1(environment.getattr(l_1_vlan_interface, 'ip_address'), '-')
            _loop_vars['row_ip_addr'] = l_1_row_ip_addr
            l_1_row_ip_vaddr = t_1(environment.getattr(l_1_vlan_interface, 'ip_address_virtual'), '-')
            _loop_vars['row_ip_vaddr'] = l_1_row_ip_vaddr
            l_1_row_varp = t_3(context.eval_ctx, t_1(environment.getattr(l_1_vlan_interface, 'ip_virtual_router_addresses'), '-'), ', ')
            _loop_vars['row_varp'] = l_1_row_varp
            l_1_row_vrrp = t_1(environment.getattr(environment.getattr(l_1_vlan_interface, 'vrrp'), 'ipv4'), '-')
            _loop_vars['row_vrrp'] = l_1_row_vrrp
            l_1_row_acl_in = t_1(environment.getattr(l_1_vlan_interface, 'access_group_in'), '-')
            _loop_vars['row_acl_in'] = l_1_row_acl_in
            l_1_row_acl_out = t_1(environment.getattr(l_1_vlan_interface, 'access_group_out'), '-')
            _loop_vars['row_acl_out'] = l_1_row_acl_out
            yield '| '
            yield str(environment.getattr(l_1_vlan_interface, 'name'))
            yield ' |  '
            yield str((undefined(name='row_vrf') if l_1_row_vrf is missing else l_1_row_vrf))
            yield '  |  '
            yield str((undefined(name='row_ip_addr') if l_1_row_ip_addr is missing else l_1_row_ip_addr))
            yield '  |  '
            yield str((undefined(name='row_ip_vaddr') if l_1_row_ip_vaddr is missing else l_1_row_ip_vaddr))
            yield '  |  '
            yield str((undefined(name='row_varp') if l_1_row_varp is missing else l_1_row_varp))
            yield '  |  '
            yield str((undefined(name='row_vrrp') if l_1_row_vrrp is missing else l_1_row_vrrp))
            yield '  |  '
            yield str((undefined(name='row_acl_in') if l_1_row_acl_in is missing else l_1_row_acl_in))
            yield '  |  '
            yield str((undefined(name='row_acl_out') if l_1_row_acl_out is missing else l_1_row_acl_out))
            yield '  |\n'
        l_1_vlan_interface = l_1_row_vrf = l_1_row_ip_addr = l_1_row_ip_vaddr = l_1_row_varp = l_1_row_vrrp = l_1_row_acl_in = l_1_row_acl_out = missing
        l_0_vlan_interfaces_ipv6 = []
        context.vars['vlan_interfaces_ipv6'] = l_0_vlan_interfaces_ipv6
        context.exported_vars.add('vlan_interfaces_ipv6')
        for l_1_vlan_interface in t_1((undefined(name='vlan_interfaces') if l_0_vlan_interfaces is missing else l_0_vlan_interfaces), []):
            _loop_vars = {}
            pass
            if ((t_7(environment.getattr(l_1_vlan_interface, 'ipv6_address')) or t_7(environment.getattr(l_1_vlan_interface, 'ipv6_address_virtual'))) or t_7(environment.getattr(l_1_vlan_interface, 'ipv6_address_virtuals'))):
                pass
                context.call(environment.getattr((undefined(name='vlan_interfaces_ipv6') if l_0_vlan_interfaces_ipv6 is missing else l_0_vlan_interfaces_ipv6), 'append'), l_1_vlan_interface, _loop_vars=_loop_vars)
        l_1_vlan_interface = missing
        if (t_4((undefined(name='vlan_interfaces_ipv6') if l_0_vlan_interfaces_ipv6 is missing else l_0_vlan_interfaces_ipv6)) > 0):
            pass
            yield '\n##### IPv6\n\n| Interface | VRF | IPv6 Address | IPv6 Virtual Addresses | Virtual Router Address | VRRP | ND RA Disabled | Managed Config Flag | IPv6 ACL In | IPv6 ACL Out |\n| --------- | --- | ------------ | -------------------- | ---------------------- | ---- | -------------- | ------------------- | ----------- | ------------ |\n'
            for l_1_vlan_interface in t_2((undefined(name='vlan_interfaces_ipv6') if l_0_vlan_interfaces_ipv6 is missing else l_0_vlan_interfaces_ipv6), 'name'):
                l_1_row_ip_vaddr = resolve('row_ip_vaddr')
                l_1_row_varp = resolve('row_varp')
                l_1_row_vrf = l_1_row_ip_addr = l_1_row_vrrp = l_1_row_nd_ra_disabled = l_1_row_nd_man_cfg = l_1_row_acl_in = l_1_row_acl_out = missing
                _loop_vars = {}
                pass
                l_1_row_vrf = t_1(environment.getattr(l_1_vlan_interface, 'vrf'), 'default')
                _loop_vars['row_vrf'] = l_1_row_vrf
                l_1_row_ip_addr = t_1(environment.getattr(l_1_vlan_interface, 'ipv6_address'), '-')
                _loop_vars['row_ip_addr'] = l_1_row_ip_addr
                if t_7(environment.getattr(l_1_vlan_interface, 'ipv6_address_virtual')):
                    pass
                    l_1_row_ip_vaddr = t_3(context.eval_ctx, ([environment.getattr(l_1_vlan_interface, 'ipv6_address_virtual')] + t_1(environment.getattr(l_1_vlan_interface, 'ipv6_address_virtuals'), [])), ', ')
                    _loop_vars['row_ip_vaddr'] = l_1_row_ip_vaddr
                else:
                    pass
                    l_1_row_ip_vaddr = t_3(context.eval_ctx, t_1(environment.getattr(l_1_vlan_interface, 'ipv6_address_virtuals'), '-'), ', ')
                    _loop_vars['row_ip_vaddr'] = l_1_row_ip_vaddr
                if t_7(environment.getattr(l_1_vlan_interface, 'ipv6_virtual_router_addresses')):
                    pass
                    l_1_row_varp = t_3(context.eval_ctx, environment.getattr(l_1_vlan_interface, 'ipv6_virtual_router_addresses'), ', ')
                    _loop_vars['row_varp'] = l_1_row_varp
                else:
                    pass
                    l_1_row_varp = t_1(environment.getattr(l_1_vlan_interface, 'ipv6_virtual_router_address'), '-')
                    _loop_vars['row_varp'] = l_1_row_varp
                l_1_row_vrrp = t_1(environment.getattr(environment.getattr(l_1_vlan_interface, 'vrrp'), 'ipv6'), '-')
                _loop_vars['row_vrrp'] = l_1_row_vrrp
                l_1_row_nd_ra_disabled = t_1(environment.getattr(l_1_vlan_interface, 'ipv6_nd_ra_disabled'), '-')
                _loop_vars['row_nd_ra_disabled'] = l_1_row_nd_ra_disabled
                l_1_row_nd_man_cfg = t_1(environment.getattr(l_1_vlan_interface, 'ipv6_nd_managed_config_flag'), '-')
                _loop_vars['row_nd_man_cfg'] = l_1_row_nd_man_cfg
                l_1_row_acl_in = t_1(environment.getattr(l_1_vlan_interface, 'ipv6_access_group_in'), '-')
                _loop_vars['row_acl_in'] = l_1_row_acl_in
                l_1_row_acl_out = t_1(environment.getattr(l_1_vlan_interface, 'ipv6_access_group_out'), '-')
                _loop_vars['row_acl_out'] = l_1_row_acl_out
                yield '| '
                yield str(environment.getattr(l_1_vlan_interface, 'name'))
                yield ' | '
                yield str((undefined(name='row_vrf') if l_1_row_vrf is missing else l_1_row_vrf))
                yield ' | '
                yield str((undefined(name='row_ip_addr') if l_1_row_ip_addr is missing else l_1_row_ip_addr))
                yield ' | '
                yield str((undefined(name='row_ip_vaddr') if l_1_row_ip_vaddr is missing else l_1_row_ip_vaddr))
                yield ' | '
                yield str((undefined(name='row_varp') if l_1_row_varp is missing else l_1_row_varp))
                yield ' | '
                yield str((undefined(name='row_vrrp') if l_1_row_vrrp is missing else l_1_row_vrrp))
                yield ' | '
                yield str((undefined(name='row_nd_ra_disabled') if l_1_row_nd_ra_disabled is missing else l_1_row_nd_ra_disabled))
                yield ' | '
                yield str((undefined(name='row_nd_man_cfg') if l_1_row_nd_man_cfg is missing else l_1_row_nd_man_cfg))
                yield ' | '
                yield str((undefined(name='row_acl_in') if l_1_row_acl_in is missing else l_1_row_acl_in))
                yield ' | '
                yield str((undefined(name='row_acl_out') if l_1_row_acl_out is missing else l_1_row_acl_out))
                yield ' |\n'
            l_1_vlan_interface = l_1_row_vrf = l_1_row_ip_addr = l_1_row_ip_vaddr = l_1_row_varp = l_1_row_vrrp = l_1_row_nd_ra_disabled = l_1_row_nd_man_cfg = l_1_row_acl_in = l_1_row_acl_out = missing
        l_0_vlan_interfaces_vrrp_details = []
        context.vars['vlan_interfaces_vrrp_details'] = l_0_vlan_interfaces_vrrp_details
        context.exported_vars.add('vlan_interfaces_vrrp_details')
        for l_1_vlan_interface in t_1((undefined(name='vlan_interfaces') if l_0_vlan_interfaces is missing else l_0_vlan_interfaces), []):
            _loop_vars = {}
            pass
            if t_7(environment.getattr(l_1_vlan_interface, 'vrrp_ids')):
                pass
                context.call(environment.getattr((undefined(name='vlan_interfaces_vrrp_details') if l_0_vlan_interfaces_vrrp_details is missing else l_0_vlan_interfaces_vrrp_details), 'append'), l_1_vlan_interface, _loop_vars=_loop_vars)
        l_1_vlan_interface = missing
        if (t_4((undefined(name='vlan_interfaces_vrrp_details') if l_0_vlan_interfaces_vrrp_details is missing else l_0_vlan_interfaces_vrrp_details)) > 0):
            pass
            yield '\n##### VRRP Details\n\n| Interface | VRRP-ID | Priority | Advertisement Interval | Preempt | Tracked Object Name(s) | Tracked Object Action(s) | IPv4 Virtual IP | IPv4 VRRP Version | IPv6 Virtual IP |\n| --------- | ------- | -------- | ---------------------- | --------| ---------------------- | ------------------------ | --------------- | ----------------- | --------------- |\n'
            for l_1_vlan_interface in t_2((undefined(name='vlan_interfaces_vrrp_details') if l_0_vlan_interfaces_vrrp_details is missing else l_0_vlan_interfaces_vrrp_details), 'name'):
                _loop_vars = {}
                pass
                def t_9(fiter):
                    for l_2_vrid in fiter:
                        if t_7(environment.getattr(l_2_vrid, 'id')):
                            yield l_2_vrid
                for l_2_vrid in t_9(environment.getattr(l_1_vlan_interface, 'vrrp_ids')):
                    l_2_row_tracked_object_name = resolve('row_tracked_object_name')
                    l_2_row_tracked_object_action = resolve('row_tracked_object_action')
                    l_2_row_id = l_2_row_prio_level = l_2_row_ad_interval = l_2_row_preempt = l_2_row_ipv4_virt = l_2_row_ipv4_vers = l_2_row_ipv6_virt = missing
                    _loop_vars = {}
                    pass
                    l_2_row_id = environment.getattr(l_2_vrid, 'id')
                    _loop_vars['row_id'] = l_2_row_id
                    l_2_row_prio_level = t_1(environment.getattr(l_2_vrid, 'priority_level'), '-')
                    _loop_vars['row_prio_level'] = l_2_row_prio_level
                    l_2_row_ad_interval = t_1(environment.getattr(environment.getattr(l_2_vrid, 'advertisement'), 'interval'), '-')
                    _loop_vars['row_ad_interval'] = l_2_row_ad_interval
                    l_2_row_preempt = 'Enabled'
                    _loop_vars['row_preempt'] = l_2_row_preempt
                    if t_7(environment.getattr(environment.getattr(l_2_vrid, 'preempt'), 'enabled'), False):
                        pass
                        l_2_row_preempt = 'Disabled'
                        _loop_vars['row_preempt'] = l_2_row_preempt
                    if t_7(environment.getattr(l_2_vrid, 'tracked_object')):
                        pass
                        l_2_row_tracked_object_name = []
                        _loop_vars['row_tracked_object_name'] = l_2_row_tracked_object_name
                        l_2_row_tracked_object_action = []
                        _loop_vars['row_tracked_object_action'] = l_2_row_tracked_object_action
                        for l_3_tracked_obj in t_2(environment.getattr(l_2_vrid, 'tracked_object'), 'name'):
                            _loop_vars = {}
                            pass
                            context.call(environment.getattr((undefined(name='row_tracked_object_name') if l_2_row_tracked_object_name is missing else l_2_row_tracked_object_name), 'append'), environment.getattr(l_3_tracked_obj, 'name'), _loop_vars=_loop_vars)
                            if t_7(environment.getattr(l_3_tracked_obj, 'shutdown'), True):
                                pass
                                context.call(environment.getattr((undefined(name='row_tracked_object_action') if l_2_row_tracked_object_action is missing else l_2_row_tracked_object_action), 'append'), 'Shutdown', _loop_vars=_loop_vars)
                            elif t_7(environment.getattr(l_3_tracked_obj, 'decrement')):
                                pass
                                context.call(environment.getattr((undefined(name='row_tracked_object_action') if l_2_row_tracked_object_action is missing else l_2_row_tracked_object_action), 'append'), str_join(('Decrement ', environment.getattr(l_3_tracked_obj, 'decrement'), )), _loop_vars=_loop_vars)
                        l_3_tracked_obj = missing
                        l_2_row_tracked_object_name = t_3(context.eval_ctx, (undefined(name='row_tracked_object_name') if l_2_row_tracked_object_name is missing else l_2_row_tracked_object_name), ', ')
                        _loop_vars['row_tracked_object_name'] = l_2_row_tracked_object_name
                        l_2_row_tracked_object_action = t_3(context.eval_ctx, (undefined(name='row_tracked_object_action') if l_2_row_tracked_object_action is missing else l_2_row_tracked_object_action), ', ')
                        _loop_vars['row_tracked_object_action'] = l_2_row_tracked_object_action
                    l_2_row_ipv4_virt = t_1(environment.getattr(environment.getattr(l_2_vrid, 'ipv4'), 'address'), '-')
                    _loop_vars['row_ipv4_virt'] = l_2_row_ipv4_virt
                    l_2_row_ipv4_vers = t_1(environment.getattr(environment.getattr(l_2_vrid, 'ipv4'), 'version'), '2')
                    _loop_vars['row_ipv4_vers'] = l_2_row_ipv4_vers
                    l_2_row_ipv6_virt = t_1(environment.getattr(environment.getattr(l_2_vrid, 'ipv6'), 'address'), '-')
                    _loop_vars['row_ipv6_virt'] = l_2_row_ipv6_virt
                    yield '| '
                    yield str(environment.getattr(l_1_vlan_interface, 'name'))
                    yield ' | '
                    yield str((undefined(name='row_id') if l_2_row_id is missing else l_2_row_id))
                    yield ' | '
                    yield str((undefined(name='row_prio_level') if l_2_row_prio_level is missing else l_2_row_prio_level))
                    yield ' | '
                    yield str((undefined(name='row_ad_interval') if l_2_row_ad_interval is missing else l_2_row_ad_interval))
                    yield ' | '
                    yield str((undefined(name='row_preempt') if l_2_row_preempt is missing else l_2_row_preempt))
                    yield ' | '
                    yield str(t_1((undefined(name='row_tracked_object_name') if l_2_row_tracked_object_name is missing else l_2_row_tracked_object_name), '-'))
                    yield ' | '
                    yield str(t_1((undefined(name='row_tracked_object_action') if l_2_row_tracked_object_action is missing else l_2_row_tracked_object_action), '-'))
                    yield ' | '
                    yield str((undefined(name='row_ipv4_virt') if l_2_row_ipv4_virt is missing else l_2_row_ipv4_virt))
                    yield ' | '
                    yield str((undefined(name='row_ipv4_vers') if l_2_row_ipv4_vers is missing else l_2_row_ipv4_vers))
                    yield ' | '
                    yield str((undefined(name='row_ipv6_virt') if l_2_row_ipv6_virt is missing else l_2_row_ipv6_virt))
                    yield ' |\n'
                l_2_vrid = l_2_row_id = l_2_row_prio_level = l_2_row_ad_interval = l_2_row_preempt = l_2_row_tracked_object_name = l_2_row_tracked_object_action = l_2_row_ipv4_virt = l_2_row_ipv4_vers = l_2_row_ipv6_virt = missing
            l_1_vlan_interface = missing
        l_0_vlan_interface_isis = context.call((undefined(name='namespace') if l_0_namespace is missing else l_0_namespace))
        context.vars['vlan_interface_isis'] = l_0_vlan_interface_isis
        context.exported_vars.add('vlan_interface_isis')
        if not isinstance(l_0_vlan_interface_isis, Namespace):
            raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
        l_0_vlan_interface_isis['configured'] = False
        for l_1_vlan_interface in t_2((undefined(name='vlan_interfaces') if l_0_vlan_interfaces is missing else l_0_vlan_interfaces), 'name'):
            _loop_vars = {}
            pass
            if t_8(environment.getattr(l_1_vlan_interface, 'isis_enable')):
                pass
                if not isinstance(l_0_vlan_interface_isis, Namespace):
                    raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                l_0_vlan_interface_isis['configured'] = True
                break
        l_1_vlan_interface = missing
        if (environment.getattr((undefined(name='vlan_interface_isis') if l_0_vlan_interface_isis is missing else l_0_vlan_interface_isis), 'configured') == True):
            pass
            yield '\n##### ISIS\n\n| Interface | ISIS Instance | ISIS Metric | Mode |\n| --------- | ------------- | ----------- | ---- |\n'
            for l_1_vlan_interface in t_2((undefined(name='vlan_interfaces') if l_0_vlan_interfaces is missing else l_0_vlan_interfaces), 'name'):
                l_1_isis_metric = resolve('isis_metric')
                l_1_mode = resolve('mode')
                _loop_vars = {}
                pass
                if t_7(environment.getattr(l_1_vlan_interface, 'isis_enable')):
                    pass
                    l_1_isis_metric = t_1(environment.getattr(l_1_vlan_interface, 'isis_metric'), '-')
                    _loop_vars['isis_metric'] = l_1_isis_metric
                    if t_7(environment.getattr(l_1_vlan_interface, 'isis_network_point_to_point')):
                        pass
                        l_1_mode = 'point-to-point'
                        _loop_vars['mode'] = l_1_mode
                    elif t_7(environment.getattr(l_1_vlan_interface, 'isis_passive')):
                        pass
                        l_1_mode = 'passive'
                        _loop_vars['mode'] = l_1_mode
                    else:
                        pass
                        l_1_mode = '-'
                        _loop_vars['mode'] = l_1_mode
                    yield '| '
                    yield str(environment.getattr(l_1_vlan_interface, 'name'))
                    yield ' | '
                    yield str(environment.getattr(l_1_vlan_interface, 'isis_enable'))
                    yield ' | '
                    yield str((undefined(name='isis_metric') if l_1_isis_metric is missing else l_1_isis_metric))
                    yield ' | '
                    yield str((undefined(name='mode') if l_1_mode is missing else l_1_mode))
                    yield ' |\n'
            l_1_vlan_interface = l_1_isis_metric = l_1_mode = missing
        l_0_multicast_interfaces = []
        context.vars['multicast_interfaces'] = l_0_multicast_interfaces
        context.exported_vars.add('multicast_interfaces')
        for l_1_vlan_interface in t_2((undefined(name='vlan_interfaces') if l_0_vlan_interfaces is missing else l_0_vlan_interfaces), 'name'):
            _loop_vars = {}
            pass
            if t_7(environment.getattr(l_1_vlan_interface, 'multicast')):
                pass
                context.call(environment.getattr((undefined(name='multicast_interfaces') if l_0_multicast_interfaces is missing else l_0_multicast_interfaces), 'append'), l_1_vlan_interface, _loop_vars=_loop_vars)
        l_1_vlan_interface = missing
        if (t_4((undefined(name='multicast_interfaces') if l_0_multicast_interfaces is missing else l_0_multicast_interfaces)) > 0):
            pass
            yield '\n##### Multicast Routing\n\n| Interface | IP Version | Static Routes Allowed | Multicast Boundaries | Export Host Routes For Multicast Sources |\n| --------- | ---------- | --------------------- | -------------------- | ---------------------------------------- |\n'
            for l_1_multicast_interface in (undefined(name='multicast_interfaces') if l_0_multicast_interfaces is missing else l_0_multicast_interfaces):
                l_1_static = resolve('static')
                l_1_boundaries = resolve('boundaries')
                l_1_source_route_export = resolve('source_route_export')
                _loop_vars = {}
                pass
                if t_7(environment.getattr(environment.getattr(l_1_multicast_interface, 'multicast'), 'ipv4')):
                    pass
                    l_1_static = t_1(environment.getattr(environment.getattr(environment.getattr(l_1_multicast_interface, 'multicast'), 'ipv4'), 'static'), '-')
                    _loop_vars['static'] = l_1_static
                    if t_7(environment.getattr(environment.getattr(environment.getattr(l_1_multicast_interface, 'multicast'), 'ipv4'), 'boundaries')):
                        pass
                        l_1_boundaries = t_3(context.eval_ctx, t_5(context, t_6(context, environment.getattr(environment.getattr(environment.getattr(l_1_multicast_interface, 'multicast'), 'ipv4'), 'boundaries'), 'boundary', 'arista.avd.defined'), attribute='boundary'), ', ')
                        _loop_vars['boundaries'] = l_1_boundaries
                    else:
                        pass
                        l_1_boundaries = '-'
                        _loop_vars['boundaries'] = l_1_boundaries
                    l_1_source_route_export = t_1(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_multicast_interface, 'multicast'), 'ipv4'), 'source_route_export'), 'enabled'), '-')
                    _loop_vars['source_route_export'] = l_1_source_route_export
                    yield '| '
                    yield str(environment.getattr(l_1_multicast_interface, 'name'))
                    yield ' | IPv4 | '
                    yield str((undefined(name='static') if l_1_static is missing else l_1_static))
                    yield ' | '
                    yield str((undefined(name='boundaries') if l_1_boundaries is missing else l_1_boundaries))
                    yield ' | '
                    yield str((undefined(name='source_route_export') if l_1_source_route_export is missing else l_1_source_route_export))
                    yield ' |\n'
                if t_7(environment.getattr(environment.getattr(l_1_multicast_interface, 'multicast'), 'ipv6')):
                    pass
                    l_1_static = t_1(environment.getattr(environment.getattr(environment.getattr(l_1_multicast_interface, 'multicast'), 'ipv6'), 'static'), '-')
                    _loop_vars['static'] = l_1_static
                    if t_7(environment.getattr(environment.getattr(environment.getattr(l_1_multicast_interface, 'multicast'), 'ipv6'), 'boundaries')):
                        pass
                        l_1_boundaries = t_3(context.eval_ctx, t_5(context, t_6(context, environment.getattr(environment.getattr(environment.getattr(l_1_multicast_interface, 'multicast'), 'ipv6'), 'boundaries'), 'boundary', 'arista.avd.defined'), attribute='boundary'), ', ')
                        _loop_vars['boundaries'] = l_1_boundaries
                    else:
                        pass
                        l_1_boundaries = '-'
                        _loop_vars['boundaries'] = l_1_boundaries
                    l_1_source_route_export = t_1(environment.getattr(environment.getattr(environment.getattr(environment.getattr(l_1_multicast_interface, 'multicast'), 'ipv6'), 'source_route_export'), 'enabled'), '-')
                    _loop_vars['source_route_export'] = l_1_source_route_export
                    yield '| '
                    yield str(environment.getattr(l_1_multicast_interface, 'name'))
                    yield ' | IPv6 | '
                    yield str((undefined(name='static') if l_1_static is missing else l_1_static))
                    yield ' | '
                    yield str((undefined(name='boundaries') if l_1_boundaries is missing else l_1_boundaries))
                    yield ' | '
                    yield str((undefined(name='source_route_export') if l_1_source_route_export is missing else l_1_source_route_export))
                    yield ' |\n'
            l_1_multicast_interface = l_1_static = l_1_boundaries = l_1_source_route_export = missing
        yield '\n#### VLAN Interfaces Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/vlan-interfaces.j2', 'documentation/vlan-interfaces.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {'multicast_interfaces': l_0_multicast_interfaces, 'vlan_interface_isis': l_0_vlan_interface_isis, 'vlan_interface_pvlan': l_0_vlan_interface_pvlan, 'vlan_interfaces_ipv6': l_0_vlan_interfaces_ipv6, 'vlan_interfaces_vrrp_details': l_0_vlan_interfaces_vrrp_details})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '2=66&10=69&11=73&12=75&13=77&14=79&15=82&18=93&19=96&20=99&21=102&22=104&23=107&26=109&32=112&33=115&34=118&43=124&44=128&45=130&46=132&47=134&48=136&49=138&50=140&51=143&54=160&55=163&56=166&57=168&60=170&66=173&67=179&68=181&69=183&70=185&72=189&74=191&75=193&77=197&79=199&80=201&81=203&82=205&83=207&84=210&88=231&89=234&90=237&91=239&94=241&100=244&101=247&102=257&103=259&104=261&105=263&106=265&107=267&109=269&110=271&111=273&112=275&113=278&114=279&115=281&116=282&117=284&120=286&121=288&123=290&124=292&125=294&126=297&131=319&132=322&133=325&134=328&135=330&136=333&139=335&145=338&146=343&147=345&148=347&149=349&150=351&151=353&153=357&155=360&160=369&161=372&162=375&163=377&166=379&172=382&173=388&174=390&175=392&176=394&180=398&182=400&183=403&185=411&186=413&187=415&188=417&192=421&194=423&195=426&203=436'