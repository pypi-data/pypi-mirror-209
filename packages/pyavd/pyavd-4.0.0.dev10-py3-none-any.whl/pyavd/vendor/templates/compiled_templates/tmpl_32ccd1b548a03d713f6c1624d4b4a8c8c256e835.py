from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/match-list-input.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_match_list_input = resolve('match_list_input')
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
    if t_2((undefined(name='match_list_input') if l_0_match_list_input is missing else l_0_match_list_input)):
        pass
        yield '\n### Match-lists\n\n'
        if t_2(environment.getattr((undefined(name='match_list_input') if l_0_match_list_input is missing else l_0_match_list_input), 'string')):
            pass
            yield '#### Match-list Input String Summary\n\n'
            for l_1_match_list in t_1(environment.getattr((undefined(name='match_list_input') if l_0_match_list_input is missing else l_0_match_list_input), 'string'), 'name'):
                _loop_vars = {}
                pass
                yield '##### '
                yield str(environment.getattr(l_1_match_list, 'name'))
                yield '\n\n| Sequence | Match Regex |\n| -------- | ------ |\n'
                for l_2_sequence in t_1(environment.getattr(l_1_match_list, 'sequence_numbers'), 'sequence'):
                    _loop_vars = {}
                    pass
                    yield '| '
                    yield str(environment.getattr(l_2_sequence, 'sequence'))
                    yield ' | '
                    yield str(environment.getattr(l_2_sequence, 'match_regex'))
                    yield ' |\n'
                l_2_sequence = missing
                yield '\n'
            l_1_match_list = missing
            yield '\n'
        yield '#### Match-lists Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/match-list-input.j2', 'documentation/match-list-input.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '2=24&6=27&9=30&10=34&14=36&15=40&24=49'