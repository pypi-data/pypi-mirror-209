from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/patch-panel.j2'

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
        t_2 = environment.filters['arista.avd.natural_sort']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.natural_sort' found.")
    try:
        t_3 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_3((undefined(name='patch_panel') if l_0_patch_panel is missing else l_0_patch_panel)):
        pass
        yield '!\npatch panel\n'
        for l_1_patch in t_1(environment.getattr((undefined(name='patch_panel') if l_0_patch_panel is missing else l_0_patch_panel), 'patches'), []):
            _loop_vars = {}
            pass
            if t_3(environment.getattr(l_1_patch, 'name')):
                pass
                yield '   patch '
                yield str(environment.getattr(l_1_patch, 'name'))
                yield '\n'
                if t_3(environment.getattr(l_1_patch, 'enabled'), False):
                    pass
                    yield '      shutdown\n'
                for l_2_connector in t_2(environment.getattr(l_1_patch, 'connectors')):
                    l_2_connector_cli = resolve('connector_cli')
                    _loop_vars = {}
                    pass
                    if t_3(environment.getattr(l_2_connector, 'id')):
                        pass
                        if t_3(environment.getattr(l_2_connector, 'type'), 'interface'):
                            pass
                            l_2_connector_cli = str_join(('connector ', environment.getattr(l_2_connector, 'id'), ' interface ', environment.getattr(l_2_connector, 'endpoint'), ))
                            _loop_vars['connector_cli'] = l_2_connector_cli
                        elif t_3(environment.getattr(l_2_connector, 'type'), 'pseudowire'):
                            pass
                            l_2_connector_cli = str_join(('connector ', environment.getattr(l_2_connector, 'id'), ' pseudowire ', environment.getattr(l_2_connector, 'endpoint'), ))
                            _loop_vars['connector_cli'] = l_2_connector_cli
                        yield '      '
                        yield str((undefined(name='connector_cli') if l_2_connector_cli is missing else l_2_connector_cli))
                        yield '\n'
                l_2_connector = l_2_connector_cli = missing
            yield '   !\n'
        l_1_patch = missing

blocks = {}
debug_info = '2=30&5=33&6=36&7=39&8=41&11=44&12=48&13=50&14=52&15=54&16=56&18=59'