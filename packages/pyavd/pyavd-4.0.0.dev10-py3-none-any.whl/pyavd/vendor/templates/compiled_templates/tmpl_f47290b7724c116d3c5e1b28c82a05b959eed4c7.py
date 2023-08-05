from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/enable-password.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_enable_password = resolve('enable_password')
    l_0_generate_default_config = resolve('generate_default_config')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_1((undefined(name='enable_password') if l_0_enable_password is missing else l_0_enable_password)):
        pass
        if t_1(environment.getattr((undefined(name='enable_password') if l_0_enable_password is missing else l_0_enable_password), 'key')):
            pass
            yield '!\n'
            if t_1(environment.getattr((undefined(name='enable_password') if l_0_enable_password is missing else l_0_enable_password), 'hash_algorithm'), 'md5'):
                pass
                yield 'enable password 5 '
                yield str(environment.getattr((undefined(name='enable_password') if l_0_enable_password is missing else l_0_enable_password), 'key'))
                yield '\n'
            elif t_1(environment.getattr((undefined(name='enable_password') if l_0_enable_password is missing else l_0_enable_password), 'hash_algorithm'), 'sha512'):
                pass
                yield 'enable password sha512 '
                yield str(environment.getattr((undefined(name='enable_password') if l_0_enable_password is missing else l_0_enable_password), 'key'))
                yield '\n'
    elif (not t_1((undefined(name='generate_default_config') if l_0_generate_default_config is missing else l_0_generate_default_config), False)):
        pass
        yield '!\nno enable password\n'

blocks = {}
debug_info = '2=19&3=21&5=24&6=27&7=29&8=32&11=34'