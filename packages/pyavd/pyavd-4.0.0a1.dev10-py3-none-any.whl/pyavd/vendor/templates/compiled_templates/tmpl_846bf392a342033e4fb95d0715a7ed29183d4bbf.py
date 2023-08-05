from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/ip-hardware.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_ip_hardware = resolve('ip_hardware')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_1(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='ip_hardware') if l_0_ip_hardware is missing else l_0_ip_hardware), 'fib'), 'optimize'), 'prefixes'), 'profile')):
        pass
        yield 'ip hardware fib optimize prefixes profile '
        yield str(environment.getattr(environment.getattr(environment.getattr(environment.getattr((undefined(name='ip_hardware') if l_0_ip_hardware is missing else l_0_ip_hardware), 'fib'), 'optimize'), 'prefixes'), 'profile'))
        yield '\n'

blocks = {}
debug_info = '2=18&3=21'