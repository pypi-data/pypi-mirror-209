from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/snmp-server.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_snmp_server = resolve('snmp_server')
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
        t_3 = environment.filters['string']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No filter named 'string' found.")
    try:
        t_4 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_4(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_4((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server)):
        pass
        yield '!\n'
        if t_4(environment.getattr(environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'engine_ids'), 'local')):
            pass
            yield 'snmp-server engineID local '
            yield str(environment.getattr(environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'engine_ids'), 'local'))
            yield '\n'
        if t_4(environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'contact')):
            pass
            yield 'snmp-server contact '
            yield str(environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'contact'))
            yield '\n'
        if t_4(environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'location')):
            pass
            yield 'snmp-server location '
            yield str(environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'location'))
            yield '\n'
        if t_4(environment.getattr(environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'engine_ids'), 'remotes')):
            pass
            for l_1_engine_id in environment.getattr(environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'engine_ids'), 'remotes'):
                l_1_remote_engine_ids_cli = resolve('remote_engine_ids_cli')
                _loop_vars = {}
                pass
                if (t_4(environment.getattr(l_1_engine_id, 'id')) and t_4(environment.getattr(l_1_engine_id, 'address'))):
                    pass
                    l_1_remote_engine_ids_cli = str_join(('snmp-server engineID remote ', environment.getattr(l_1_engine_id, 'address'), ))
                    _loop_vars['remote_engine_ids_cli'] = l_1_remote_engine_ids_cli
                    if t_4(environment.getattr(l_1_engine_id, 'udp_port')):
                        pass
                        l_1_remote_engine_ids_cli = str_join(((undefined(name='remote_engine_ids_cli') if l_1_remote_engine_ids_cli is missing else l_1_remote_engine_ids_cli), ' udp-port ', environment.getattr(l_1_engine_id, 'udp_port'), ))
                        _loop_vars['remote_engine_ids_cli'] = l_1_remote_engine_ids_cli
                    l_1_remote_engine_ids_cli = str_join(((undefined(name='remote_engine_ids_cli') if l_1_remote_engine_ids_cli is missing else l_1_remote_engine_ids_cli), ' ', environment.getattr(l_1_engine_id, 'id'), ))
                    _loop_vars['remote_engine_ids_cli'] = l_1_remote_engine_ids_cli
                    yield str((undefined(name='remote_engine_ids_cli') if l_1_remote_engine_ids_cli is missing else l_1_remote_engine_ids_cli))
                    yield '\n'
            l_1_engine_id = l_1_remote_engine_ids_cli = missing
        if t_4(environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'ipv4_acls')):
            pass
            for l_1_acl in environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'ipv4_acls'):
                l_1_acl_cli = missing
                _loop_vars = {}
                pass
                l_1_acl_cli = str_join(('snmp-server ipv4 access-list ', environment.getattr(l_1_acl, 'name'), ))
                _loop_vars['acl_cli'] = l_1_acl_cli
                if t_4(environment.getattr(l_1_acl, 'vrf')):
                    pass
                    l_1_acl_cli = str_join(((undefined(name='acl_cli') if l_1_acl_cli is missing else l_1_acl_cli), ' vrf ', environment.getattr(l_1_acl, 'vrf'), ))
                    _loop_vars['acl_cli'] = l_1_acl_cli
                yield str((undefined(name='acl_cli') if l_1_acl_cli is missing else l_1_acl_cli))
                yield '\n'
            l_1_acl = l_1_acl_cli = missing
        if t_4(environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'ipv6_acls')):
            pass
            for l_1_acl in environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'ipv6_acls'):
                l_1_acl_cli = missing
                _loop_vars = {}
                pass
                l_1_acl_cli = str_join(('snmp-server ipv6 access-list ', environment.getattr(l_1_acl, 'name'), ))
                _loop_vars['acl_cli'] = l_1_acl_cli
                if t_4(environment.getattr(l_1_acl, 'vrf')):
                    pass
                    l_1_acl_cli = str_join(((undefined(name='acl_cli') if l_1_acl_cli is missing else l_1_acl_cli), ' vrf ', environment.getattr(l_1_acl, 'vrf'), ))
                    _loop_vars['acl_cli'] = l_1_acl_cli
                yield str((undefined(name='acl_cli') if l_1_acl_cli is missing else l_1_acl_cli))
                yield '\n'
            l_1_acl = l_1_acl_cli = missing
        if t_4(environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'local_interfaces')):
            pass
            for l_1_local_interface in environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'local_interfaces'):
                l_1_interface_snmp_cli = missing
                _loop_vars = {}
                pass
                l_1_interface_snmp_cli = 'snmp-server'
                _loop_vars['interface_snmp_cli'] = l_1_interface_snmp_cli
                if t_4(environment.getattr(l_1_local_interface, 'vrf')):
                    pass
                    l_1_interface_snmp_cli = str_join(((undefined(name='interface_snmp_cli') if l_1_interface_snmp_cli is missing else l_1_interface_snmp_cli), ' vrf ', environment.getattr(l_1_local_interface, 'vrf'), ))
                    _loop_vars['interface_snmp_cli'] = l_1_interface_snmp_cli
                l_1_interface_snmp_cli = str_join(((undefined(name='interface_snmp_cli') if l_1_interface_snmp_cli is missing else l_1_interface_snmp_cli), ' local-interface ', environment.getattr(l_1_local_interface, 'name'), ))
                _loop_vars['interface_snmp_cli'] = l_1_interface_snmp_cli
                yield str((undefined(name='interface_snmp_cli') if l_1_interface_snmp_cli is missing else l_1_interface_snmp_cli))
                yield '\n'
            l_1_local_interface = l_1_interface_snmp_cli = missing
        if t_4(environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'views')):
            pass
            for l_1_view in environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'views'):
                l_1_view_cli = resolve('view_cli')
                _loop_vars = {}
                pass
                if t_4(environment.getattr(l_1_view, 'name')):
                    pass
                    l_1_view_cli = str_join(('snmp-server view ', environment.getattr(l_1_view, 'name'), ))
                    _loop_vars['view_cli'] = l_1_view_cli
                if t_4(environment.getattr(l_1_view, 'MIB_family_name')):
                    pass
                    l_1_view_cli = str_join(((undefined(name='view_cli') if l_1_view_cli is missing else l_1_view_cli), ' ', environment.getattr(l_1_view, 'MIB_family_name'), ' ', ))
                    _loop_vars['view_cli'] = l_1_view_cli
                if t_4(environment.getattr(l_1_view, 'included'), True):
                    pass
                    l_1_view_cli = str_join(((undefined(name='view_cli') if l_1_view_cli is missing else l_1_view_cli), 'included', ))
                    _loop_vars['view_cli'] = l_1_view_cli
                elif t_4(environment.getattr(l_1_view, 'included'), False):
                    pass
                    l_1_view_cli = str_join(((undefined(name='view_cli') if l_1_view_cli is missing else l_1_view_cli), 'excluded', ))
                    _loop_vars['view_cli'] = l_1_view_cli
                yield str((undefined(name='view_cli') if l_1_view_cli is missing else l_1_view_cli))
                yield '\n'
            l_1_view = l_1_view_cli = missing
        if t_4(environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'communities')):
            pass
            for l_1_community in t_2(environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'communities'), 'name'):
                l_1_communities_cli = missing
                _loop_vars = {}
                pass
                l_1_communities_cli = str_join(('snmp-server community ', environment.getattr(l_1_community, 'name'), ))
                _loop_vars['communities_cli'] = l_1_communities_cli
                if t_4(environment.getattr(l_1_community, 'view')):
                    pass
                    l_1_communities_cli = str_join(((undefined(name='communities_cli') if l_1_communities_cli is missing else l_1_communities_cli), ' view ', environment.getattr(l_1_community, 'view'), ))
                    _loop_vars['communities_cli'] = l_1_communities_cli
                if t_4(environment.getattr(l_1_community, 'access')):
                    pass
                    l_1_communities_cli = str_join(((undefined(name='communities_cli') if l_1_communities_cli is missing else l_1_communities_cli), ' ', environment.getattr(l_1_community, 'access'), ))
                    _loop_vars['communities_cli'] = l_1_communities_cli
                else:
                    pass
                    l_1_communities_cli = str_join(((undefined(name='communities_cli') if l_1_communities_cli is missing else l_1_communities_cli), ' ro', ))
                    _loop_vars['communities_cli'] = l_1_communities_cli
                if t_4(environment.getattr(l_1_community, 'access_list_ipv6')):
                    pass
                    l_1_communities_cli = str_join(((undefined(name='communities_cli') if l_1_communities_cli is missing else l_1_communities_cli), ' ipv6 ', environment.getattr(environment.getattr(l_1_community, 'access_list_ipv6'), 'name'), ))
                    _loop_vars['communities_cli'] = l_1_communities_cli
                if t_4(environment.getattr(l_1_community, 'access_list_ipv4')):
                    pass
                    l_1_communities_cli = str_join(((undefined(name='communities_cli') if l_1_communities_cli is missing else l_1_communities_cli), ' ', environment.getattr(environment.getattr(l_1_community, 'access_list_ipv4'), 'name'), ))
                    _loop_vars['communities_cli'] = l_1_communities_cli
                yield str((undefined(name='communities_cli') if l_1_communities_cli is missing else l_1_communities_cli))
                yield '\n'
            l_1_community = l_1_communities_cli = missing
        if t_4(environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'groups')):
            pass
            for l_1_group in environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'groups'):
                l_1_group_cli = resolve('group_cli')
                _loop_vars = {}
                pass
                if t_4(environment.getattr(l_1_group, 'name')):
                    pass
                    l_1_group_cli = str_join(('snmp-server group ', environment.getattr(l_1_group, 'name'), ))
                    _loop_vars['group_cli'] = l_1_group_cli
                if t_4(environment.getattr(l_1_group, 'version')):
                    pass
                    l_1_group_cli = str_join(((undefined(name='group_cli') if l_1_group_cli is missing else l_1_group_cli), ' ', environment.getattr(l_1_group, 'version'), ))
                    _loop_vars['group_cli'] = l_1_group_cli
                if (t_4(environment.getattr(l_1_group, 'authentication')) and t_4(environment.getattr(l_1_group, 'version'), 'v3')):
                    pass
                    l_1_group_cli = str_join(((undefined(name='group_cli') if l_1_group_cli is missing else l_1_group_cli), ' ', environment.getattr(l_1_group, 'authentication'), ))
                    _loop_vars['group_cli'] = l_1_group_cli
                if t_4(environment.getattr(l_1_group, 'read')):
                    pass
                    l_1_group_cli = str_join(((undefined(name='group_cli') if l_1_group_cli is missing else l_1_group_cli), ' read ', environment.getattr(l_1_group, 'read'), ))
                    _loop_vars['group_cli'] = l_1_group_cli
                if t_4(environment.getattr(l_1_group, 'write')):
                    pass
                    l_1_group_cli = str_join(((undefined(name='group_cli') if l_1_group_cli is missing else l_1_group_cli), ' write ', environment.getattr(l_1_group, 'write'), ))
                    _loop_vars['group_cli'] = l_1_group_cli
                if t_4(environment.getattr(l_1_group, 'notify')):
                    pass
                    l_1_group_cli = str_join(((undefined(name='group_cli') if l_1_group_cli is missing else l_1_group_cli), ' notify ', environment.getattr(l_1_group, 'notify'), ))
                    _loop_vars['group_cli'] = l_1_group_cli
                yield str((undefined(name='group_cli') if l_1_group_cli is missing else l_1_group_cli))
                yield '\n'
            l_1_group = l_1_group_cli = missing
        if t_4(environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'users')):
            pass
            for l_1_user in environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'users'):
                l_1_user_cli = resolve('user_cli')
                _loop_vars = {}
                pass
                if t_4(environment.getattr(l_1_user, 'name')):
                    pass
                    l_1_user_cli = str_join(('snmp-server user ', environment.getattr(l_1_user, 'name'), ))
                    _loop_vars['user_cli'] = l_1_user_cli
                if t_4(environment.getattr(l_1_user, 'group')):
                    pass
                    l_1_user_cli = str_join(((undefined(name='user_cli') if l_1_user_cli is missing else l_1_user_cli), ' ', environment.getattr(l_1_user, 'group'), ))
                    _loop_vars['user_cli'] = l_1_user_cli
                if (t_4(environment.getattr(l_1_user, 'remote_address')) and t_4(environment.getattr(l_1_user, 'version'), 'v3')):
                    pass
                    l_1_user_cli = str_join(((undefined(name='user_cli') if l_1_user_cli is missing else l_1_user_cli), ' remote ', environment.getattr(l_1_user, 'remote_address'), ))
                    _loop_vars['user_cli'] = l_1_user_cli
                    if t_4(environment.getattr(l_1_user, 'udp_port')):
                        pass
                        l_1_user_cli = str_join(((undefined(name='user_cli') if l_1_user_cli is missing else l_1_user_cli), ' udp-port ', environment.getattr(l_1_user, 'udp_port'), ))
                        _loop_vars['user_cli'] = l_1_user_cli
                if t_4(environment.getattr(l_1_user, 'version')):
                    pass
                    l_1_user_cli = str_join(((undefined(name='user_cli') if l_1_user_cli is missing else l_1_user_cli), ' ', environment.getattr(l_1_user, 'version'), ))
                    _loop_vars['user_cli'] = l_1_user_cli
                if ((t_4(environment.getattr(l_1_user, 'auth')) and t_4(environment.getattr(l_1_user, 'version'), 'v3')) and t_4(environment.getattr(l_1_user, 'auth_passphrase'))):
                    pass
                    if t_4(environment.getattr(l_1_user, 'localized')):
                        pass
                        l_1_user_cli = str_join(((undefined(name='user_cli') if l_1_user_cli is missing else l_1_user_cli), ' localized ', environment.getattr(l_1_user, 'localized'), ))
                        _loop_vars['user_cli'] = l_1_user_cli
                    l_1_user_cli = str_join(((undefined(name='user_cli') if l_1_user_cli is missing else l_1_user_cli), ' auth ', environment.getattr(l_1_user, 'auth'), ' ', environment.getattr(l_1_user, 'auth_passphrase'), ))
                    _loop_vars['user_cli'] = l_1_user_cli
                    if (t_4(environment.getattr(l_1_user, 'priv')) and t_4(environment.getattr(l_1_user, 'priv_passphrase'))):
                        pass
                        l_1_user_cli = str_join(((undefined(name='user_cli') if l_1_user_cli is missing else l_1_user_cli), ' priv ', environment.getattr(l_1_user, 'priv'), ' ', environment.getattr(l_1_user, 'priv_passphrase'), ))
                        _loop_vars['user_cli'] = l_1_user_cli
                yield str((undefined(name='user_cli') if l_1_user_cli is missing else l_1_user_cli))
                yield '\n'
            l_1_user = l_1_user_cli = missing
        if t_4(environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'hosts')):
            pass
            for l_1_host in environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'hosts'):
                l_1_host_cli = resolve('host_cli')
                _loop_vars = {}
                pass
                if t_4(environment.getattr(l_1_host, 'host')):
                    pass
                    l_1_host_cli = str_join(('snmp-server host ', environment.getattr(l_1_host, 'host'), ))
                    _loop_vars['host_cli'] = l_1_host_cli
                    if t_4(environment.getattr(l_1_host, 'vrf')):
                        pass
                        l_1_host_cli = str_join(((undefined(name='host_cli') if l_1_host_cli is missing else l_1_host_cli), ' vrf ', environment.getattr(l_1_host, 'vrf'), ))
                        _loop_vars['host_cli'] = l_1_host_cli
                    if (t_4(environment.getattr(l_1_host, 'users')) and (t_3(t_1(environment.getattr(l_1_host, 'version'), '3')) == '3')):
                        pass
                        for l_2_user in environment.getattr(l_1_host, 'users'):
                            _loop_vars = {}
                            pass
                            if (t_4(environment.getattr(l_2_user, 'username')) and t_4(environment.getattr(l_2_user, 'authentication_level'))):
                                pass
                                yield str((undefined(name='host_cli') if l_1_host_cli is missing else l_1_host_cli))
                                yield ' version 3 '
                                yield str(environment.getattr(l_2_user, 'authentication_level'))
                                yield ' '
                                yield str(environment.getattr(l_2_user, 'username'))
                                yield '\n'
                        l_2_user = missing
                    elif (t_4(environment.getattr(l_1_host, 'community')) and (t_3(t_1(environment.getattr(l_1_host, 'version'), '2c')) in ['1', '2c'])):
                        pass
                        yield str((undefined(name='host_cli') if l_1_host_cli is missing else l_1_host_cli))
                        yield ' version '
                        yield str(t_1(environment.getattr(l_1_host, 'version'), '2c'))
                        yield ' '
                        yield str(environment.getattr(l_1_host, 'community'))
                        yield '\n'
            l_1_host = l_1_host_cli = missing
        if t_4(environment.getattr(environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'traps'), 'enable'), True):
            pass
            yield 'snmp-server enable traps\n'
        elif t_4(environment.getattr(environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'traps'), 'enable'), False):
            pass
            yield 'no snmp-server enable traps\n'
        for l_1_snmp_trap in t_2(environment.getattr(environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'traps'), 'snmp_traps'), 'name'):
            _loop_vars = {}
            pass
            if t_4(environment.getattr(l_1_snmp_trap, 'enabled'), False):
                pass
                yield 'no snmp-server enable traps '
                yield str(environment.getattr(l_1_snmp_trap, 'name'))
                yield '\n'
            else:
                pass
                yield 'snmp-server enable traps '
                yield str(environment.getattr(l_1_snmp_trap, 'name'))
                yield '\n'
        l_1_snmp_trap = missing
        if t_4(environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'vrfs')):
            pass
            for l_1_vrf in environment.getattr((undefined(name='snmp_server') if l_0_snmp_server is missing else l_0_snmp_server), 'vrfs'):
                _loop_vars = {}
                pass
                if t_4(environment.getattr(l_1_vrf, 'enable'), True):
                    pass
                    yield 'snmp-server vrf '
                    yield str(environment.getattr(l_1_vrf, 'name'))
                    yield '\n'
                else:
                    pass
                    yield 'no snmp-server vrf '
                    yield str(environment.getattr(l_1_vrf, 'name'))
                    yield '\n'
            l_1_vrf = missing

blocks = {}
debug_info = '2=36&4=39&5=42&7=44&8=47&10=49&11=52&13=54&14=56&15=60&16=62&17=64&18=66&20=68&21=70&25=73&26=75&27=79&28=81&29=83&31=85&34=88&35=90&36=94&37=96&38=98&40=100&43=103&44=105&45=109&46=111&47=113&49=115&50=117&53=120&54=122&55=126&56=128&58=130&59=132&61=134&62=136&63=138&64=140&66=142&69=145&70=147&71=151&72=153&73=155&75=157&76=159&78=163&80=165&81=167&83=169&84=171&86=173&89=176&90=178&91=182&92=184&94=186&95=188&97=190&98=192&100=194&101=196&103=198&104=200&106=202&107=204&109=206&112=209&113=211&114=215&115=217&117=219&118=221&120=223&121=225&122=227&123=229&126=231&127=233&129=235&132=237&133=239&135=241&136=243&138=245&141=247&144=250&145=252&146=256&147=258&148=260&149=262&151=264&153=266&154=269&156=271&159=278&161=280&166=287&168=290&171=293&172=296&173=299&175=304&178=307&179=309&180=312&181=315&183=320'