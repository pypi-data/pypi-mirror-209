from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos-intended-config.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    pass
    template = environment.get_template('eos/rancid-content-type.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/boot.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/terminal.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/prompt.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/aliases.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/hardware-counters.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/service-routing-configuration-bgp.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/daemon-terminattr.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/daemons.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/dhcp-relay.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/ip-dhcp-relay.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/switchport-default.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/vlan-internal-order.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/ip-igmp-snooping.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/event-monitor.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/flow-trackings.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/load-interval.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/interface-defaults.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/interface-profiles.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/transceiver-qsfp-default-mode.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/errdisable.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/service-routing-protocols-model.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/queue-monitor-length.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/lldp.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/l2-protocol-forwarding.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/lacp.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/logging.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/mcs-client.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/match-list-input.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/as-path.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/mac-security.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/hostname.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/ip-domain-lookup.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/ip-name-servers.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/dns-domain.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/domain-list.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/trackers.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/ntp.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/poe.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/ptp.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/radius-servers.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/radius-server.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/router-l2-vpn.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/sflow.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/redundancy.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/qos-profiles.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/snmp-server.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/hardware.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/spanning-tree.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/platform.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/service-unsupported-transceiver.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/tacacs-servers.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/aaa.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/enable-password.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/aaa-root.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/local-users.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/roles.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/address-locking.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/tap-aggregation.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/clock.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/vlans.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/vrfs.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/link-tracking-groups.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/cvx.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/port-channel-interfaces.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/ethernet-interfaces.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/loopback-interfaces.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/management-interfaces.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/tunnel-interfaces.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/vlan-interfaces.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/vxlan-interface.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/tcam-profile.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/monitor-connectivity.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/mac-address-table-aging-time.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/ip-virtual-router-mac-address.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/virtual-source-nat-vrfs.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/event-handlers.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/bgp-groups.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/interface-groups.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/ipv6-access-lists.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/ipv6-standard-access-lists.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/access-lists.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/ip-access-lists.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/standard-access-lists.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/mac-access-lists.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/ip-routing.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/ip-icmp-redirect.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/ip-hardware.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/ip-routing-vrfs.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/ipv6-unicast-routing.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/ipv6-unicast-routing-vrfs.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/ipv6-icmp-redirect.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/ipv6-hardware.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/monitor-sessions.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/qos.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/community-lists.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/ip-community-lists.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/ip-extcommunity-lists.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/ip-extcommunity-lists-regexp.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/dynamic-prefix-lists.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/prefix-lists.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/ipv6-prefix-lists.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/system.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/mac-address-table-notification.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/maintenance.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/mlag-configuration.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/static-routes.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/ipv6-static-routes.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/class-maps.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/policy-maps-pbr.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/policy-maps-qos.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/arp.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/route-maps.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/router-bfd.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/peer-filters.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/router-bgp.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/router-igmp.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/router-multicast.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/router-general.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/router-traffic-engineering.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/router-ospf.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/router-pim-sparse-mode.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/router-isis.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/router-msdp.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/mpls.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/patch-panel.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/queue-monitor-streaming.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/ip-tacacs-source-interfaces.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/ip-radius-source-interfaces.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/vmtracer-sessions.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/traffic-policies.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/banners.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/ip-http-client-source-interfaces.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/ip-ssh-client-source-interfaces.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/management-api-http.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/management-console.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/management-cvx.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/management-defaults.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/management-api-gnmi.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/management-api-models.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/management-security.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/dot1x.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/management-ssh.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/management-tech-support.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/eos-cli.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/custom-templates.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('eos/end.j2', 'eos-intended-config.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event

blocks = {}
debug_info = '2=11&4=14&6=17&8=20&10=23&12=26&14=29&16=32&18=35&20=38&22=41&24=44&26=47&28=50&30=53&32=56&34=59&36=62&38=65&40=68&42=71&44=74&46=77&48=80&50=83&52=86&54=89&56=92&58=95&60=98&62=101&64=104&66=107&68=110&70=113&72=116&74=119&76=122&78=125&80=128&82=131&84=134&86=137&88=140&90=143&92=146&94=149&96=152&98=155&100=158&102=161&104=164&106=167&108=170&110=173&112=176&114=179&116=182&118=185&120=188&122=191&124=194&126=197&128=200&130=203&132=206&134=209&136=212&138=215&140=218&142=221&144=224&146=227&148=230&150=233&152=236&154=239&156=242&158=245&160=248&162=251&164=254&166=257&168=260&170=263&172=266&174=269&176=272&178=275&180=278&182=281&184=284&186=287&188=290&190=293&192=296&194=299&196=302&198=305&200=308&202=311&204=314&206=317&208=320&210=323&212=326&214=329&216=332&218=335&220=338&222=341&224=344&226=347&228=350&230=353&232=356&234=359&236=362&238=365&240=368&242=371&244=374&246=377&248=380&250=383&252=386&254=389&256=392&258=395&260=398&262=401&264=404&266=407&268=410&270=413&272=416&274=419&276=422&278=425&280=428&282=431&284=434&286=437&288=440&290=443&292=446&294=449'