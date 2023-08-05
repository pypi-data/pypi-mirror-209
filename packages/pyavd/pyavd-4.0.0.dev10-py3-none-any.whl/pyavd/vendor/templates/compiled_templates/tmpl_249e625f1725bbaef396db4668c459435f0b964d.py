from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/management-tech-support.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_management_tech_support = resolve('management_tech_support')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_1((undefined(name='management_tech_support') if l_0_management_tech_support is missing else l_0_management_tech_support)):
        pass
        yield '!\nmanagement tech-support\n'
        if t_1(environment.getattr((undefined(name='management_tech_support') if l_0_management_tech_support is missing else l_0_management_tech_support), 'policy_show_tech_support')):
            pass
            yield '   policy show tech-support\n'
            if t_1(environment.getattr(environment.getattr((undefined(name='management_tech_support') if l_0_management_tech_support is missing else l_0_management_tech_support), 'policy_show_tech_support'), 'exclude_commands')):
                pass
                for l_1_exclude_command in environment.getattr(environment.getattr((undefined(name='management_tech_support') if l_0_management_tech_support is missing else l_0_management_tech_support), 'policy_show_tech_support'), 'exclude_commands'):
                    l_1_exclude_cli = missing
                    _loop_vars = {}
                    pass
                    l_1_exclude_cli = ''
                    _loop_vars['exclude_cli'] = l_1_exclude_cli
                    if t_1(environment.getattr(l_1_exclude_command, 'type'), 'json'):
                        pass
                        l_1_exclude_cli = 'json '
                        _loop_vars['exclude_cli'] = l_1_exclude_cli
                    l_1_exclude_cli = str_join(((undefined(name='exclude_cli') if l_1_exclude_cli is missing else l_1_exclude_cli), environment.getattr(l_1_exclude_command, 'command'), ))
                    _loop_vars['exclude_cli'] = l_1_exclude_cli
                    yield '      exclude command '
                    yield str((undefined(name='exclude_cli') if l_1_exclude_cli is missing else l_1_exclude_cli))
                    yield '\n'
                l_1_exclude_command = l_1_exclude_cli = missing
            if t_1(environment.getattr(environment.getattr((undefined(name='management_tech_support') if l_0_management_tech_support is missing else l_0_management_tech_support), 'policy_show_tech_support'), 'include_commands')):
                pass
                for l_1_include_command in environment.getattr(environment.getattr((undefined(name='management_tech_support') if l_0_management_tech_support is missing else l_0_management_tech_support), 'policy_show_tech_support'), 'include_commands'):
                    _loop_vars = {}
                    pass
                    yield '      include command '
                    yield str(environment.getattr(l_1_include_command, 'command'))
                    yield '\n'
                l_1_include_command = missing
            yield '   exit\n'

blocks = {}
debug_info = '2=18&5=21&7=24&8=26&9=30&10=32&11=34&13=36&14=39&17=42&18=44&19=48'