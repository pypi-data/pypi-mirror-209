from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/management-ssh.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_management_ssh = resolve('management_ssh')
    l_0_namespace = resolve('namespace')
    l_0_ssh = resolve('ssh')
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
    if t_4((undefined(name='management_ssh') if l_0_management_ssh is missing else l_0_management_ssh)):
        pass
        yield '\n### Management SSH\n\n'
        if t_4(environment.getattr((undefined(name='management_ssh') if l_0_management_ssh is missing else l_0_management_ssh), 'access_groups')):
            pass
            yield '#### IPv4 ACL\n\n| IPv4 ACL | VRF |\n| -------- | --- |\n'
            for l_1_acl in environment.getattr((undefined(name='management_ssh') if l_0_management_ssh is missing else l_0_management_ssh), 'access_groups'):
                _loop_vars = {}
                pass
                yield '| '
                yield str(environment.getattr(l_1_acl, 'name'))
                yield ' | '
                yield str(t_1(environment.getattr(l_1_acl, 'vrf'), '-'))
                yield ' |\n'
            l_1_acl = missing
        if t_4(environment.getattr((undefined(name='management_ssh') if l_0_management_ssh is missing else l_0_management_ssh), 'ipv6_access_groups')):
            pass
            yield '\n#### IPv6 ACL\n\n| IPv6 ACL | VRF |\n| -------- | --- |\n'
            for l_1_acl in environment.getattr((undefined(name='management_ssh') if l_0_management_ssh is missing else l_0_management_ssh), 'ipv6_access_groups'):
                _loop_vars = {}
                pass
                yield '| '
                yield str(environment.getattr(l_1_acl, 'name'))
                yield ' | '
                yield str(t_1(environment.getattr(l_1_acl, 'vrf'), '-'))
                yield ' |\n'
            l_1_acl = missing
        yield '\n'
        l_0_ssh = context.call((undefined(name='namespace') if l_0_namespace is missing else l_0_namespace), enable=True)
        context.vars['ssh'] = l_0_ssh
        context.exported_vars.add('ssh')
        if t_4(environment.getattr((undefined(name='management_ssh') if l_0_management_ssh is missing else l_0_management_ssh), 'enable')):
            pass
            if not isinstance(l_0_ssh, Namespace):
                raise TemplateRuntimeError("cannot assign attribute on non-namespace object")
            l_0_ssh['enable'] = environment.getattr((undefined(name='management_ssh') if l_0_management_ssh is missing else l_0_management_ssh), 'enable')
        yield '#### SSH timeout and management\n\n| Idle Timeout | SSH Management |\n| ------------ | -------------- |\n'
        if environment.getattr((undefined(name='ssh') if l_0_ssh is missing else l_0_ssh), 'enable'):
            pass
            l_0_ssh = 'Enabled'
            context.vars['ssh'] = l_0_ssh
            context.exported_vars.add('ssh')
        else:
            pass
            l_0_ssh = 'Disabled'
            context.vars['ssh'] = l_0_ssh
            context.exported_vars.add('ssh')
        yield '| '
        yield str(t_1(environment.getattr((undefined(name='management_ssh') if l_0_management_ssh is missing else l_0_management_ssh), 'idle_timeout'), 'default'))
        yield ' | '
        yield str((undefined(name='ssh') if l_0_ssh is missing else l_0_ssh))
        yield ' |\n\n#### Max number of SSH sessions limit and per-host limit\n\n| Connection Limit | Max from a single Host |\n| ---------------- | ---------------------- |\n| '
        yield str(t_1(environment.getattr(environment.getattr((undefined(name='management_ssh') if l_0_management_ssh is missing else l_0_management_ssh), 'connection'), 'limit'), '-'))
        yield ' | '
        yield str(t_1(environment.getattr(environment.getattr((undefined(name='management_ssh') if l_0_management_ssh is missing else l_0_management_ssh), 'connection'), 'per_host'), '-'))
        yield ' |\n\n#### Ciphers and algorithms\n\n| Ciphers | Key-exchange methods | MAC algorithms | Hostkey server algorithms |\n|---------|----------------------|----------------|---------------------------|\n| '
        yield str(t_3(context.eval_ctx, t_1(environment.getattr((undefined(name='management_ssh') if l_0_management_ssh is missing else l_0_management_ssh), 'cipher'), ['default']), ', '))
        yield ' | '
        yield str(t_3(context.eval_ctx, t_1(environment.getattr((undefined(name='management_ssh') if l_0_management_ssh is missing else l_0_management_ssh), 'key_exchange'), ['default']), ', '))
        yield ' | '
        yield str(t_3(context.eval_ctx, t_1(environment.getattr((undefined(name='management_ssh') if l_0_management_ssh is missing else l_0_management_ssh), 'mac'), ['default']), ', '))
        yield ' | '
        yield str(t_3(context.eval_ctx, t_1(environment.getattr(environment.getattr((undefined(name='management_ssh') if l_0_management_ssh is missing else l_0_management_ssh), 'hostkey'), 'server'), ['default']), ', '))
        yield ' |\n\n'
        if t_4(environment.getattr((undefined(name='management_ssh') if l_0_management_ssh is missing else l_0_management_ssh), 'vrfs')):
            pass
            yield '#### VRFs\n\n| VRF | Status |\n| --- | ------ |\n'
            for l_1_vrf in t_2(environment.getattr((undefined(name='management_ssh') if l_0_management_ssh is missing else l_0_management_ssh), 'vrfs'), 'name'):
                l_1_status = resolve('status')
                _loop_vars = {}
                pass
                if environment.getattr(l_1_vrf, 'enable'):
                    pass
                    l_1_status = 'Enabled'
                    _loop_vars['status'] = l_1_status
                else:
                    pass
                    l_1_status = 'Disabled'
                    _loop_vars['status'] = l_1_status
                yield '| '
                yield str(environment.getattr(l_1_vrf, 'name'))
                yield ' | '
                yield str((undefined(name='status') if l_1_status is missing else l_1_status))
                yield ' |\n'
            l_1_vrf = l_1_status = missing
        yield '\n#### Management SSH Configuration\n\n```eos\n'
        template = environment.get_template('eos/management-ssh.j2', 'documentation/management-ssh.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {'ssh': l_0_ssh})):
            yield event
        yield '```\n'

blocks = {}
debug_info = '2=38&6=41&11=44&12=48&15=53&21=56&22=60&26=66&27=69&28=71&34=75&35=77&37=82&39=86&45=90&51=94&53=102&58=105&59=109&60=111&62=115&64=118&71=124'