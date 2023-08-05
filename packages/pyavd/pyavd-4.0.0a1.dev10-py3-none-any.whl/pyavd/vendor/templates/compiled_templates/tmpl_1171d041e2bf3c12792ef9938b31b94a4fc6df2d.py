from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'documentation/management.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_management_interfaces = resolve('management_interfaces')
    l_0_dns_domain = resolve('dns_domain')
    l_0_domain_list = resolve('domain_list')
    l_0_ip_name_servers = resolve('ip_name_servers')
    l_0_name_server = resolve('name_server')
    l_0_ip_domain_lookup = resolve('ip_domain_lookup')
    l_0_clock = resolve('clock')
    l_0_ntp = resolve('ntp')
    l_0_ptp = resolve('ptp')
    l_0_system = resolve('system')
    l_0_management_ssh = resolve('management_ssh')
    l_0_management_tech_support = resolve('management_tech_support')
    l_0_ip_ssh_client_source_interfaces = resolve('ip_ssh_client_source_interfaces')
    l_0_management_api_gnmi = resolve('management_api_gnmi')
    l_0_management_cvx = resolve('management_cvx')
    l_0_management_console = resolve('management_console')
    l_0_management_api_http = resolve('management_api_http')
    l_0_management_api_models = resolve('management_api_models')
    l_0_ip_http_client_source_interfaces = resolve('ip_http_client_source_interfaces')
    try:
        t_1 = environment.tests['arista.avd.defined']
    except KeyError:
        @internalcode
        def t_1(*unused):
            raise TemplateRuntimeError("No test named 'arista.avd.defined' found.")
    pass
    if ((((((((((((((((((t_1((undefined(name='management_interfaces') if l_0_management_interfaces is missing else l_0_management_interfaces)) or t_1((undefined(name='dns_domain') if l_0_dns_domain is missing else l_0_dns_domain))) or t_1((undefined(name='domain_list') if l_0_domain_list is missing else l_0_domain_list))) or t_1((undefined(name='ip_name_servers') if l_0_ip_name_servers is missing else l_0_ip_name_servers))) or t_1((undefined(name='name_server') if l_0_name_server is missing else l_0_name_server))) or t_1((undefined(name='ip_domain_lookup') if l_0_ip_domain_lookup is missing else l_0_ip_domain_lookup))) or t_1((undefined(name='clock') if l_0_clock is missing else l_0_clock))) or t_1((undefined(name='ntp') if l_0_ntp is missing else l_0_ntp))) or t_1((undefined(name='ptp') if l_0_ptp is missing else l_0_ptp))) or t_1((undefined(name='system') if l_0_system is missing else l_0_system))) or t_1((undefined(name='management_ssh') if l_0_management_ssh is missing else l_0_management_ssh))) or t_1((undefined(name='management_tech_support') if l_0_management_tech_support is missing else l_0_management_tech_support))) or t_1((undefined(name='ip_ssh_client_source_interfaces') if l_0_ip_ssh_client_source_interfaces is missing else l_0_ip_ssh_client_source_interfaces))) or t_1((undefined(name='management_api_gnmi') if l_0_management_api_gnmi is missing else l_0_management_api_gnmi))) or t_1((undefined(name='management_cvx') if l_0_management_cvx is missing else l_0_management_cvx))) or t_1((undefined(name='management_console') if l_0_management_console is missing else l_0_management_console))) or t_1((undefined(name='management_api_http') if l_0_management_api_http is missing else l_0_management_api_http))) or t_1((undefined(name='management_api_models') if l_0_management_api_models is missing else l_0_management_api_models))) or t_1((undefined(name='ip_http_client_source_interfaces') if l_0_ip_http_client_source_interfaces is missing else l_0_ip_http_client_source_interfaces))):
        pass
        yield '\n## Management\n'
        template = environment.get_template('documentation/management-interfaces.j2', 'documentation/management.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/dns-domain.j2', 'documentation/management.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/domain-list.j2', 'documentation/management.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/ip-name-servers.j2', 'documentation/management.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/ip-domain-lookup.j2', 'documentation/management.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/clock.j2', 'documentation/management.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/ntp.j2', 'documentation/management.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/ptp.j2', 'documentation/management.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/system.j2', 'documentation/management.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/management-ssh.j2', 'documentation/management.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/management-tech-support.j2', 'documentation/management.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/ip-ssh-client-source-interfaces.j2', 'documentation/management.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/management-api-gnmi.j2', 'documentation/management.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/management-cvx.j2', 'documentation/management.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/management-console.j2', 'documentation/management.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/management-api-http.j2', 'documentation/management.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/management-api-models.j2', 'documentation/management.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event
        template = environment.get_template('documentation/ip-http-client-source-interfaces.j2', 'documentation/management.j2')
        for event in template.root_render_func(template.new_context(context.get_all(), True, {})):
            yield event

blocks = {}
debug_info = '2=36&24=39&26=42&28=45&30=48&32=51&34=54&36=57&38=60&40=63&42=66&44=69&46=72&48=75&50=78&52=81&54=84&56=87&58=90'