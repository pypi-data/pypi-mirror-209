from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/spanning-tree.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_spanning_tree = resolve('spanning_tree')
    l_0_global_settings = resolve('global_settings')
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
        t_3 = environment.filters['join']
    except KeyError:
        @internalcode
        def t_3(*unused):
            raise TemplateRuntimeError("No filter named 'join' found.")
    try:
        t_4 = environment.filters['length']
    except KeyError:
        @internalcode
        def t_4(*unused):
            raise TemplateRuntimeError("No filter named 'length' found.")
    try:
        t_5 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_5(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_5((undefined(name='spanning_tree') if l_0_spanning_tree is missing else l_0_spanning_tree)):
        pass
        yield '\n## Spanning Tree\n\n### Spanning Tree Summary\n\nSTP mode: **'
        yield str(t_1(environment.getattr((undefined(name='spanning_tree') if l_0_spanning_tree is missing else l_0_spanning_tree), 'mode'), 'mstp'))
        yield '**\n'
        if t_5(environment.getattr((undefined(name='spanning_tree') if l_0_spanning_tree is missing else l_0_spanning_tree), 'root_super')):
            pass
            yield '\nSTP Root Super: **'
            yield str(environment.getattr((undefined(name='spanning_tree') if l_0_spanning_tree is missing else l_0_spanning_tree), 'root_super'))
            yield '**\n'
        if t_5(environment.getattr((undefined(name='spanning_tree') if l_0_spanning_tree is missing else l_0_spanning_tree), 'mst_instances')):
            pass
            yield '\n#### MSTP Instance and Priority\n\n| Instance(s) | Priority |\n| -------- | -------- |\n'
            for l_1_mst_instance in t_2(environment.getattr((undefined(name='spanning_tree') if l_0_spanning_tree is missing else l_0_spanning_tree), 'mst_instances'), 'id'):
                _loop_vars = {}
                pass
                yield '| '
                yield str(environment.getattr(l_1_mst_instance, 'id'))
                yield ' | '
                yield str(t_1(environment.getattr(l_1_mst_instance, 'priority'), '-'))
                yield ' |\n'
            l_1_mst_instance = missing
        if t_5(environment.getattr(environment.getattr((undefined(name='spanning_tree') if l_0_spanning_tree is missing else l_0_spanning_tree), 'mst'), 'configuration')):
            pass
            yield '\n#### MST Configuration\n\n| Variable | Value |\n| -------- | -------- |\n'
            if t_5(environment.getattr(environment.getattr(environment.getattr((undefined(name='spanning_tree') if l_0_spanning_tree is missing else l_0_spanning_tree), 'mst'), 'configuration'), 'name')):
                pass
                yield '| Name | '
                yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='spanning_tree') if l_0_spanning_tree is missing else l_0_spanning_tree), 'mst'), 'configuration'), 'name'))
                yield ' |\n'
            if t_5(environment.getattr(environment.getattr(environment.getattr((undefined(name='spanning_tree') if l_0_spanning_tree is missing else l_0_spanning_tree), 'mst'), 'configuration'), 'revision')):
                pass
                yield '| Revision | '
                yield str(environment.getattr(environment.getattr(environment.getattr((undefined(name='spanning_tree') if l_0_spanning_tree is missing else l_0_spanning_tree), 'mst'), 'configuration'), 'revision'))
                yield ' |\n'
            if t_5(environment.getattr(environment.getattr(environment.getattr((undefined(name='spanning_tree') if l_0_spanning_tree is missing else l_0_spanning_tree), 'mst'), 'configuration'), 'instances')):
                pass
                for l_1_instance in t_2(environment.getattr(environment.getattr(environment.getattr((undefined(name='spanning_tree') if l_0_spanning_tree is missing else l_0_spanning_tree), 'mst'), 'configuration'), 'instances'), 'id'):
                    _loop_vars = {}
                    pass
                    yield '| Instance '
                    yield str(environment.getattr(l_1_instance, 'id'))
                    yield ' | VLAN(s) '
                    yield str(t_1(environment.getattr(l_1_instance, 'vlans'), '-'))
                    yield ' |\n'
                l_1_instance = missing
        if t_5(environment.getattr((undefined(name='spanning_tree') if l_0_spanning_tree is missing else l_0_spanning_tree), 'mode'), 'rapid-pvst'):
            pass
            yield '\n#### Rapid-PVST Instance and Priority\n\n| Instance(s) | Priority |\n| -------- | -------- |\n'
            if t_5(environment.getattr((undefined(name='spanning_tree') if l_0_spanning_tree is missing else l_0_spanning_tree), 'rapid_pvst_instances')):
                pass
                for l_1_vlan_id in t_2(environment.getattr((undefined(name='spanning_tree') if l_0_spanning_tree is missing else l_0_spanning_tree), 'rapid_pvst_instances'), 'id'):
                    _loop_vars = {}
                    pass
                    yield '| '
                    yield str(environment.getattr(l_1_vlan_id, 'id'))
                    yield ' | '
                    yield str(t_1(environment.getattr(l_1_vlan_id, 'priority'), '-'))
                    yield ' |\n'
                l_1_vlan_id = missing
        l_0_global_settings = []
        context.vars['global_settings'] = l_0_global_settings
        context.exported_vars.add('global_settings')
        if t_5(environment.getattr((undefined(name='spanning_tree') if l_0_spanning_tree is missing else l_0_spanning_tree), 'mode'), 'rstp'):
            pass
            if t_5(environment.getattr((undefined(name='spanning_tree') if l_0_spanning_tree is missing else l_0_spanning_tree), 'rstp_priority')):
                pass
                context.call(environment.getattr((undefined(name='global_settings') if l_0_global_settings is missing else l_0_global_settings), 'append'), str_join(('- Global RSTP priority: ', environment.getattr((undefined(name='spanning_tree') if l_0_spanning_tree is missing else l_0_spanning_tree), 'rstp_priority'), )))
        if t_5(environment.getattr((undefined(name='spanning_tree') if l_0_spanning_tree is missing else l_0_spanning_tree), 'no_spanning_tree_vlan')):
            pass
            context.call(environment.getattr((undefined(name='global_settings') if l_0_global_settings is missing else l_0_global_settings), 'append'), str_join(('- Spanning Tree disabled for VLANs: ', '**', environment.getattr((undefined(name='spanning_tree') if l_0_spanning_tree is missing else l_0_spanning_tree), 'no_spanning_tree_vlan'), '**', )))
        if t_5(environment.getattr(environment.getattr((undefined(name='spanning_tree') if l_0_spanning_tree is missing else l_0_spanning_tree), 'edge_port'), 'bpduguard_default'), True):
            pass
            context.call(environment.getattr((undefined(name='global_settings') if l_0_global_settings is missing else l_0_global_settings), 'append'), '- Global BPDU Guard for Edge ports is enabled.')
        elif t_5(environment.getattr(environment.getattr((undefined(name='spanning_tree') if l_0_spanning_tree is missing else l_0_spanning_tree), 'edge_port'), 'bpduguard_default'), False):
            pass
            context.call(environment.getattr((undefined(name='global_settings') if l_0_global_settings is missing else l_0_global_settings), 'append'), '- Global BPDU Guard for Edge ports is disabled.')
        if t_5(environment.getattr(environment.getattr((undefined(name='spanning_tree') if l_0_spanning_tree is missing else l_0_spanning_tree), 'edge_port'), 'bpdufilter_default'), True):
            pass
            context.call(environment.getattr((undefined(name='global_settings') if l_0_global_settings is missing else l_0_global_settings), 'append'), '- Global BPDU Filter for Edge ports is enabled.')
        elif t_5(environment.getattr(environment.getattr((undefined(name='spanning_tree') if l_0_spanning_tree is missing else l_0_spanning_tree), 'edge_port'), 'bpdufilter_default'), False):
            pass
            context.call(environment.getattr((undefined(name='global_settings') if l_0_global_settings is missing else l_0_global_settings), 'append'), '- Global BPDU Filter for Edge ports is disabled.')
        if t_5(environment.getattr((undefined(name='spanning_tree') if l_0_spanning_tree is missing else l_0_spanning_tree), 'mode'), 'mstp'):
            pass
            if t_5(environment.getattr((undefined(name='spanning_tree') if l_0_spanning_tree is missing else l_0_spanning_tree), 'mst')):
                pass
                if t_5(environment.getattr(environment.getattr((undefined(name='spanning_tree') if l_0_spanning_tree is missing else l_0_spanning_tree), 'mst'), 'pvst_border'), True):
                    pass
                    context.call(environment.getattr((undefined(name='global_settings') if l_0_global_settings is missing else l_0_global_settings), 'append'), '- MST PSVT Border is enabled.')
        if (t_4((undefined(name='global_settings') if l_0_global_settings is missing else l_0_global_settings)) > 0):
            pass
            yield '\n#### Global Spanning-Tree Settings\n\n'
            yield str(t_3(context.eval_ctx, (undefined(name='global_settings') if l_0_global_settings is missing else l_0_global_settings), '\n'))
            yield '\n'
        yield '\n### Spanning Tree Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/spanning-tree.j2', 'documentation/spanning-tree.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {'global_settings': l_0_global_settings})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '2=43&8=46&9=48&11=51&13=53&19=56&20=60&23=65&29=68&30=71&32=73&33=76&35=78&36=80&37=84&41=89&47=92&48=94&49=98&53=103&54=106&55=108&56=110&59=111&60=113&62=114&63=116&64=117&65=119&67=120&68=122&69=123&70=125&72=126&73=128&74=130&75=132&79=133&83=136&89=139'