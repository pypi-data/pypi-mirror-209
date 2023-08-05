from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/arp.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_arp = resolve('arp')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_1(environment.getattr(environment.getattr((undefined(name='arp') if l_0_arp is missing else l_0_arp), 'aging'), 'timeout_default')):
        pass
        yield '\n### ARP\n\nGlobal ARP timeout: '
        yield str(environment.getattr(environment.getattr((undefined(name='arp') if l_0_arp is missing else l_0_arp), 'aging'), 'timeout_default'))
        yield '\n'

blocks = {}
debug_info = '2=18&6=21'