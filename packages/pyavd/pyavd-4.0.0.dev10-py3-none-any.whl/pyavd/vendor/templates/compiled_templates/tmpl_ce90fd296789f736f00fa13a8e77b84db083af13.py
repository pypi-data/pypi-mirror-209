from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/patch-panel.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_patch_panel = resolve('patch_panel')
    try:
        t_1 = environment.filters['arista.avd.default']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.default' found.")
    try:
        t_2 = environment.filters['capitalize']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No filter named 'capitalize' found.")
    try:
        t_3 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_3((undefined(name='patch_panel') if l_0_patch_panel is missing else l_0_patch_panel)):
        pass
        yield '\n## Patch Panel\n\n### Patch Panel Summary\n\n| Patch Name | Enabled | Connector A Type | Connector A Endpoint | Connector B Type | Connector B Endpoint |\n| ---------- | ------- | ---------------- | -------------------- | ---------------- | -------------------- |\n'
        l_1_loop = missing
        for l_1_patch, l_1_loop in LoopContext(t_1(environment.getattr((undefined(name='patch_panel') if l_0_patch_panel is missing else l_0_patch_panel), 'patches'), []), undefined):
            l_1_namespace = resolve('namespace')
            l_1_patch_panel_patch = resolve('patch_panel_patch')
            _loop_vars = {}
            pass
            if t_3(environment.getattr(l_1_patch, 'name')):
                pass
                l_1_patch_panel_patch = context.call((undefined(name='namespace') if l_1_namespace is missing else l_1_namespace), _loop_vars=_loop_vars)
                _loop_vars['patch_panel_patch'] = l_1_patch_panel_patch
                if not isinstance(l_1_patch_panel_patch, Namespace):
                    raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                l_1_patch_panel_patch['enabled'] = t_1(environment.getattr(l_1_patch, 'enabled'), True)
                l_2_loop = missing
                for l_2_connector, l_2_loop in LoopContext(t_1(environment.getattr(l_1_patch, 'connectors'), []), undefined):
                    _loop_vars = {}
                    pass
                    if environment.getattr(l_2_loop, 'first'):
                        pass
                        if not isinstance(l_1_patch_panel_patch, Namespace):
                            raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                        l_1_patch_panel_patch['connector_a_type'] = t_2(environment.getattr(l_2_connector, 'type'))
                        if not isinstance(l_1_patch_panel_patch, Namespace):
                            raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                        l_1_patch_panel_patch['connector_a_endpoint'] = environment.getattr(l_2_connector, 'endpoint')
                    else:
                        pass
                        if not isinstance(l_1_patch_panel_patch, Namespace):
                            raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                        l_1_patch_panel_patch['connector_b_type'] = t_2(environment.getattr(l_2_connector, 'type'))
                        if not isinstance(l_1_patch_panel_patch, Namespace):
                            raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                        l_1_patch_panel_patch['connector_b_endpoint'] = environment.getattr(l_2_connector, 'endpoint')
                l_2_loop = l_2_connector = missing
                yield '| '
                yield str(environment.getattr(l_1_patch, 'name'))
                yield ' | '
                yield str(environment.getattr((undefined(name='patch_panel_patch') if l_1_patch_panel_patch is missing else l_1_patch_panel_patch), 'enabled'))
                yield ' | '
                yield str(environment.getattr((undefined(name='patch_panel_patch') if l_1_patch_panel_patch is missing else l_1_patch_panel_patch), 'connector_a_type'))
                yield ' | '
                yield str(environment.getattr((undefined(name='patch_panel_patch') if l_1_patch_panel_patch is missing else l_1_patch_panel_patch), 'connector_a_endpoint'))
                yield ' | '
                yield str(environment.getattr((undefined(name='patch_panel_patch') if l_1_patch_panel_patch is missing else l_1_patch_panel_patch), 'connector_b_type'))
                yield ' | '
                yield str(environment.getattr((undefined(name='patch_panel_patch') if l_1_patch_panel_patch is missing else l_1_patch_panel_patch), 'connector_b_endpoint'))
                yield ' |\n'
        l_1_loop = l_1_patch = l_1_namespace = l_1_patch_panel_patch = missing
        yield '\n### Patch Panel Configuration\n\n```eos\n'
        template = environment.get_template('eos/patch-panel.j2', 'documentation/patch-panel.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '2=30&10=34&11=39&12=41&13=43&14=47&15=50&16=52&17=55&19=60&20=63&23=68&30=82'