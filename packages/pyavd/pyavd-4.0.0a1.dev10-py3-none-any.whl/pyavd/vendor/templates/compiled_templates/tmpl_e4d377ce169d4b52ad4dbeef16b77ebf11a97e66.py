from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/monitor-sessions.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_monitor_sessions = resolve('monitor_sessions')
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
    pass
    if t_2((undefined(name='monitor_sessions') if l_0_monitor_sessions is missing else l_0_monitor_sessions)):
        pass
        yield '!\n'
        def t_3(fiter):
            for l_1_monitor_session in fiter:
                if t_2(environment.getattr(l_1_monitor_session, 'name')):
                    yield l_1_monitor_session
        for l_1_monitor_session in t_3(t_1((undefined(name='monitor_sessions') if l_0_monitor_sessions is missing else l_0_monitor_sessions), 'name')):
            l_1_truncate_cli = resolve('truncate_cli')
            _loop_vars = {}
            pass
            if (t_2(environment.getattr(l_1_monitor_session, 'sources')) and t_2(environment.getattr(l_1_monitor_session, 'destinations'))):
                pass
                def t_4(fiter):
                    for l_2_source in fiter:
                        if t_2(environment.getattr(l_2_source, 'name')):
                            yield l_2_source
                for l_2_source in t_4(t_1(environment.getattr(l_1_monitor_session, 'sources'), 'name')):
                    l_2_source_cli = missing
                    _loop_vars = {}
                    pass
                    l_2_source_cli = str_join(('monitor session ', environment.getattr(l_1_monitor_session, 'name'), ' source ', environment.getattr(l_2_source, 'name'), ))
                    _loop_vars['source_cli'] = l_2_source_cli
                    if t_2(environment.getattr(l_2_source, 'direction')):
                        pass
                        l_2_source_cli = str_join(((undefined(name='source_cli') if l_2_source_cli is missing else l_2_source_cli), ' ', environment.getattr(l_2_source, 'direction'), ))
                        _loop_vars['source_cli'] = l_2_source_cli
                    if (t_2(environment.getattr(environment.getattr(l_2_source, 'access_group'), 'type')) and t_2(environment.getattr(environment.getattr(l_2_source, 'access_group'), 'name'))):
                        pass
                        l_2_source_cli = str_join(((undefined(name='source_cli') if l_2_source_cli is missing else l_2_source_cli), ' ', environment.getattr(environment.getattr(l_2_source, 'access_group'), 'type'), ' access-group ', environment.getattr(environment.getattr(l_2_source, 'access_group'), 'name'), ))
                        _loop_vars['source_cli'] = l_2_source_cli
                        if t_2(environment.getattr(environment.getattr(l_2_source, 'access_group'), 'priority')):
                            pass
                            l_2_source_cli = str_join(((undefined(name='source_cli') if l_2_source_cli is missing else l_2_source_cli), ' priority ', environment.getattr(environment.getattr(l_2_source, 'access_group'), 'priority'), ))
                            _loop_vars['source_cli'] = l_2_source_cli
                    yield str((undefined(name='source_cli') if l_2_source_cli is missing else l_2_source_cli))
                    yield '\n'
                l_2_source = l_2_source_cli = missing
                for l_2_destination in t_1(environment.getattr(l_1_monitor_session, 'destinations')):
                    _loop_vars = {}
                    pass
                    yield 'monitor session '
                    yield str(environment.getattr(l_1_monitor_session, 'name'))
                    yield ' destination '
                    yield str(l_2_destination)
                    yield '\n'
                l_2_destination = missing
                if t_2(environment.getattr(l_1_monitor_session, 'encapsulation_gre_metadata_tx'), True):
                    pass
                    yield 'monitor session '
                    yield str(environment.getattr(l_1_monitor_session, 'name'))
                    yield ' encapsulation gre metadata tx\n'
                if t_2(environment.getattr(l_1_monitor_session, 'header_remove_size')):
                    pass
                    yield 'monitor session '
                    yield str(environment.getattr(l_1_monitor_session, 'name'))
                    yield ' header remove size '
                    yield str(environment.getattr(l_1_monitor_session, 'header_remove_size'))
                    yield '\n'
                if (t_2(environment.getattr(environment.getattr(l_1_monitor_session, 'access_group'), 'type')) and t_2(environment.getattr(environment.getattr(l_1_monitor_session, 'access_group'), 'name'))):
                    pass
                    yield 'monitor session '
                    yield str(environment.getattr(l_1_monitor_session, 'name'))
                    yield ' '
                    yield str(environment.getattr(environment.getattr(l_1_monitor_session, 'access_group'), 'type'))
                    yield ' access-group '
                    yield str(environment.getattr(environment.getattr(l_1_monitor_session, 'access_group'), 'name'))
                    yield '\n'
                if t_2(environment.getattr(l_1_monitor_session, 'rate_limit_per_ingress_chip')):
                    pass
                    yield 'monitor session '
                    yield str(environment.getattr(l_1_monitor_session, 'name'))
                    yield ' rate-limit per-ingress-chip '
                    yield str(environment.getattr(l_1_monitor_session, 'rate_limit_per_ingress_chip'))
                    yield '\n'
                if t_2(environment.getattr(l_1_monitor_session, 'rate_limit_per_egress_chip')):
                    pass
                    yield 'monitor session '
                    yield str(environment.getattr(l_1_monitor_session, 'name'))
                    yield ' rate-limit per-egress-chip '
                    yield str(environment.getattr(l_1_monitor_session, 'rate_limit_per_egress_chip'))
                    yield '\n'
                if t_2(environment.getattr(l_1_monitor_session, 'sample')):
                    pass
                    yield 'monitor session '
                    yield str(environment.getattr(l_1_monitor_session, 'name'))
                    yield ' sample '
                    yield str(environment.getattr(l_1_monitor_session, 'sample'))
                    yield '\n'
                if t_2(environment.getattr(environment.getattr(l_1_monitor_session, 'truncate'), 'enabled'), True):
                    pass
                    l_1_truncate_cli = str_join(('monitor session ', environment.getattr(l_1_monitor_session, 'name'), ' truncate', ))
                    _loop_vars['truncate_cli'] = l_1_truncate_cli
                    if t_2(environment.getattr(environment.getattr(l_1_monitor_session, 'truncate'), 'size')):
                        pass
                        l_1_truncate_cli = str_join(((undefined(name='truncate_cli') if l_1_truncate_cli is missing else l_1_truncate_cli), ' size ', environment.getattr(environment.getattr(l_1_monitor_session, 'truncate'), 'size'), ))
                        _loop_vars['truncate_cli'] = l_1_truncate_cli
                    yield str((undefined(name='truncate_cli') if l_1_truncate_cli is missing else l_1_truncate_cli))
                    yield '\n'
        l_1_monitor_session = l_1_truncate_cli = missing

blocks = {}
debug_info = '2=24&4=27&5=35&6=37&7=45&8=47&9=49&11=51&12=53&13=55&14=57&17=59&19=62&20=66&22=71&23=74&25=76&26=79&28=83&29=86&31=92&32=95&34=99&35=102&37=106&38=109&40=113&41=115&42=117&43=119&45=121'