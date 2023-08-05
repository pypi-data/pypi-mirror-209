from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/enable-password.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_enable_password = resolve('enable_password')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_1((undefined(name='enable_password') if l_0_enable_password is missing else l_0_enable_password)):
        pass
        yield '\n### Enable Password\n\n'
        if t_1(environment.getattr((undefined(name='enable_password') if l_0_enable_password is missing else l_0_enable_password), 'key')):
            pass
            if t_1(environment.getattr((undefined(name='enable_password') if l_0_enable_password is missing else l_0_enable_password), 'hash_algorithm'), 'md5'):
                pass
                yield 'md5 encrypted enable password is configured\n'
            elif t_1(environment.getattr((undefined(name='enable_password') if l_0_enable_password is missing else l_0_enable_password), 'hash_algorithm'), 'sha512'):
                pass
                yield 'sha512 encrypted enable password is configured\n'
            yield '#### Enable password configuration\n\n```eos\n'
            template = environment.get_template('eos/enable-password.j2', 'documentation/enable-password.j2')
            for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
                yield event
            yield '!\n```\n'

blocks = {}
debug_info = '2=18&6=21&7=23&9=26&15=30'