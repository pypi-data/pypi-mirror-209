from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos-device-documentation.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_inventory_hostname = resolve('inventory_hostname')
    pass
    yield '# '
    yield str((undefined(name='inventory_hostname') if l_0_inventory_hostname is missing else l_0_inventory_hostname))
    yield '\n\n## Table of Contents\n\n<!-- toc -->\n<!-- toc -->\n'
    template = environment.get_template('documentation/management.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('documentation/cvx.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('documentation/authentication.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('documentation/address-locking.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('documentation/management-security.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('documentation/prompt.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('documentation/aliases.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('documentation/dhcp-relay.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('documentation/boot.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('documentation/monitoring.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('documentation/monitor-connectivity.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('documentation/tcam-profile.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('documentation/link-tracking-groups.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('documentation/mlag-configuration.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('documentation/lldp.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('documentation/l2-protocol-forwarding.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('documentation/lacp.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('documentation/spanning-tree.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('documentation/vlan-internal-order.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('documentation/vlans.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('documentation/mac-address-table.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('documentation/interfaces.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('documentation/routing.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('documentation/bfd.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('documentation/mpls.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('documentation/patch-panel.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('documentation/multicast.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('documentation/filters.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('documentation/dot1x.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('documentation/poe.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('documentation/acl.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('documentation/vrfs.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('documentation/virtual-source-nat-vrfs.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('documentation/platform.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('documentation/router-l2-vpn.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('documentation/ip-dhcp-relay.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('documentation/errdisable.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('documentation/mac-security.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('documentation/traffic-policies.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('documentation/quality-of-service.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('documentation/maintenance-mode.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('documentation/eos-cli.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event
    template = environment.get_template('documentation/custom-templates.j2', 'eos-device-documentation.j2')
    for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
        yield event

blocks = {}
debug_info = '1=13&8=15&10=18&12=21&14=24&16=27&18=30&20=33&22=36&24=39&26=42&28=45&30=48&32=51&34=54&36=57&38=60&40=63&42=66&44=69&46=72&48=75&50=78&52=81&54=84&56=87&58=90&60=93&62=96&64=99&66=102&68=105&70=108&72=111&74=114&76=117&78=120&80=123&82=126&84=129&86=132&88=135&90=138&92=141'