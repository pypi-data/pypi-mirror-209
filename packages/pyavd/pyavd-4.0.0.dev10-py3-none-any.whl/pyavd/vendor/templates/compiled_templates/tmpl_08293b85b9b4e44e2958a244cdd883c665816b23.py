from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/router-bfd.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_router_bfd = resolve('router_bfd')
    l_0_interval = resolve('interval')
    l_0_min_rx = resolve('min_rx')
    l_0_multiplier = resolve('multiplier')
    l_0_init_interval = resolve('init_interval')
    l_0_init_multiplier = resolve('init_multiplier')
    l_0_ref_min_rx = resolve('ref_min_rx')
    l_0_ref_discriminator = resolve('ref_discriminator')
    try:
        t_1 = environment.filters['arista.avd.default']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No filter named 'arista.avd.default' found.")
    try:
        t_2 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_2(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_2((undefined(name='router_bfd') if l_0_router_bfd is missing else l_0_router_bfd)):
        pass
        yield '\n### Router BFD\n'
        if ((t_2(environment.getattr((undefined(name='router_bfd') if l_0_router_bfd is missing else l_0_router_bfd), 'interval')) and t_2(environment.getattr((undefined(name='router_bfd') if l_0_router_bfd is missing else l_0_router_bfd), 'min_rx'))) and t_2(environment.getattr((undefined(name='router_bfd') if l_0_router_bfd is missing else l_0_router_bfd), 'multiplier'))):
            pass
            yield '\n#### Router BFD Singlehop Summary\n\n| Interval | Minimum RX | Multiplier |\n| -------- | ---------- | ---------- |\n'
            l_0_interval = t_1(environment.getattr((undefined(name='router_bfd') if l_0_router_bfd is missing else l_0_router_bfd), 'interval'), '-')
            context.vars['interval'] = l_0_interval
            context.exported_vars.add('interval')
            l_0_min_rx = t_1(environment.getattr((undefined(name='router_bfd') if l_0_router_bfd is missing else l_0_router_bfd), 'min_rx'), '-')
            context.vars['min_rx'] = l_0_min_rx
            context.exported_vars.add('min_rx')
            l_0_multiplier = t_1(environment.getattr((undefined(name='router_bfd') if l_0_router_bfd is missing else l_0_router_bfd), 'multiplier'), '-')
            context.vars['multiplier'] = l_0_multiplier
            context.exported_vars.add('multiplier')
            yield '| '
            yield str((undefined(name='interval') if l_0_interval is missing else l_0_interval))
            yield ' | '
            yield str((undefined(name='min_rx') if l_0_min_rx is missing else l_0_min_rx))
            yield ' | '
            yield str((undefined(name='multiplier') if l_0_multiplier is missing else l_0_multiplier))
            yield ' |\n'
        if t_2(environment.getattr((undefined(name='router_bfd') if l_0_router_bfd is missing else l_0_router_bfd), 'multihop')):
            pass
            yield '\n#### Router BFD Multihop Summary\n\n| Interval | Minimum RX | Multiplier |\n| -------- | ---------- | ---------- |\n'
            l_0_interval = t_1(environment.getattr(environment.getattr((undefined(name='router_bfd') if l_0_router_bfd is missing else l_0_router_bfd), 'multihop'), 'interval'), '-')
            context.vars['interval'] = l_0_interval
            context.exported_vars.add('interval')
            l_0_min_rx = t_1(environment.getattr(environment.getattr((undefined(name='router_bfd') if l_0_router_bfd is missing else l_0_router_bfd), 'multihop'), 'min_rx'), '-')
            context.vars['min_rx'] = l_0_min_rx
            context.exported_vars.add('min_rx')
            l_0_multiplier = t_1(environment.getattr(environment.getattr((undefined(name='router_bfd') if l_0_router_bfd is missing else l_0_router_bfd), 'multihop'), 'multiplier'), '-')
            context.vars['multiplier'] = l_0_multiplier
            context.exported_vars.add('multiplier')
            yield '| '
            yield str((undefined(name='interval') if l_0_interval is missing else l_0_interval))
            yield ' | '
            yield str((undefined(name='min_rx') if l_0_min_rx is missing else l_0_min_rx))
            yield ' | '
            yield str((undefined(name='multiplier') if l_0_multiplier is missing else l_0_multiplier))
            yield ' |\n'
        if t_2(environment.getattr((undefined(name='router_bfd') if l_0_router_bfd is missing else l_0_router_bfd), 'sbfd')):
            pass
            yield '\n#### Router BFD SBFD Summary\n\n| Initiator Interval | Initiator Multiplier | Reflector Minimum RX | Reflector Local-Discriminator |\n| ------------------ | -------------------- | -------------------- | ----------------------------- |\n'
            l_0_init_interval = t_1(environment.getattr(environment.getattr((undefined(name='router_bfd') if l_0_router_bfd is missing else l_0_router_bfd), 'sbfd'), 'initiator_interval'), '-')
            context.vars['init_interval'] = l_0_init_interval
            context.exported_vars.add('init_interval')
            l_0_init_multiplier = t_1(environment.getattr(environment.getattr((undefined(name='router_bfd') if l_0_router_bfd is missing else l_0_router_bfd), 'sbfd'), 'initiator_multiplier'), '-')
            context.vars['init_multiplier'] = l_0_init_multiplier
            context.exported_vars.add('init_multiplier')
            l_0_ref_min_rx = t_1(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bfd') if l_0_router_bfd is missing else l_0_router_bfd), 'sbfd'), 'reflector'), 'min_rx'), '-')
            context.vars['ref_min_rx'] = l_0_ref_min_rx
            context.exported_vars.add('ref_min_rx')
            l_0_ref_discriminator = t_1(environment.getattr(environment.getattr(environment.getattr((undefined(name='router_bfd') if l_0_router_bfd is missing else l_0_router_bfd), 'sbfd'), 'reflector'), 'local_discriminator'), '-')
            context.vars['ref_discriminator'] = l_0_ref_discriminator
            context.exported_vars.add('ref_discriminator')
            yield '| '
            yield str((undefined(name='init_interval') if l_0_init_interval is missing else l_0_init_interval))
            yield ' | '
            yield str((undefined(name='init_multiplier') if l_0_init_multiplier is missing else l_0_init_multiplier))
            yield ' | '
            yield str((undefined(name='ref_min_rx') if l_0_ref_min_rx is missing else l_0_ref_min_rx))
            yield ' | '
            yield str((undefined(name='ref_discriminator') if l_0_ref_discriminator is missing else l_0_ref_discriminator))
            yield ' |\n'
        yield '\n#### Router BFD Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/router-bfd.j2', 'documentation/router-bfd.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {'init_interval': l_0_init_interval, 'init_multiplier': l_0_init_multiplier, 'interval': l_0_interval, 'min_rx': l_0_min_rx, 'multiplier': l_0_multiplier, 'ref_discriminator': l_0_ref_discriminator, 'ref_min_rx': l_0_ref_min_rx})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '2=31&5=34&11=37&12=40&13=43&14=47&16=53&22=56&23=59&24=62&25=66&27=72&33=75&34=78&35=81&36=84&37=88&43=97'