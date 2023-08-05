from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/aaa-root.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_aaa_root = resolve('aaa_root')
    l_0_generate_default_config = resolve('generate_default_config')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_1((undefined(name='aaa_root') if l_0_aaa_root is missing else l_0_aaa_root)):
        pass
        if t_1(environment.getattr(environment.getattr((undefined(name='aaa_root') if l_0_aaa_root is missing else l_0_aaa_root), 'secret'), 'sha512_password')):
            pass
            yield 'aaa root secret sha512 '
            yield str(environment.getattr(environment.getattr((undefined(name='aaa_root') if l_0_aaa_root is missing else l_0_aaa_root), 'secret'), 'sha512_password'))
            yield '\n'
    elif (not t_1((undefined(name='generate_default_config') if l_0_generate_default_config is missing else l_0_generate_default_config), False)):
        pass
        yield 'no aaa root\n'

blocks = {}
debug_info = '2=19&3=21&4=24&6=26'