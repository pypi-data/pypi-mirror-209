from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/dhcp-relay.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_dhcp_relay = resolve('dhcp_relay')
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
    if t_2((undefined(name='dhcp_relay') if l_0_dhcp_relay is missing else l_0_dhcp_relay)):
        pass
        yield '!\ndhcp relay\n'
        for l_1_server in t_1(environment.getattr((undefined(name='dhcp_relay') if l_0_dhcp_relay is missing else l_0_dhcp_relay), 'servers')):
            _loop_vars = {}
            pass
            yield '   server '
            yield str(l_1_server)
            yield '\n'
        l_1_server = missing
        if t_2(environment.getattr((undefined(name='dhcp_relay') if l_0_dhcp_relay is missing else l_0_dhcp_relay), 'tunnel_requests_disabled'), True):
            pass
            yield '   tunnel requests disabled\n'
        elif t_2(environment.getattr((undefined(name='dhcp_relay') if l_0_dhcp_relay is missing else l_0_dhcp_relay), 'tunnel_requests_disabled'), False):
            pass
            yield '   no tunnel requests disabled\n'

blocks = {}
debug_info = '2=24&5=27&6=31&8=34&10=37'