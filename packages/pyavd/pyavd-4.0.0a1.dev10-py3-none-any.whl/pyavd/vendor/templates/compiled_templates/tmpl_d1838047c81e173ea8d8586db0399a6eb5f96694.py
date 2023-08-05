from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/logging.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_logging = resolve('logging')
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
        t_4 = environment.filters['upper']
    except KeyError:
        @internalcode
        def t_4(*unused):
            raise TemplateRuntimeError("No filter named 'upper' found.")
    try:
        t_5 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_5(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_5((undefined(name='logging') if l_0_logging is missing else l_0_logging)):
        pass
        yield '\n### Logging\n\n#### Logging Servers and Features Summary\n\n| Type | Level |\n| -----| ----- |\n'
        if t_5(environment.getattr((undefined(name='logging') if l_0_logging is missing else l_0_logging), 'console')):
            pass
            yield '| Console | '
            yield str(environment.getattr((undefined(name='logging') if l_0_logging is missing else l_0_logging), 'console'))
            yield ' |\n'
        if t_5(environment.getattr((undefined(name='logging') if l_0_logging is missing else l_0_logging), 'monitor')):
            pass
            yield '| Monitor | '
            yield str(environment.getattr((undefined(name='logging') if l_0_logging is missing else l_0_logging), 'monitor'))
            yield ' |\n'
        if t_5(environment.getattr((undefined(name='logging') if l_0_logging is missing else l_0_logging), 'buffered')):
            pass
            yield '| Buffer | '
            yield str(t_1(environment.getattr(environment.getattr((undefined(name='logging') if l_0_logging is missing else l_0_logging), 'buffered'), 'level'), '-'))
            yield ' |\n'
        if t_5(environment.getattr((undefined(name='logging') if l_0_logging is missing else l_0_logging), 'trap')):
            pass
            yield '| Trap | '
            yield str(environment.getattr((undefined(name='logging') if l_0_logging is missing else l_0_logging), 'trap'))
            yield ' |\n'
        if t_5(environment.getattr((undefined(name='logging') if l_0_logging is missing else l_0_logging), 'synchronous')):
            pass
            yield '| Synchronous | '
            yield str(t_1(environment.getattr(environment.getattr((undefined(name='logging') if l_0_logging is missing else l_0_logging), 'synchronous'), 'level'), 'critical'))
            yield ' |\n'
        if t_5(environment.getattr((undefined(name='logging') if l_0_logging is missing else l_0_logging), 'format')):
            pass
            yield '\n| Format Type | Setting |\n| ----------- | ------- |\n'
            if t_5(environment.getattr(environment.getattr((undefined(name='logging') if l_0_logging is missing else l_0_logging), 'format'), 'timestamp')):
                pass
                yield '| Timestamp | '
                yield str(environment.getattr(environment.getattr((undefined(name='logging') if l_0_logging is missing else l_0_logging), 'format'), 'timestamp'))
                yield ' |\n'
            if t_5(environment.getattr(environment.getattr((undefined(name='logging') if l_0_logging is missing else l_0_logging), 'format'), 'hostname')):
                pass
                yield '| Hostname | '
                yield str(environment.getattr(environment.getattr((undefined(name='logging') if l_0_logging is missing else l_0_logging), 'format'), 'hostname'))
                yield ' |\n'
            else:
                pass
                yield '| Hostname | hostname |\n'
            if t_5(environment.getattr(environment.getattr((undefined(name='logging') if l_0_logging is missing else l_0_logging), 'format'), 'sequence_numbers'), True):
                pass
                yield '| Sequence-numbers | true |\n'
            else:
                pass
                yield '| Sequence-numbers | false |\n'
        if t_5(environment.getattr((undefined(name='logging') if l_0_logging is missing else l_0_logging), 'vrfs')):
            pass
            yield '\n| VRF | Source Interface |\n| --- | ---------------- |\n'
            if t_5(environment.getattr((undefined(name='logging') if l_0_logging is missing else l_0_logging), 'source_interface')):
                pass
                yield '| - | '
                yield str(environment.getattr((undefined(name='logging') if l_0_logging is missing else l_0_logging), 'source_interface'))
                yield ' |\n'
            for l_1_vrf in t_2(environment.getattr((undefined(name='logging') if l_0_logging is missing else l_0_logging), 'vrfs'), 'name'):
                _loop_vars = {}
                pass
                if t_5(environment.getattr(l_1_vrf, 'source_interface')):
                    pass
                    yield '| '
                    yield str(environment.getattr(l_1_vrf, 'name'))
                    yield ' | '
                    yield str(environment.getattr(l_1_vrf, 'source_interface'))
                    yield ' |\n'
            l_1_vrf = missing
            yield '\n| VRF | Hosts | Ports | Protocol |\n| --- | ----- | ----- | -------- |\n'
            for l_1_vrf in t_2(environment.getattr((undefined(name='logging') if l_0_logging is missing else l_0_logging), 'vrfs'), 'name'):
                _loop_vars = {}
                pass
                if t_5(environment.getattr(l_1_vrf, 'hosts')):
                    pass
                    for l_2_host in t_2(environment.getattr(l_1_vrf, 'hosts'), 'name'):
                        _loop_vars = {}
                        pass
                        yield '| '
                        yield str(environment.getattr(l_1_vrf, 'name'))
                        yield ' | '
                        yield str(environment.getattr(l_2_host, 'name'))
                        yield ' | '
                        yield str(t_3(context.eval_ctx, t_1(environment.getattr(l_2_host, 'ports'), ['Default']), ', '))
                        yield ' | '
                        yield str(t_4(t_1(environment.getattr(l_2_host, 'protocol'), 'UDP')))
                        yield ' |\n'
                    l_2_host = missing
            l_1_vrf = missing
        if t_5(environment.getattr((undefined(name='logging') if l_0_logging is missing else l_0_logging), 'facility')):
            pass
            yield '\n**Syslog facility value:** '
            yield str(environment.getattr((undefined(name='logging') if l_0_logging is missing else l_0_logging), 'facility'))
            yield '\n'
        yield '\n#### Logging Servers and Features Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/logging.j2', 'documentation/logging.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '2=42&10=45&11=48&13=50&14=53&16=55&17=58&19=60&20=63&22=65&23=68&25=70&29=73&30=76&32=78&33=81&37=86&43=92&47=95&48=98&50=100&51=103&52=106&58=112&59=115&60=117&61=121&66=131&68=134&74=137'