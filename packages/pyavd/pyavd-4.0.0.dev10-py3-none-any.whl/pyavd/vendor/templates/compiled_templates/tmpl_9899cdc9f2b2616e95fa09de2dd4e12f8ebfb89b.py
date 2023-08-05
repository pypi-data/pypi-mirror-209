from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/boot.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_boot = resolve('boot')
    l_0_hash_algorithm = resolve('hash_algorithm')
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
    if t_2((undefined(name='boot') if l_0_boot is missing else l_0_boot)):
        pass
        yield '!\n'
        if t_2(environment.getattr(environment.getattr((undefined(name='boot') if l_0_boot is missing else l_0_boot), 'secret'), 'key')):
            pass
            if t_2(environment.getattr(environment.getattr((undefined(name='boot') if l_0_boot is missing else l_0_boot), 'secret'), 'hash_algorithm'), 'md5'):
                pass
                l_0_hash_algorithm = 5
                context.vars['hash_algorithm'] = l_0_hash_algorithm
                context.exported_vars.add('hash_algorithm')
            yield 'boot secret '
            yield str(t_1((undefined(name='hash_algorithm') if l_0_hash_algorithm is missing else l_0_hash_algorithm), 'sha512'))
            yield ' '
            yield str(environment.getattr(environment.getattr((undefined(name='boot') if l_0_boot is missing else l_0_boot), 'secret'), 'key'))
            yield '\n'

blocks = {}
debug_info = '2=25&4=28&5=30&6=32&8=36'