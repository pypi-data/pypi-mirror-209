from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/logging.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_logging = resolve('logging')
    l_0_logging_buffered_cli = resolve('logging_buffered_cli')
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
        t_4 = environment.filters['lower']
    except KeyError:
        @internalcode
        def t_4(*unused):
            raise TemplateRuntimeError("No filter named 'lower' found.")
    try:
        t_5 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_5(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_5((undefined(name='logging') if l_0_logging is missing else l_0_logging)):
        pass
        yield '!\n'
        if t_5(environment.getattr(environment.getattr((undefined(name='logging') if l_0_logging is missing else l_0_logging), 'buffered'), 'level'), 'disabled'):
            pass
            yield 'no logging buffered\n'
        elif (t_5(environment.getattr(environment.getattr((undefined(name='logging') if l_0_logging is missing else l_0_logging), 'buffered'), 'size')) or t_5(environment.getattr(environment.getattr((undefined(name='logging') if l_0_logging is missing else l_0_logging), 'buffered'), 'level'))):
            pass
            l_0_logging_buffered_cli = 'logging buffered'
            context.vars['logging_buffered_cli'] = l_0_logging_buffered_cli
            context.exported_vars.add('logging_buffered_cli')
            if t_5(environment.getattr(environment.getattr((undefined(name='logging') if l_0_logging is missing else l_0_logging), 'buffered'), 'size')):
                pass
                l_0_logging_buffered_cli = str_join(((undefined(name='logging_buffered_cli') if l_0_logging_buffered_cli is missing else l_0_logging_buffered_cli), ' ', environment.getattr(environment.getattr((undefined(name='logging') if l_0_logging is missing else l_0_logging), 'buffered'), 'size'), ))
                context.vars['logging_buffered_cli'] = l_0_logging_buffered_cli
                context.exported_vars.add('logging_buffered_cli')
            if t_5(environment.getattr(environment.getattr((undefined(name='logging') if l_0_logging is missing else l_0_logging), 'buffered'), 'level')):
                pass
                l_0_logging_buffered_cli = str_join(((undefined(name='logging_buffered_cli') if l_0_logging_buffered_cli is missing else l_0_logging_buffered_cli), ' ', environment.getattr(environment.getattr((undefined(name='logging') if l_0_logging is missing else l_0_logging), 'buffered'), 'level'), ))
                context.vars['logging_buffered_cli'] = l_0_logging_buffered_cli
                context.exported_vars.add('logging_buffered_cli')
            yield str((undefined(name='logging_buffered_cli') if l_0_logging_buffered_cli is missing else l_0_logging_buffered_cli))
            yield '\n'
        if t_5(environment.getattr((undefined(name='logging') if l_0_logging is missing else l_0_logging), 'trap'), 'disabled'):
            pass
            yield 'no logging trap\n'
        elif t_5(environment.getattr((undefined(name='logging') if l_0_logging is missing else l_0_logging), 'trap')):
            pass
            yield 'logging trap '
            yield str(environment.getattr((undefined(name='logging') if l_0_logging is missing else l_0_logging), 'trap'))
            yield '\n'
        if t_5(environment.getattr((undefined(name='logging') if l_0_logging is missing else l_0_logging), 'console'), 'disabled'):
            pass
            yield 'no logging console\n'
        elif t_5(environment.getattr((undefined(name='logging') if l_0_logging is missing else l_0_logging), 'console')):
            pass
            yield 'logging console '
            yield str(environment.getattr((undefined(name='logging') if l_0_logging is missing else l_0_logging), 'console'))
            yield '\n'
        if t_5(environment.getattr((undefined(name='logging') if l_0_logging is missing else l_0_logging), 'monitor'), 'disabled'):
            pass
            yield 'no logging monitor\n'
        elif t_5(environment.getattr((undefined(name='logging') if l_0_logging is missing else l_0_logging), 'monitor')):
            pass
            yield 'logging monitor '
            yield str(environment.getattr((undefined(name='logging') if l_0_logging is missing else l_0_logging), 'monitor'))
            yield '\n'
        if t_5(environment.getattr(environment.getattr((undefined(name='logging') if l_0_logging is missing else l_0_logging), 'synchronous'), 'level'), 'disabled'):
            pass
            yield 'no logging synchronous\n'
        elif t_5(environment.getattr((undefined(name='logging') if l_0_logging is missing else l_0_logging), 'synchronous')):
            pass
            yield 'logging synchronous level '
            yield str(t_1(environment.getattr(environment.getattr((undefined(name='logging') if l_0_logging is missing else l_0_logging), 'synchronous'), 'level'), 'critical'))
            yield '\n'
        for l_1_vrf in t_2(environment.getattr((undefined(name='logging') if l_0_logging is missing else l_0_logging), 'vrfs'), 'name'):
            _loop_vars = {}
            pass
            for l_2_host in t_2(environment.getattr(l_1_vrf, 'hosts'), 'name'):
                l_2_logging_host_cli = missing
                _loop_vars = {}
                pass
                l_2_logging_host_cli = 'logging'
                _loop_vars['logging_host_cli'] = l_2_logging_host_cli
                if (environment.getattr(l_1_vrf, 'name') != 'default'):
                    pass
                    l_2_logging_host_cli = str_join(((undefined(name='logging_host_cli') if l_2_logging_host_cli is missing else l_2_logging_host_cli), ' vrf ', environment.getattr(l_1_vrf, 'name'), ))
                    _loop_vars['logging_host_cli'] = l_2_logging_host_cli
                l_2_logging_host_cli = str_join(((undefined(name='logging_host_cli') if l_2_logging_host_cli is missing else l_2_logging_host_cli), ' host ', environment.getattr(l_2_host, 'name'), ))
                _loop_vars['logging_host_cli'] = l_2_logging_host_cli
                if t_5(environment.getattr(l_2_host, 'ports')):
                    pass
                    l_2_logging_host_cli = str_join(((undefined(name='logging_host_cli') if l_2_logging_host_cli is missing else l_2_logging_host_cli), ' ', t_3(context.eval_ctx, environment.getattr(l_2_host, 'ports'), ' '), ))
                    _loop_vars['logging_host_cli'] = l_2_logging_host_cli
                if (t_5(environment.getattr(l_2_host, 'protocol')) and (not t_5(environment.getattr(l_2_host, 'protocol'), 'udp'))):
                    pass
                    l_2_logging_host_cli = str_join(((undefined(name='logging_host_cli') if l_2_logging_host_cli is missing else l_2_logging_host_cli), ' protocol ', t_4(environment.getattr(l_2_host, 'protocol')), ))
                    _loop_vars['logging_host_cli'] = l_2_logging_host_cli
                yield str((undefined(name='logging_host_cli') if l_2_logging_host_cli is missing else l_2_logging_host_cli))
                yield '\n'
            l_2_host = l_2_logging_host_cli = missing
        l_1_vrf = missing
        if t_5(environment.getattr(environment.getattr((undefined(name='logging') if l_0_logging is missing else l_0_logging), 'format'), 'timestamp')):
            pass
            yield 'logging format timestamp '
            yield str(environment.getattr(environment.getattr((undefined(name='logging') if l_0_logging is missing else l_0_logging), 'format'), 'timestamp'))
            yield '\n'
        if t_5(environment.getattr(environment.getattr((undefined(name='logging') if l_0_logging is missing else l_0_logging), 'format'), 'hostname'), 'fqdn'):
            pass
            yield 'logging format hostname fqdn\n'
        elif t_5(environment.getattr(environment.getattr((undefined(name='logging') if l_0_logging is missing else l_0_logging), 'format'), 'hostname'), 'ipv4'):
            pass
            yield 'logging format hostname ipv4\n'
        if t_5(environment.getattr(environment.getattr((undefined(name='logging') if l_0_logging is missing else l_0_logging), 'format'), 'sequence_numbers'), True):
            pass
            yield 'logging format sequence-numbers\n'
        if t_5(environment.getattr((undefined(name='logging') if l_0_logging is missing else l_0_logging), 'facility')):
            pass
            yield 'logging facility '
            yield str(environment.getattr((undefined(name='logging') if l_0_logging is missing else l_0_logging), 'facility'))
            yield '\n'
        if t_5(environment.getattr((undefined(name='logging') if l_0_logging is missing else l_0_logging), 'source_interface')):
            pass
            yield 'logging source-interface '
            yield str(environment.getattr((undefined(name='logging') if l_0_logging is missing else l_0_logging), 'source_interface'))
            yield '\n'
        for l_1_vrf in t_2(environment.getattr((undefined(name='logging') if l_0_logging is missing else l_0_logging), 'vrfs'), 'name'):
            l_1_logging_cli = missing
            _loop_vars = {}
            pass
            l_1_logging_cli = 'logging'
            _loop_vars['logging_cli'] = l_1_logging_cli
            if t_5(environment.getattr(l_1_vrf, 'source_interface')):
                pass
                if (environment.getattr(l_1_vrf, 'name') != 'default'):
                    pass
                    l_1_logging_cli = str_join(((undefined(name='logging_cli') if l_1_logging_cli is missing else l_1_logging_cli), ' vrf ', environment.getattr(l_1_vrf, 'name'), ))
                    _loop_vars['logging_cli'] = l_1_logging_cli
                l_1_logging_cli = str_join(((undefined(name='logging_cli') if l_1_logging_cli is missing else l_1_logging_cli), ' source-interface ', environment.getattr(l_1_vrf, 'source_interface'), ))
                _loop_vars['logging_cli'] = l_1_logging_cli
                yield str((undefined(name='logging_cli') if l_1_logging_cli is missing else l_1_logging_cli))
                yield '\n'
        l_1_vrf = l_1_logging_cli = missing
        for l_1_match_list in t_2(environment.getattr(environment.getattr(environment.getattr((undefined(name='logging') if l_0_logging is missing else l_0_logging), 'policy'), 'match'), 'match_lists'), 'name'):
            _loop_vars = {}
            pass
            yield 'logging policy match match-list '
            yield str(environment.getattr(l_1_match_list, 'name'))
            yield ' '
            yield str(environment.getattr(l_1_match_list, 'action'))
            yield '\n'
        l_1_match_list = missing

blocks = {}
debug_info = '2=43&4=46&6=49&7=51&8=54&9=56&11=59&12=61&14=64&16=66&18=69&19=72&21=74&23=77&24=80&26=82&28=85&29=88&31=90&33=93&34=96&36=98&37=101&38=105&39=107&40=109&42=111&43=113&44=115&46=117&47=119&49=121&52=125&53=128&55=130&57=133&60=136&63=139&64=142&66=144&67=147&69=149&70=153&71=155&72=157&73=159&75=161&76=163&79=166&80=170'