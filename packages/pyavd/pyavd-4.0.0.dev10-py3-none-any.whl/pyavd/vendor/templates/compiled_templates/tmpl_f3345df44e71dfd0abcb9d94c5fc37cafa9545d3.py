from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/snmp-server.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_snmp_server = resolve('snmp_server')
    l_0_row_contact = resolve('row_contact')
    l_0_row_location = resolve('row_location')
    l_0_row_state = resolve('row_state')
    l_0_row_traps_disabled = resolve('row_traps_disabled')
    l_0_row_traps_enabled = resolve('row_traps_enabled')
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
        t_4 = environment.filters['map']
    except KeyError:
        @internalcode
        def t_4(*unused):
            raise TemplateRuntimeError("No filter named 'map' found.")
    try:
        t_5 = environment.filters['rejectattr']
    except KeyError:
        @internalcode
        def t_5(*unused):
            raise TemplateRuntimeError("No filter named 'rejectattr' found.")
    try:
        t_6 = environment.filters['selectattr']
    except KeyError:
        @internalcode
        def t_6(*unused):
            raise TemplateRuntimeError("No filter named 'selectattr' found.")
    try:
        t_7 = environment.filters['string']
    except KeyError:
        @internalcode
        def t_7(*unused):
            raise TemplateRuntimeError("No filter named 'string' found.")
    try:
        t_8 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_8(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_8((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server)):
        pass
        yield '\n### SNMP\n\n#### SNMP Configuration Summary\n\n| Contact | Location | SNMP Traps | State |\n| ------- | -------- | ---------- | ----- |\n'
        l_0_row_contact = t_1(environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'contact'), '-')
        context.vars['row_contact'] = l_0_row_contact
        context.exported_vars.add('row_contact')
        l_0_row_location = t_1(environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'location'), '-')
        context.vars['row_location'] = l_0_row_location
        context.exported_vars.add('row_location')
        if t_8(environment.getattr(environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'traps'), 'enable'), True):
            pass
            l_0_row_state = 'Enabled'
            context.vars['row_state'] = l_0_row_state
            context.exported_vars.add('row_state')
        else:
            pass
            l_0_row_state = 'Disabled'
            context.vars['row_state'] = l_0_row_state
            context.exported_vars.add('row_state')
        yield '| '
        yield str((undefined(name='row_contact') if l_0_row_contact is missing else l_0_row_contact))
        yield ' | '
        yield str((undefined(name='row_location') if l_0_row_location is missing else l_0_row_location))
        yield ' | All | '
        yield str((undefined(name='row_state') if l_0_row_state is missing else l_0_row_state))
        yield ' |\n'
        if t_8(environment.getattr(environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'traps'), 'snmp_traps')):
            pass
            l_0_row_traps_disabled = t_3(context.eval_ctx, t_2(t_4(context, t_6(context, environment.getattr(environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'traps'), 'snmp_traps'), 'enabled', 'false'), attribute='name')), ', ')
            context.vars['row_traps_disabled'] = l_0_row_traps_disabled
            context.exported_vars.add('row_traps_disabled')
            l_0_row_traps_enabled = t_3(context.eval_ctx, t_2(t_4(context, t_5(context, environment.getattr(environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'traps'), 'snmp_traps'), 'enabled', 'false'), attribute='name')), ', ')
            context.vars['row_traps_enabled'] = l_0_row_traps_enabled
            context.exported_vars.add('row_traps_enabled')
            if t_8((undefined(name='row_traps_enabled') if l_0_row_traps_enabled is missing else l_0_row_traps_enabled)):
                pass
                yield '| '
                yield str((undefined(name='row_contact') if l_0_row_contact is missing else l_0_row_contact))
                yield ' | '
                yield str((undefined(name='row_location') if l_0_row_location is missing else l_0_row_location))
                yield ' | '
                yield str((undefined(name='row_traps_enabled') if l_0_row_traps_enabled is missing else l_0_row_traps_enabled))
                yield ' | Enabled |\n'
            if t_8((undefined(name='row_traps_disabled') if l_0_row_traps_disabled is missing else l_0_row_traps_disabled)):
                pass
                yield '| '
                yield str((undefined(name='row_contact') if l_0_row_contact is missing else l_0_row_contact))
                yield ' | '
                yield str((undefined(name='row_location') if l_0_row_location is missing else l_0_row_location))
                yield ' | '
                yield str((undefined(name='row_traps_disabled') if l_0_row_traps_disabled is missing else l_0_row_traps_disabled))
                yield ' | Disabled |\n'
        if t_8(environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'engine_ids')):
            pass
            yield '\n#### SNMP EngineID Configuration\n\n| Type | EngineID (Hex) | IP | Port |\n| ---- | -------------- | -- | ---- |\n'
            if t_8(environment.getattr(environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'engine_ids'), 'local')):
                pass
                yield '| local | '
                yield str(environment.getattr(environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'engine_ids'), 'local'))
                yield ' | - | - |\n'
            for l_1_engine_id in t_1(environment.getattr(environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'engine_ids'), 'remotes'), []):
                l_1_row_udp_port = resolve('row_udp_port')
                _loop_vars = {}
                pass
                if (t_8(environment.getattr(l_1_engine_id, 'id')) and t_8(environment.getattr(l_1_engine_id, 'address'))):
                    pass
                    l_1_row_udp_port = t_1(environment.getattr(l_1_engine_id, 'udp_port'), '-')
                    _loop_vars['row_udp_port'] = l_1_row_udp_port
                    yield '| remote | '
                    yield str(environment.getattr(l_1_engine_id, 'id'))
                    yield ' | '
                    yield str(environment.getattr(l_1_engine_id, 'address'))
                    yield ' | '
                    yield str((undefined(name='row_udp_port') if l_1_row_udp_port is missing else l_1_row_udp_port))
                    yield ' |\n'
            l_1_engine_id = l_1_row_udp_port = missing
        if t_8(environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'ipv4_acls')):
            pass
            yield '\n#### SNMP ACLs\n| IP | ACL | VRF |\n| -- | --- | --- |\n'
            for l_1_acl in environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'ipv4_acls'):
                _loop_vars = {}
                pass
                yield '| IPv4 | '
                yield str(t_1(environment.getattr(l_1_acl, 'name'), '-'))
                yield ' | '
                yield str(t_1(environment.getattr(l_1_acl, 'vrf'), 'default'))
                yield ' |\n'
            l_1_acl = missing
        if t_8(environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'ipv6_acls')):
            pass
            for l_1_acl in environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'ipv6_acls'):
                _loop_vars = {}
                pass
                yield '| IPv6 | '
                yield str(t_1(environment.getattr(l_1_acl, 'name'), '-'))
                yield ' | '
                yield str(t_1(environment.getattr(l_1_acl, 'vrf'), 'default'))
                yield ' |\n'
            l_1_acl = missing
        if t_8(environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'local_interfaces')):
            pass
            yield '\n#### SNMP Local Interfaces\n\n| Local Interface | VRF |\n| --------------- | --- |\n'
            for l_1_interface in environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'local_interfaces'):
                _loop_vars = {}
                pass
                yield '| '
                yield str(environment.getattr(l_1_interface, 'name'))
                yield ' | '
                yield str(t_1(environment.getattr(l_1_interface, 'vrf'), 'default'))
                yield ' |\n'
            l_1_interface = missing
        if t_8(environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'vrfs')):
            pass
            yield '\n#### SNMP VRF Status\n\n| VRF | Status |\n| --- | ------ |\n'
            for l_1_vrf in environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'vrfs'):
                l_1_status = resolve('status')
                _loop_vars = {}
                pass
                if t_1(environment.getattr(l_1_vrf, 'enable'), False):
                    pass
                    l_1_status = 'Enabled'
                    _loop_vars['status'] = l_1_status
                else:
                    pass
                    l_1_status = 'Disabled'
                    _loop_vars['status'] = l_1_status
                yield '| '
                yield str(environment.getattr(l_1_vrf, 'name'))
                yield ' | '
                yield str((undefined(name='status') if l_1_status is missing else l_1_status))
                yield ' |\n'
            l_1_vrf = l_1_status = missing
        if t_8(environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'hosts')):
            pass
            yield '\n#### SNMP Hosts Configuration\n\n| Host | VRF | Community | Username | Authentication level | SNMP Version |\n| ---- |---- | --------- | -------- | -------------------- | ------------ |\n'
            for l_1_host in environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'hosts'):
                l_1_row_host = resolve('row_host')
                l_1_row_vrf = resolve('row_vrf')
                _loop_vars = {}
                pass
                if t_8(environment.getattr(l_1_host, 'host')):
                    pass
                    l_1_row_host = environment.getattr(l_1_host, 'host')
                    _loop_vars['row_host'] = l_1_row_host
                    l_1_row_vrf = t_1(environment.getattr(l_1_host, 'vrf'), '-')
                    _loop_vars['row_vrf'] = l_1_row_vrf
                    if (t_8(environment.getattr(l_1_host, 'users')) and (t_7(t_1(environment.getattr(l_1_host, 'version'), '3')) == '3')):
                        pass
                        for l_2_user in environment.getattr(l_1_host, 'users'):
                            _loop_vars = {}
                            pass
                            if (t_8(environment.getattr(l_2_user, 'username')) and t_8(environment.getattr(l_2_user, 'authentication_level'))):
                                pass
                                yield '| '
                                yield str((undefined(name='row_host') if l_1_row_host is missing else l_1_row_host))
                                yield ' | '
                                yield str((undefined(name='row_vrf') if l_1_row_vrf is missing else l_1_row_vrf))
                                yield ' | - | '
                                yield str(environment.getattr(l_2_user, 'username'))
                                yield ' | '
                                yield str(environment.getattr(l_2_user, 'authentication_level'))
                                yield ' | '
                                yield str(t_1(environment.getattr(l_1_host, 'version'), '3'))
                                yield ' |\n'
                        l_2_user = missing
                    elif (t_8(environment.getattr(l_1_host, 'community')) and (t_7(t_1(environment.getattr(l_1_host, 'version'), '2c')) in ['1', '2c'])):
                        pass
                        yield '| '
                        yield str((undefined(name='row_host') if l_1_row_host is missing else l_1_row_host))
                        yield ' | '
                        yield str((undefined(name='row_vrf') if l_1_row_vrf is missing else l_1_row_vrf))
                        yield ' | '
                        yield str(environment.getattr(l_1_host, 'community'))
                        yield ' | - | - | '
                        yield str(t_1(environment.getattr(l_1_host, 'version'), '2c'))
                        yield ' |\n'
            l_1_host = l_1_row_host = l_1_row_vrf = missing
        if t_8(environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'views')):
            pass
            yield '\n#### SNMP Views Configuration\n\n| View | MIB Family Name | Status |\n| ---- | --------------- | ------ |\n'
            for l_1_view in environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'views'):
                l_1_row_status = resolve('row_status')
                l_1_row_view = l_1_row_mib_family_name = missing
                _loop_vars = {}
                pass
                l_1_row_view = t_1(environment.getattr(l_1_view, 'name'), 'default')
                _loop_vars['row_view'] = l_1_row_view
                l_1_row_mib_family_name = t_1(environment.getattr(l_1_view, 'MIB_family_name'), '-')
                _loop_vars['row_mib_family_name'] = l_1_row_mib_family_name
                if t_1(environment.getattr(l_1_view, 'included'), False):
                    pass
                    l_1_row_status = 'Included'
                    _loop_vars['row_status'] = l_1_row_status
                else:
                    pass
                    l_1_row_status = 'Excluded'
                    _loop_vars['row_status'] = l_1_row_status
                yield '| '
                yield str((undefined(name='row_view') if l_1_row_view is missing else l_1_row_view))
                yield ' | '
                yield str((undefined(name='row_mib_family_name') if l_1_row_mib_family_name is missing else l_1_row_mib_family_name))
                yield ' | '
                yield str((undefined(name='row_status') if l_1_row_status is missing else l_1_row_status))
                yield ' |\n'
            l_1_view = l_1_row_view = l_1_row_mib_family_name = l_1_row_status = missing
        if t_8(environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'communities')):
            pass
            yield '\n#### SNMP Communities\n\n| Community | Access | Access List IPv4 | Access List IPv6 | View |\n| --------- | ------ | ---------------- | ---------------- | ---- |\n'
            for l_1_community in t_2(environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'communities'), 'name'):
                l_1_access = l_1_access_list_ipv4 = l_1_access_list_ipv6 = l_1_view = missing
                _loop_vars = {}
                pass
                l_1_access = t_1(environment.getattr(l_1_community, 'access'), 'ro')
                _loop_vars['access'] = l_1_access
                l_1_access_list_ipv4 = t_1(environment.getattr(environment.getattr(l_1_community, 'access_list_ipv4'), 'name'), '-')
                _loop_vars['access_list_ipv4'] = l_1_access_list_ipv4
                l_1_access_list_ipv6 = t_1(environment.getattr(environment.getattr(l_1_community, 'access_list_ipv6'), 'name'), '-')
                _loop_vars['access_list_ipv6'] = l_1_access_list_ipv6
                l_1_view = t_1(environment.getattr(l_1_community, 'view'), '-')
                _loop_vars['view'] = l_1_view
                yield '| '
                yield str(environment.getattr(l_1_community, 'name'))
                yield ' | '
                yield str((undefined(name='access') if l_1_access is missing else l_1_access))
                yield ' | '
                yield str((undefined(name='access_list_ipv4') if l_1_access_list_ipv4 is missing else l_1_access_list_ipv4))
                yield ' | '
                yield str((undefined(name='access_list_ipv6') if l_1_access_list_ipv6 is missing else l_1_access_list_ipv6))
                yield ' | '
                yield str((undefined(name='view') if l_1_view is missing else l_1_view))
                yield ' |\n'
            l_1_community = l_1_access = l_1_access_list_ipv4 = l_1_access_list_ipv6 = l_1_view = missing
        if t_8(environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'groups')):
            pass
            yield '\n#### SNMP Groups Configuration\n\n| Group | SNMP Version | Authentication | Read | Write | Notify |\n| ----- | ------------ | -------------- | ---- | ----- | ------ |\n'
            for l_1_group in environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'groups'):
                l_1_row_group = l_1_row_version = l_1_row_auth = l_1_row_read = l_1_row_write = l_1_row_notify = missing
                _loop_vars = {}
                pass
                l_1_row_group = t_1(environment.getattr(l_1_group, 'name'), 'default')
                _loop_vars['row_group'] = l_1_row_group
                l_1_row_version = t_1(environment.getattr(l_1_group, 'version'), '-')
                _loop_vars['row_version'] = l_1_row_version
                l_1_row_auth = t_1(environment.getattr(l_1_group, 'authentication'), '-')
                _loop_vars['row_auth'] = l_1_row_auth
                l_1_row_read = t_1(environment.getattr(l_1_group, 'read'), '-')
                _loop_vars['row_read'] = l_1_row_read
                l_1_row_write = t_1(environment.getattr(l_1_group, 'write'), '-')
                _loop_vars['row_write'] = l_1_row_write
                l_1_row_notify = t_1(environment.getattr(l_1_group, 'notify'), '-')
                _loop_vars['row_notify'] = l_1_row_notify
                yield '| '
                yield str((undefined(name='row_group') if l_1_row_group is missing else l_1_row_group))
                yield ' | '
                yield str((undefined(name='row_version') if l_1_row_version is missing else l_1_row_version))
                yield ' | '
                yield str((undefined(name='row_auth') if l_1_row_auth is missing else l_1_row_auth))
                yield ' | '
                yield str((undefined(name='row_read') if l_1_row_read is missing else l_1_row_read))
                yield ' | '
                yield str((undefined(name='row_write') if l_1_row_write is missing else l_1_row_write))
                yield ' | '
                yield str((undefined(name='row_notify') if l_1_row_notify is missing else l_1_row_notify))
                yield ' |\n'
            l_1_group = l_1_row_group = l_1_row_version = l_1_row_auth = l_1_row_read = l_1_row_write = l_1_row_notify = missing
        if t_8(environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'users')):
            pass
            yield '\n#### SNMP Users Configuration\n\n| User | Group | Version | Authentication | Privacy | Remote Address | Remote Port | Engine ID |\n| ---- | ----- | ------- | -------------- | ------- | -------------- | ----------- | --------- |\n'
            for l_1_user in environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'users'):
                l_1_row_user = l_1_row_group = l_1_row_version = l_1_row_auth = l_1_row_policy = l_1_row_remote_address = l_1_row_udp_port = l_1_row_engine_id = missing
                _loop_vars = {}
                pass
                l_1_row_user = t_1(environment.getattr(l_1_user, 'name'), 'default')
                _loop_vars['row_user'] = l_1_row_user
                l_1_row_group = t_1(environment.getattr(l_1_user, 'group'), '-')
                _loop_vars['row_group'] = l_1_row_group
                l_1_row_version = t_1(environment.getattr(l_1_user, 'version'), '-')
                _loop_vars['row_version'] = l_1_row_version
                l_1_row_auth = t_1(environment.getattr(l_1_user, 'auth'), '-')
                _loop_vars['row_auth'] = l_1_row_auth
                l_1_row_policy = t_1(environment.getattr(l_1_user, 'priv'), '-')
                _loop_vars['row_policy'] = l_1_row_policy
                l_1_row_remote_address = t_1(environment.getattr(l_1_user, 'remote_address'), '-')
                _loop_vars['row_remote_address'] = l_1_row_remote_address
                l_1_row_udp_port = t_1(environment.getattr(l_1_user, 'udp_port'), '-')
                _loop_vars['row_udp_port'] = l_1_row_udp_port
                l_1_row_engine_id = t_1(environment.getattr(l_1_user, 'localized'), '-')
                _loop_vars['row_engine_id'] = l_1_row_engine_id
                yield '| '
                yield str((undefined(name='row_user') if l_1_row_user is missing else l_1_row_user))
                yield ' | '
                yield str((undefined(name='row_group') if l_1_row_group is missing else l_1_row_group))
                yield ' | '
                yield str((undefined(name='row_version') if l_1_row_version is missing else l_1_row_version))
                yield ' | '
                yield str((undefined(name='row_auth') if l_1_row_auth is missing else l_1_row_auth))
                yield ' | '
                yield str((undefined(name='row_policy') if l_1_row_policy is missing else l_1_row_policy))
                yield ' | '
                yield str((undefined(name='row_remote_address') if l_1_row_remote_address is missing else l_1_row_remote_address))
                yield ' | '
                yield str((undefined(name='row_udp_port') if l_1_row_udp_port is missing else l_1_row_udp_port))
                yield ' | '
                yield str((undefined(name='row_engine_id') if l_1_row_engine_id is missing else l_1_row_engine_id))
                yield ' |\n'
            l_1_user = l_1_row_user = l_1_row_group = l_1_row_version = l_1_row_auth = l_1_row_policy = l_1_row_remote_address = l_1_row_udp_port = l_1_row_engine_id = missing
        yield '\n#### SNMP Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/snmp-server.j2', 'documentation/snmp-server.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {'row_contact': l_0_row_contact, 'row_location': l_0_row_location, 'row_state': l_0_row_state, 'row_traps_disabled': l_0_row_traps_disabled, 'row_traps_enabled': l_0_row_traps_enabled})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '2=65&10=68&11=71&12=74&13=76&15=81&17=85&18=91&19=93&20=96&21=99&22=102&24=108&25=111&28=117&34=120&35=123&37=125&38=129&39=131&40=134&44=141&49=144&50=148&53=153&54=155&55=159&58=164&64=167&65=171&68=176&74=179&75=183&76=185&78=189&80=192&83=197&89=200&90=205&91=207&92=209&93=211&95=213&96=216&98=219&101=230&103=233&108=242&114=245&115=250&116=252&117=254&118=256&120=260&122=263&125=270&131=273&132=277&133=279&134=281&135=283&136=286&139=297&145=300&146=304&147=306&148=308&149=310&150=312&151=314&152=317&155=330&161=333&162=337&163=339&164=341&165=343&166=345&167=347&168=349&169=351&170=354&177=372'