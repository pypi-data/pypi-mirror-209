from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/terminal.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_terminal = resolve('terminal')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_1((undefined(name='terminal') if l_0_terminal is missing else l_0_terminal)):
        pass
        yield '!\n'
        if t_1(environment.getattr((undefined(name='terminal') if l_0_terminal is missing else l_0_terminal), 'width')):
            pass
            yield 'terminal width '
            yield str(environment.getattr((undefined(name='terminal') if l_0_terminal is missing else l_0_terminal), 'width'))
            yield '\n'
        if t_1(environment.getattr((undefined(name='terminal') if l_0_terminal is missing else l_0_terminal), 'length')):
            pass
            yield 'terminal length '
            yield str(environment.getattr((undefined(name='terminal') if l_0_terminal is missing else l_0_terminal), 'length'))
            yield '\n'

blocks = {}
debug_info = '2=18&4=21&5=24&7=26&8=29'