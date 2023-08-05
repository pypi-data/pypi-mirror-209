from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/flow-trackings.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_flow_trackings = resolve('flow_trackings')
    try:
        t_1 = environment.filters['arista.avd.default']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.default' found.")
    try:
        t_2 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    for l_1_flow_tracking in t_1((undefined(name='flow_trackings') if l_0_flow_trackings is missing else l_0_flow_trackings), []):
        _loop_vars = {}
        pass
        yield '!\nflow tracking '
        yield str(environment.getattr(l_1_flow_tracking, 'type'))
        yield '\n'
        if t_2(environment.getattr(l_1_flow_tracking, 'sample')):
            pass
            yield '   sample '
            yield str(environment.getattr(l_1_flow_tracking, 'sample'))
            yield '\n'
        for l_2_tracker in environment.getattr(l_1_flow_tracking, 'trackers'):
            _loop_vars = {}
            pass
            yield '   tracker '
            yield str(environment.getattr(l_2_tracker, 'name'))
            yield '\n'
            if t_2(environment.getattr(environment.getattr(l_2_tracker, 'record_export'), 'on_inactive_timeout')):
                pass
                yield '      record export on inactive timeout '
                yield str(environment.getattr(environment.getattr(l_2_tracker, 'record_export'), 'on_inactive_timeout'))
                yield '\n'
            if t_2(environment.getattr(environment.getattr(l_2_tracker, 'record_export'), 'on_interval')):
                pass
                yield '      record export on interval '
                yield str(environment.getattr(environment.getattr(l_2_tracker, 'record_export'), 'on_interval'))
                yield '\n'
            if t_2(environment.getattr(environment.getattr(l_2_tracker, 'record_export'), 'mpls'), True):
                pass
                yield '      record export mpls\n'
            if t_2(environment.getattr(l_2_tracker, 'exporters')):
                pass
                for l_3_exporter in environment.getattr(l_2_tracker, 'exporters'):
                    l_3_collector_cli = resolve('collector_cli')
                    _loop_vars = {}
                    pass
                    yield '      exporter '
                    yield str(environment.getattr(l_3_exporter, 'name'))
                    yield '\n'
                    if t_2(environment.getattr(environment.getattr(l_3_exporter, 'collector'), 'host')):
                        pass
                        l_3_collector_cli = str_join(('collector ', environment.getattr(environment.getattr(l_3_exporter, 'collector'), 'host'), ))
                        _loop_vars['collector_cli'] = l_3_collector_cli
                        if t_2(environment.getattr(environment.getattr(l_3_exporter, 'collector'), 'port')):
                            pass
                            l_3_collector_cli = str_join(((undefined(name='collector_cli') if l_3_collector_cli is missing else l_3_collector_cli), ' port ', environment.getattr(environment.getattr(l_3_exporter, 'collector'), 'port'), ))
                            _loop_vars['collector_cli'] = l_3_collector_cli
                        yield '         '
                        yield str((undefined(name='collector_cli') if l_3_collector_cli is missing else l_3_collector_cli))
                        yield '\n'
                    if t_2(environment.getattr(environment.getattr(l_3_exporter, 'format'), 'ipfix_version')):
                        pass
                        yield '         format ipfix version '
                        yield str(environment.getattr(environment.getattr(l_3_exporter, 'format'), 'ipfix_version'))
                        yield '\n'
                    if t_2(environment.getattr(l_3_exporter, 'local_interface')):
                        pass
                        yield '         local interface '
                        yield str(environment.getattr(l_3_exporter, 'local_interface'))
                        yield '\n'
                    if t_2(environment.getattr(l_3_exporter, 'template_interval')):
                        pass
                        yield '         template interval '
                        yield str(environment.getattr(l_3_exporter, 'template_interval'))
                        yield '\n'
                l_3_exporter = l_3_collector_cli = missing
        l_2_tracker = missing
        if t_2(environment.getattr(l_1_flow_tracking, 'shutdown'), False):
            pass
            yield '   no shutdown\n'
    l_1_flow_tracking = missing

blocks = {}
debug_info = '2=24&4=28&5=30&6=33&8=35&9=39&10=41&11=44&13=46&14=49&16=51&19=54&20=56&21=61&22=63&23=65&24=67&25=69&27=72&29=74&30=77&32=79&33=82&35=84&36=87&41=91'