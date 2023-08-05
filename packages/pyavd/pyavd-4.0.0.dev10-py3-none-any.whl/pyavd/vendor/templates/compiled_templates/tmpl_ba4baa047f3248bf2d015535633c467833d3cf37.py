from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/ip-igmp-snooping.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_ip_igmp_snooping = resolve('ip_igmp_snooping')
    l_0_proxy_cli = resolve('proxy_cli')
    try:
        t_1 = environment.filters['arista.avd.natural_sort']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.natural_sort' found.")
    try:
        t_2 = environment.filters['join']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No filter named 'join' found.")
    try:
        t_3 = environment.filters['length']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No filter named 'length' found.")
    try:
        t_4 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_4(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if (t_4((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping)) and ((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping) != {'globally_enabled': True})):
        pass
        yield '!\n'
        if t_4(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'globally_enabled'), False):
            pass
            yield 'no ip igmp snooping\n'
        else:
            pass
            l_0_proxy_cli = []
            context.vars['proxy_cli'] = l_0_proxy_cli
            context.exported_vars.add('proxy_cli')
            if t_4(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'proxy'), True):
                pass
                context.call(environment.getattr((undefined(name='proxy_cli') if l_0_proxy_cli is missing else l_0_proxy_cli), 'append'), 'ip igmp snooping proxy')
            if t_4(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'robustness_variable')):
                pass
                yield 'ip igmp snooping robustness-variable '
                yield str(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'robustness_variable'))
                yield '\n'
            if t_4(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'restart_query_interval')):
                pass
                yield 'ip igmp snooping restart query-interval '
                yield str(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'restart_query_interval'))
                yield '\n'
            if t_4(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'interface_restart_query')):
                pass
                yield 'ip igmp snooping interface-restart-query '
                yield str(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'interface_restart_query'))
                yield '\n'
            if t_4(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'fast_leave'), False):
                pass
                yield 'no ip igmp snooping fast-leave\n'
            elif t_4(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'fast_leave'), True):
                pass
                yield 'ip igmp snooping fast-leave\n'
            if t_4(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'vlans')):
                pass
                for l_1_vlan in t_1(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'vlans'), 'id'):
                    _loop_vars = {}
                    pass
                    if t_4(environment.getattr(l_1_vlan, 'enabled'), False):
                        pass
                        yield 'no ip igmp snooping vlan '
                        yield str(environment.getattr(l_1_vlan, 'id'))
                        yield '\n'
                    elif t_4(environment.getattr(l_1_vlan, 'enabled'), True):
                        pass
                        yield 'ip igmp snooping vlan '
                        yield str(environment.getattr(l_1_vlan, 'id'))
                        yield '\n'
                    if t_4(environment.getattr(l_1_vlan, 'querier')):
                        pass
                        if t_4(environment.getattr(environment.getattr(l_1_vlan, 'querier'), 'enabled'), True):
                            pass
                            yield 'ip igmp snooping vlan '
                            yield str(environment.getattr(l_1_vlan, 'id'))
                            yield ' querier\n'
                        elif t_4(environment.getattr(environment.getattr(l_1_vlan, 'querier'), 'enabled'), False):
                            pass
                            yield 'no ip igmp snooping vlan '
                            yield str(environment.getattr(l_1_vlan, 'id'))
                            yield ' querier\n'
                        if t_4(environment.getattr(environment.getattr(l_1_vlan, 'querier'), 'address')):
                            pass
                            yield 'ip igmp snooping vlan '
                            yield str(environment.getattr(l_1_vlan, 'id'))
                            yield ' querier address '
                            yield str(environment.getattr(environment.getattr(l_1_vlan, 'querier'), 'address'))
                            yield '\n'
                        if t_4(environment.getattr(environment.getattr(l_1_vlan, 'querier'), 'query_interval')):
                            pass
                            yield 'ip igmp snooping vlan '
                            yield str(environment.getattr(l_1_vlan, 'id'))
                            yield ' querier query-interval '
                            yield str(environment.getattr(environment.getattr(l_1_vlan, 'querier'), 'query_interval'))
                            yield '\n'
                        if t_4(environment.getattr(environment.getattr(l_1_vlan, 'querier'), 'max_response_time')):
                            pass
                            yield 'ip igmp snooping vlan '
                            yield str(environment.getattr(l_1_vlan, 'id'))
                            yield ' querier max-response-time '
                            yield str(environment.getattr(environment.getattr(l_1_vlan, 'querier'), 'max_response_time'))
                            yield '\n'
                        if t_4(environment.getattr(environment.getattr(l_1_vlan, 'querier'), 'last_member_query_interval')):
                            pass
                            yield 'ip igmp snooping vlan '
                            yield str(environment.getattr(l_1_vlan, 'id'))
                            yield ' querier last-member-query-interval '
                            yield str(environment.getattr(environment.getattr(l_1_vlan, 'querier'), 'last_member_query_interval'))
                            yield '\n'
                        if t_4(environment.getattr(environment.getattr(l_1_vlan, 'querier'), 'last_member_query_count')):
                            pass
                            yield 'ip igmp snooping vlan '
                            yield str(environment.getattr(l_1_vlan, 'id'))
                            yield ' querier last-member-query-count '
                            yield str(environment.getattr(environment.getattr(l_1_vlan, 'querier'), 'last_member_query_count'))
                            yield '\n'
                        if t_4(environment.getattr(environment.getattr(l_1_vlan, 'querier'), 'startup_query_interval')):
                            pass
                            yield 'ip igmp snooping vlan '
                            yield str(environment.getattr(l_1_vlan, 'id'))
                            yield ' querier startup-query-interval '
                            yield str(environment.getattr(environment.getattr(l_1_vlan, 'querier'), 'startup_query_interval'))
                            yield '\n'
                        if t_4(environment.getattr(environment.getattr(l_1_vlan, 'querier'), 'startup_query_count')):
                            pass
                            yield 'ip igmp snooping vlan '
                            yield str(environment.getattr(l_1_vlan, 'id'))
                            yield ' querier startup-query-count '
                            yield str(environment.getattr(environment.getattr(l_1_vlan, 'querier'), 'startup_query_count'))
                            yield '\n'
                        if t_4(environment.getattr(environment.getattr(l_1_vlan, 'querier'), 'version')):
                            pass
                            yield 'ip igmp snooping vlan '
                            yield str(environment.getattr(l_1_vlan, 'id'))
                            yield ' querier version '
                            yield str(environment.getattr(environment.getattr(l_1_vlan, 'querier'), 'version'))
                            yield '\n'
                    if t_4(environment.getattr(l_1_vlan, 'max_groups')):
                        pass
                        yield 'ip igmp snooping vlan '
                        yield str(environment.getattr(l_1_vlan, 'id'))
                        yield ' max-groups '
                        yield str(environment.getattr(l_1_vlan, 'max_groups'))
                        yield '\n'
                    if t_4(environment.getattr(l_1_vlan, 'fast_leave'), True):
                        pass
                        yield 'ip igmp snooping vlan '
                        yield str(environment.getattr(l_1_vlan, 'id'))
                        yield ' fast-leave\n'
                    elif t_4(environment.getattr(l_1_vlan, 'fast_leave'), False):
                        pass
                        yield 'no ip igmp snooping vlan '
                        yield str(environment.getattr(l_1_vlan, 'id'))
                        yield ' fast-leave\n'
                    if t_4(environment.getattr(l_1_vlan, 'proxy'), True):
                        pass
                        context.call(environment.getattr((undefined(name='proxy_cli') if l_0_proxy_cli is missing else l_0_proxy_cli), 'append'), str_join(('ip igmp snooping vlan ', environment.getattr(l_1_vlan, 'id'), ' proxy', )), _loop_vars=_loop_vars)
                    elif t_4(environment.getattr(l_1_vlan, 'proxy'), False):
                        pass
                        context.call(environment.getattr((undefined(name='proxy_cli') if l_0_proxy_cli is missing else l_0_proxy_cli), 'append'), str_join(('no ip igmp snooping vlan ', environment.getattr(l_1_vlan, 'id'), ' proxy', )), _loop_vars=_loop_vars)
                l_1_vlan = missing
            if t_4(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'querier')):
                pass
                if t_4(environment.getattr(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'querier'), 'enabled'), True):
                    pass
                    yield 'ip igmp snooping querier\n'
                elif t_4(environment.getattr(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'querier'), 'enabled'), False):
                    pass
                    yield 'no ip igmp snooping querier\n'
                if t_4(environment.getattr(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'querier'), 'address')):
                    pass
                    yield 'ip igmp snooping querier address '
                    yield str(environment.getattr(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'querier'), 'address'))
                    yield '\n'
                if t_4(environment.getattr(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'querier'), 'query_interval')):
                    pass
                    yield 'ip igmp snooping querier query-interval '
                    yield str(environment.getattr(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'querier'), 'query_interval'))
                    yield '\n'
                if t_4(environment.getattr(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'querier'), 'max_response_time')):
                    pass
                    yield 'ip igmp snooping querier max-response-time '
                    yield str(environment.getattr(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'querier'), 'max_response_time'))
                    yield '\n'
                if t_4(environment.getattr(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'querier'), 'last_member_query_interval')):
                    pass
                    yield 'ip igmp snooping querier last-member-query-interval '
                    yield str(environment.getattr(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'querier'), 'last_member_query_interval'))
                    yield '\n'
                if t_4(environment.getattr(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'querier'), 'last_member_query_count')):
                    pass
                    yield 'ip igmp snooping querier last-member-query-count '
                    yield str(environment.getattr(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'querier'), 'last_member_query_count'))
                    yield '\n'
                if t_4(environment.getattr(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'querier'), 'startup_query_interval')):
                    pass
                    yield 'ip igmp snooping querier startup-query-interval '
                    yield str(environment.getattr(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'querier'), 'startup_query_interval'))
                    yield '\n'
                if t_4(environment.getattr(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'querier'), 'startup_query_count')):
                    pass
                    yield 'ip igmp snooping querier startup-query-count '
                    yield str(environment.getattr(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'querier'), 'startup_query_count'))
                    yield '\n'
                if t_4(environment.getattr(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'querier'), 'version')):
                    pass
                    yield 'ip igmp snooping querier version '
                    yield str(environment.getattr(environment.getattr((undefined(name='ip_igmp_snooping') if l_0_ip_igmp_snooping is missing else l_0_ip_igmp_snooping), 'querier'), 'version'))
                    yield '\n'
            if (t_3((undefined(name='proxy_cli') if l_0_proxy_cli is missing else l_0_proxy_cli)) > 0):
                pass
                yield '!\n'
                yield str(t_2(context.eval_ctx, (undefined(name='proxy_cli') if l_0_proxy_cli is missing else l_0_proxy_cli), '\n'))
                yield '\n'

blocks = {}
debug_info = '2=37&4=40&7=45&8=48&9=50&11=51&12=54&14=56&15=59&17=61&18=64&20=66&22=69&25=72&26=74&27=77&28=80&29=82&30=85&32=87&33=89&34=92&35=94&36=97&38=99&39=102&41=106&42=109&44=113&45=116&47=120&48=123&50=127&51=130&53=134&54=137&56=141&57=144&59=148&60=151&63=155&64=158&66=162&67=165&68=167&69=170&71=172&72=174&73=175&74=177&78=179&79=181&81=184&84=187&85=190&87=192&88=195&90=197&91=200&93=202&94=205&96=207&97=210&99=212&100=215&102=217&103=220&105=222&106=225&109=227&111=230'