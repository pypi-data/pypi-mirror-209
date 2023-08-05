from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/ipv6-prefix-lists.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_ipv6_prefix_lists = resolve('ipv6_prefix_lists')
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
    if t_2((undefined(name='ipv6_prefix_lists') if l_0_ipv6_prefix_lists is missing else l_0_ipv6_prefix_lists)):
        pass
        yield '\n### IPv6 Prefix-lists\n\n#### IPv6 Prefix-lists Summary\n\n'
        for l_1_ipv6_prefix_list in t_1((undefined(name='ipv6_prefix_lists') if l_0_ipv6_prefix_lists is missing else l_0_ipv6_prefix_lists), 'name'):
            _loop_vars = {}
            pass
            yield '##### '
            yield str(environment.getattr(l_1_ipv6_prefix_list, 'name'))
            yield '\n\n| Sequence | Action |\n| -------- | ------ |\n'
            for l_2_sequence in t_1(environment.getattr(l_1_ipv6_prefix_list, 'sequence_numbers'), 'sequence'):
                _loop_vars = {}
                pass
                yield '| '
                yield str(environment.getattr(l_2_sequence, 'sequence'))
                yield ' | '
                yield str(environment.getattr(l_2_sequence, 'action'))
                yield ' |\n'
            l_2_sequence = missing
            yield '\n'
        l_1_ipv6_prefix_list = missing
        yield '#### IPv6 Prefix-lists Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/ipv6-prefix-lists.j2', 'documentation/ipv6-prefix-lists.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '2=24&8=27&9=31&13=33&14=37&21=45'