from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/daemon-terminattr.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_daemon_terminattr = resolve('daemon_terminattr')
    l_0_url = resolve('url')
    l_0_auth = resolve('auth')
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
        t_4 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_4(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if t_4((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr)):
        pass
        yield '\n### TerminAttr Daemon\n\n#### TerminAttr Daemon Summary\n\n| CV Compression | CloudVision Servers | VRF | Authentication | Smash Excludes | Ingest Exclude | Bypass AAA |\n| -------------- | ------------------- | --- | -------------- | -------------- | -------------- | ---------- |\n'
        for l_1_cluster in t_2(environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'clusters'), 'name'):
            l_1_url = l_0_url
            l_1_auth = l_0_auth
            l_1_cvvrf = resolve('cvvrf')
            _loop_vars = {}
            pass
            l_1_url = t_3(context.eval_ctx, t_1(environment.getattr(l_1_cluster, 'cvaddrs'), []), ',')
            _loop_vars['url'] = l_1_url
            if t_4(environment.getattr(environment.getattr(l_1_cluster, 'cvauth'), 'method'), 'key'):
                pass
                l_1_auth = str_join(('key,', t_1(environment.getattr(environment.getattr(l_1_cluster, 'cvauth'), 'key'), ''), ))
                _loop_vars['auth'] = l_1_auth
            elif (t_4(environment.getattr(environment.getattr(l_1_cluster, 'cvauth'), 'method'), 'token') and t_4(environment.getattr(environment.getattr(l_1_cluster, 'cvauth'), 'token_file'))):
                pass
                l_1_auth = str_join(('token,', environment.getattr(environment.getattr(l_1_cluster, 'cvauth'), 'token_file'), ))
                _loop_vars['auth'] = l_1_auth
            elif (t_4(environment.getattr(environment.getattr(l_1_cluster, 'cvauth'), 'method'), 'token-secure') and t_4(environment.getattr(environment.getattr(l_1_cluster, 'cvauth'), 'token_file'))):
                pass
                l_1_auth = str_join(('token-secure,', environment.getattr(environment.getattr(l_1_cluster, 'cvauth'), 'token_file'), ))
                _loop_vars['auth'] = l_1_auth
                yield '+\n'
            elif ((t_4(environment.getattr(environment.getattr(l_1_cluster, 'cvauth'), 'method'), 'certs') and t_4(environment.getattr(environment.getattr(l_1_cluster, 'cvauth'), 'cert_file'))) and t_4(environment.getattr(environment.getattr(l_1_cluster, 'cvauth'), 'key_file'))):
                pass
                l_1_auth = str_join(('certs,', environment.getattr(environment.getattr(l_1_cluster, 'cvauth'), 'cert_file'), ',', environment.getattr(environment.getattr(l_1_cluster, 'cvauth'), 'key_file'), ))
                _loop_vars['auth'] = l_1_auth
                if t_4(environment.getattr(environment.getattr(l_1_cluster, 'cvauth'), 'ca_file')):
                    pass
                    l_1_auth = str_join(((undefined(name='auth') if l_1_auth is missing else l_1_auth), ',', environment.getattr(environment.getattr(l_1_cluster, 'cvauth'), 'ca_file'), ))
                    _loop_vars['auth'] = l_1_auth
            if t_4(environment.getattr(l_1_cluster, 'cvvrf')):
                pass
                l_1_cvvrf = environment.getattr(l_1_cluster, 'cvvrf')
                _loop_vars['cvvrf'] = l_1_cvvrf
            else:
                pass
                l_1_cvvrf = t_1(environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'cvvrf'), '-')
                _loop_vars['cvvrf'] = l_1_cvvrf
            yield '| gzip | '
            yield str((undefined(name='url') if l_1_url is missing else l_1_url))
            yield ' | '
            yield str((undefined(name='cvvrf') if l_1_cvvrf is missing else l_1_cvvrf))
            yield ' | '
            yield str(t_1((undefined(name='auth') if l_1_auth is missing else l_1_auth), '-'))
            yield ' | '
            yield str(t_1(environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'smashexcludes'), '-'))
            yield ' | '
            yield str(t_1(environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'ingestexclude'), '-'))
            yield ' | '
            yield str(t_1(environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'disable_aaa'), False))
            yield ' |\n'
        l_1_cluster = l_1_url = l_1_auth = l_1_cvvrf = missing
        if t_4(environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'cvaddrs')):
            pass
            l_0_url = t_3(context.eval_ctx, t_1(environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'cvaddrs'), []), ',')
            context.vars['url'] = l_0_url
            context.exported_vars.add('url')
            if t_4(environment.getattr(environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'cvauth'), 'method'), 'key'):
                pass
                l_0_auth = str_join(('key,', t_1(environment.getattr(environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'cvauth'), 'key'), ''), ))
                context.vars['auth'] = l_0_auth
                context.exported_vars.add('auth')
            elif (t_4(environment.getattr(environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'cvauth'), 'method'), 'token') and t_4(environment.getattr(environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'cvauth'), 'token_file'))):
                pass
                l_0_auth = str_join(('token,', environment.getattr(environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'cvauth'), 'token_file'), ))
                context.vars['auth'] = l_0_auth
                context.exported_vars.add('auth')
            elif (t_4(environment.getattr(environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'cvauth'), 'method'), 'token-secure') and t_4(environment.getattr(environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'cvauth'), 'token_file'))):
                pass
                l_0_auth = str_join(('token-secure,', environment.getattr(environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'cvauth'), 'token_file'), ))
                context.vars['auth'] = l_0_auth
                context.exported_vars.add('auth')
            elif ((t_4(environment.getattr(environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'cvauth'), 'method'), 'certs') and t_4(environment.getattr(environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'cvauth'), 'cert_file'))) and t_4(environment.getattr(environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'cvauth'), 'key_file'))):
                pass
                l_0_auth = str_join(('certs,', environment.getattr(environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'cvauth'), 'cert_file'), ',', environment.getattr(environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'cvauth'), 'key_file'), ))
                context.vars['auth'] = l_0_auth
                context.exported_vars.add('auth')
                if t_4(environment.getattr(environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'cvauth'), 'ca_file')):
                    pass
                    l_0_auth = str_join(((undefined(name='auth') if l_0_auth is missing else l_0_auth), ',', environment.getattr(environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'cvauth'), 'ca_file'), ))
                    context.vars['auth'] = l_0_auth
                    context.exported_vars.add('auth')
            yield '| gzip | '
            yield str((undefined(name='url') if l_0_url is missing else l_0_url))
            yield ' | '
            yield str(t_1(environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'cvvrf'), '-'))
            yield ' | '
            yield str(t_1((undefined(name='auth') if l_0_auth is missing else l_0_auth), '-'))
            yield ' | '
            yield str(t_1(environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'smashexcludes'), '-'))
            yield ' | '
            yield str(t_1(environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'ingestexclude'), '-'))
            yield ' | '
            yield str(t_1(environment.getattr((undefined(name='daemon_terminattr') if l_0_daemon_terminattr is missing else l_0_daemon_terminattr), 'disable_aaa'), False))
            yield ' |\n'
        yield '\n#### TerminAttr Daemon Device Configuration\n\n```eos\n'
        template = environment.get_template('eos/daemon-terminattr.j2', 'documentation/daemon-terminattr.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {'auth': l_0_auth, 'url': l_0_url})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '2=38&10=41&11=47&12=49&13=51&14=53&15=55&16=57&17=59&18=62&19=64&20=66&21=68&24=70&25=72&27=76&29=79&31=92&32=94&33=97&34=99&35=102&36=104&37=107&38=109&39=112&40=114&41=117&42=119&45=123&51=136'