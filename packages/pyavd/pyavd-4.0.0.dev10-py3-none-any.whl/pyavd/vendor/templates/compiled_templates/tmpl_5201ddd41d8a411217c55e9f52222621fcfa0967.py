from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/tcam-profile.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_tcam_profile = resolve('tcam_profile')
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
    if t_2((undefined(name='tcam_profile') if l_0_tcam_profile is missing else l_0_tcam_profile)):
        pass
        yield '!\nhardware tcam\n'
        if t_2(environment.getattr((undefined(name='tcam_profile') if l_0_tcam_profile is missing else l_0_tcam_profile), 'profiles')):
            pass
            for l_1_profile in t_1(environment.getattr((undefined(name='tcam_profile') if l_0_tcam_profile is missing else l_0_tcam_profile), 'profiles'), 'name'):
                _loop_vars = {}
                pass
                yield '   profile '
                yield str(environment.getattr(l_1_profile, 'name'))
                yield '\n'
                yield str(environment.getattr(l_1_profile, 'config'))
                yield '\n   !\n'
            l_1_profile = missing
        if t_2(environment.getattr((undefined(name='tcam_profile') if l_0_tcam_profile is missing else l_0_tcam_profile), 'system')):
            pass
            yield '   system profile '
            yield str(environment.getattr((undefined(name='tcam_profile') if l_0_tcam_profile is missing else l_0_tcam_profile), 'system'))
            yield '\n'

blocks = {}
debug_info = '2=24&5=27&6=29&7=33&8=35&12=38&13=41'