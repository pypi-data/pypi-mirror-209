from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/standard-access-lists.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_standard_access_lists = resolve('standard_access_lists')
    try:
        t_1 = environment.filters['arista.avd.natural_sort']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.natural_sort' found.")
    try:
        t_2 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_2((undefined(name='standard_access_lists') if l_0_standard_access_lists is missing else l_0_standard_access_lists)):
        pass
        yield '\n### Standard Access-lists\n\n#### Standard Access-lists Summary\n\n'
        for l_1_standard_access_list in t_1((undefined(name='standard_access_lists') if l_0_standard_access_lists is missing else l_0_standard_access_lists), 'name'):
            _loop_vars = {}
            pass
            yield '##### '
            yield str(environment.getattr(l_1_standard_access_list, 'name'))
            yield '\n'
            if t_2(environment.getattr(l_1_standard_access_list, 'counters_per_entry'), True):
                pass
                yield '\nACL has counting mode `counters per-entry` enabled!\n'
            yield '\n| Sequence | Action |\n| -------- | ------ |\n'
            for l_2_sequence in t_1(environment.getattr(l_1_standard_access_list, 'sequence_numbers'), 'sequence'):
                _loop_vars = {}
                pass
                yield '| '
                yield str(environment.getattr(l_2_sequence, 'sequence'))
                yield ' | '
                yield str(environment.getattr(l_2_sequence, 'action'))
                yield ' |\n'
            l_2_sequence = missing
            yield '\n'
        l_1_standard_access_list = missing
        yield '#### Standard Access-lists Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/standard-access-lists.j2', 'documentation/standard-access-lists.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '2=24&8=27&9=31&10=33&17=37&18=41&25=49'