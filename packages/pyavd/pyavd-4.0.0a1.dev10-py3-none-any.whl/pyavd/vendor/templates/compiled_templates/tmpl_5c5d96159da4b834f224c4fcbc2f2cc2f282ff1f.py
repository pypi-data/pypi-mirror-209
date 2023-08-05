from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/ntp.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_ntp = resolve('ntp')
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
    if t_3((undefined(name='ntp') if l_0_ntp is missing else l_0_ntp)):
        pass
        yield '\n### NTP\n\n#### NTP Summary\n'
        if t_3(environment.getattr(environment.getattr((undefined(name='ntp') if l_0_ntp is missing else l_0_ntp), 'local_interface'), 'name')):
            pass
            yield '\n##### NTP Local Interface\n\n| Interface | VRF |\n| --------- | --- |\n| '
            yield str(environment.getattr(environment.getattr((undefined(name='ntp') if l_0_ntp is missing else l_0_ntp), 'local_interface'), 'name'))
            yield ' | '
            yield str(t_1(environment.getattr(environment.getattr((undefined(name='ntp') if l_0_ntp is missing else l_0_ntp), 'local_interface'), 'vrf'), '-'))
            yield ' |\n'
        if t_3(environment.getattr((undefined(name='ntp') if l_0_ntp is missing else l_0_ntp), 'servers')):
            pass
            yield '\n##### NTP Servers\n\n| Server | VRF | Preferred | Burst | iBurst | Version | Min Poll | Max Poll | Local-interface | Key |\n| ------ | --- | --------- | ----- | ------ | ------- | -------- | -------- | --------------- | --- |\n'
            for l_1_server in t_2(environment.getattr((undefined(name='ntp') if l_0_ntp is missing else l_0_ntp), 'servers'), 'name'):
                l_1_namespace = resolve('namespace')
                l_1_r = resolve('r')
                _loop_vars = {}
                pass
                if t_3(environment.getattr(l_1_server, 'name')):
                    pass
                    l_1_r = context.call((undefined(name='namespace') if l_1_namespace is missing else l_1_namespace), _loop_vars=_loop_vars)
                    _loop_vars['r'] = l_1_r
                    if not isinstance(l_1_r, Namespace):
                        raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                    l_1_r['s'] = environment.getattr(l_1_server, 'name')
                    if not isinstance(l_1_r, Namespace):
                        raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                    l_1_r['v'] = t_1(environment.getattr(l_1_server, 'vrf'), '-')
                    if not isinstance(l_1_r, Namespace):
                        raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                    l_1_r['p'] = t_1(environment.getattr(l_1_server, 'preferred'), '-')
                    if not isinstance(l_1_r, Namespace):
                        raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                    l_1_r['b'] = t_1(environment.getattr(l_1_server, 'burst'), '-')
                    if not isinstance(l_1_r, Namespace):
                        raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                    l_1_r['i'] = t_1(environment.getattr(l_1_server, 'iburst'), '-')
                    if not isinstance(l_1_r, Namespace):
                        raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                    l_1_r['vv'] = t_1(environment.getattr(l_1_server, 'version'), '-')
                    if not isinstance(l_1_r, Namespace):
                        raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                    l_1_r['mi'] = t_1(environment.getattr(l_1_server, 'minpoll'), '-')
                    if not isinstance(l_1_r, Namespace):
                        raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                    l_1_r['ma'] = t_1(environment.getattr(l_1_server, 'maxpoll'), '-')
                    if not isinstance(l_1_r, Namespace):
                        raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                    l_1_r['l'] = t_1(environment.getattr(l_1_server, 'local_interface'), '-')
                    if not isinstance(l_1_r, Namespace):
                        raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
                    l_1_r['k'] = t_1(environment.getattr(l_1_server, 'key'), '-')
                    yield '| '
                    yield str(environment.getattr((undefined(name='r') if l_1_r is missing else l_1_r), 's'))
                    yield ' | '
                    yield str(environment.getattr((undefined(name='r') if l_1_r is missing else l_1_r), 'v'))
                    yield ' | '
                    yield str(environment.getattr((undefined(name='r') if l_1_r is missing else l_1_r), 'p'))
                    yield ' | '
                    yield str(environment.getattr((undefined(name='r') if l_1_r is missing else l_1_r), 'b'))
                    yield ' | '
                    yield str(environment.getattr((undefined(name='r') if l_1_r is missing else l_1_r), 'i'))
                    yield ' | '
                    yield str(environment.getattr((undefined(name='r') if l_1_r is missing else l_1_r), 'vv'))
                    yield ' | '
                    yield str(environment.getattr((undefined(name='r') if l_1_r is missing else l_1_r), 'mi'))
                    yield ' | '
                    yield str(environment.getattr((undefined(name='r') if l_1_r is missing else l_1_r), 'ma'))
                    yield ' | '
                    yield str(environment.getattr((undefined(name='r') if l_1_r is missing else l_1_r), 'l'))
                    yield ' | '
                    yield str(environment.getattr((undefined(name='r') if l_1_r is missing else l_1_r), 'k'))
                    yield ' |\n'
            l_1_server = l_1_namespace = l_1_r = missing
        if ((t_3(environment.getattr((undefined(name='ntp') if l_0_ntp is missing else l_0_ntp), 'authenticate')) or t_3(environment.getattr((undefined(name='ntp') if l_0_ntp is missing else l_0_ntp), 'trusted_keys'))) or t_3(environment.getattr((undefined(name='ntp') if l_0_ntp is missing else l_0_ntp), 'authentication_keys'))):
            pass
            yield '\n##### NTP Authentication\n'
            if t_3(environment.getattr((undefined(name='ntp') if l_0_ntp is missing else l_0_ntp), 'authenticate_servers_only'), True):
                pass
                yield '\n- Authentication enabled (Servers only)\n'
            elif t_3(environment.getattr((undefined(name='ntp') if l_0_ntp is missing else l_0_ntp), 'authenticate'), True):
                pass
                yield '\n- Authentication enabled\n'
            if t_3(environment.getattr((undefined(name='ntp') if l_0_ntp is missing else l_0_ntp), 'trusted_keys')):
                pass
                yield '\n- Trusted Keys: '
                yield str(environment.getattr((undefined(name='ntp') if l_0_ntp is missing else l_0_ntp), 'trusted_keys'))
                yield '\n'
        if t_3(environment.getattr((undefined(name='ntp') if l_0_ntp is missing else l_0_ntp), 'authentication_keys')):
            pass
            yield '\n##### NTP Authentication Keys\n\n| ID | Algorithm |\n| -- | -------- |\n'
            for l_1_authentication_key in t_2(environment.getattr((undefined(name='ntp') if l_0_ntp is missing else l_0_ntp), 'authentication_keys'), 'id'):
                _loop_vars = {}
                pass
                if ((t_3(environment.getattr(l_1_authentication_key, 'id')) and t_3(environment.getattr(l_1_authentication_key, 'key'))) and t_3(environment.getattr(l_1_authentication_key, 'hash_algorithm'))):
                    pass
                    yield '| '
                    yield str(environment.getattr(l_1_authentication_key, 'id'))
                    yield ' | '
                    yield str(environment.getattr(l_1_authentication_key, 'hash_algorithm'))
                    yield ' |\n'
            l_1_authentication_key = missing
        yield '\n#### NTP Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/ntp.j2', 'documentation/ntp.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '2=30&7=33&13=36&15=40&21=43&22=48&23=50&24=52&25=55&26=58&27=61&28=64&29=67&30=70&31=73&32=76&33=79&34=83&38=104&43=107&46=110&50=113&52=116&55=118&61=121&62=124&65=127&73=133'