from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/queue-monitor-length.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_queue_monitor_length = resolve('queue_monitor_length')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if (t_1((undefined(name='queue_monitor_length') if l_0_queue_monitor_length is missing else l_0_queue_monitor_length)) and (not t_1(environment.getattr((undefined(name='queue_monitor_length') if l_0_queue_monitor_length is missing else l_0_queue_monitor_length), 'enabled'), False))):
        pass
        yield '!\nqueue-monitor length\n'
        if t_1(environment.getattr((undefined(name='queue_monitor_length') if l_0_queue_monitor_length is missing else l_0_queue_monitor_length), 'log')):
            pass
            yield 'queue-monitor length log '
            yield str(environment.getattr((undefined(name='queue_monitor_length') if l_0_queue_monitor_length is missing else l_0_queue_monitor_length), 'log'))
            yield '\n'
        if t_1(environment.getattr((undefined(name='queue_monitor_length') if l_0_queue_monitor_length is missing else l_0_queue_monitor_length), 'notifying'), True):
            pass
            yield 'queue-monitor length notifying\n'
        elif t_1(environment.getattr((undefined(name='queue_monitor_length') if l_0_queue_monitor_length is missing else l_0_queue_monitor_length), 'notifying'), False):
            pass
            yield 'no queue-monitor length notifying\n'
        if t_1(environment.getattr(environment.getattr(environment.getattr((undefined(name='queue_monitor_length') if l_0_queue_monitor_length is missing else l_0_queue_monitor_length), 'cpu'), 'thresholds'), 'high')):
            pass
            if t_1(environment.getattr(environment.getattr(environment.getattr((undefined(name='queue_monitor_length') if l_0_queue_monitor_length is missing else l_0_queue_monitor_length), 'cpu'), 'thresholds'), 'low')):
                pass
                yield 'queue-monitor length cpu thresholds '
                yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='queue_monitor_length') if l_0_queue_monitor_length is missing else l_0_queue_monitor_length), 'cpu'), 'thresholds'), 'high'))
                yield ' '
                yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='queue_monitor_length') if l_0_queue_monitor_length is missing else l_0_queue_monitor_length), 'cpu'), 'thresholds'), 'low'))
                yield '\n'
            else:
                pass
                yield 'queue-monitor length cpu threshold '
                yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='queue_monitor_length') if l_0_queue_monitor_length is missing else l_0_queue_monitor_length), 'cpu'), 'thresholds'), 'high'))
                yield '\n'

blocks = {}
debug_info = '2=18&5=21&6=24&8=26&10=29&13=32&14=34&15=37&17=44'