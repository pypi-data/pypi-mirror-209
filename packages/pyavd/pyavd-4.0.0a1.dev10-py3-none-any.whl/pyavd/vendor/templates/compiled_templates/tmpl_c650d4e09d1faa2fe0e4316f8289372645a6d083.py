from jinja2.runtime import LoopContext, Macro, Markup, Namespace, TemplateNotFound, TemplateReference, TemplateRuntimeError, Undefined, escape, identity, internalcode, markup_join, missing, str_join
name = 'eos/management-security.j2'

def root(context, missing=missing):
    resolve = context.resolve_or_missing
    undefined = environment.undefined
    concat = environment.concat
    cond_expr_undefined = Undefined
    if 0: yield None
    l_0_management_security = resolve('management_security')
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
    if t_2((undefined(name='management_security') if l_0_management_security is missing else l_0_management_security)):
        pass
        yield '!\nmanagement security\n'
        if t_2(environment.getattr((undefined(name='management_security') if l_0_management_security is missing else l_0_management_security), 'entropy_source')):
            pass
            yield '   entropy source '
            yield str(environment.getattr((undefined(name='management_security') if l_0_management_security is missing else l_0_management_security), 'entropy_source'))
            yield '\n'
        if t_2(environment.getattr(environment.getattr((undefined(name='management_security') if l_0_management_security is missing else l_0_management_security), 'password'), 'encryption_key_common'), True):
            pass
            yield '   password encryption-key common\n'
        if t_2(environment.getattr(environment.getattr((undefined(name='management_security') if l_0_management_security is missing else l_0_management_security), 'password'), 'encryption_reversible')):
            pass
            yield '   password encryption reversible '
            yield str(environment.getattr(environment.getattr((undefined(name='management_security') if l_0_management_security is missing else l_0_management_security), 'password'), 'encryption_reversible'))
            yield '\n'
        if t_2(environment.getattr(environment.getattr((undefined(name='management_security') if l_0_management_security is missing else l_0_management_security), 'password'), 'minimum_length')):
            pass
            yield '   password minimum length '
            yield str(environment.getattr(environment.getattr((undefined(name='management_security') if l_0_management_security is missing else l_0_management_security), 'password'), 'minimum_length'))
            yield '\n'
        for l_1_ssl_profile in t_1(environment.getattr((undefined(name='management_security') if l_0_management_security is missing else l_0_management_security), 'ssl_profiles')):
            _loop_vars = {}
            pass
            yield '   ssl profile '
            yield str(environment.getattr(l_1_ssl_profile, 'name'))
            yield '\n'
            if t_2(environment.getattr(l_1_ssl_profile, 'tls_versions')):
                pass
                yield '      tls versions '
                yield str(environment.getattr(l_1_ssl_profile, 'tls_versions'))
                yield '\n'
            if t_2(environment.getattr(l_1_ssl_profile, 'cipher_list')):
                pass
                yield '      cipher-list '
                yield str(environment.getattr(l_1_ssl_profile, 'cipher_list'))
                yield '\n'
            if t_2(environment.getattr(l_1_ssl_profile, 'certificate')):
                pass
                yield '      certificate '
                yield str(environment.getattr(environment.getattr(l_1_ssl_profile, 'certificate'), 'file'))
                yield ' key '
                yield str(environment.getattr(environment.getattr(l_1_ssl_profile, 'certificate'), 'key'))
                yield '\n'
        l_1_ssl_profile = missing

blocks = {}
debug_info = '2=24&5=27&6=30&8=32&11=35&12=38&14=40&15=43&17=45&18=49&19=51&20=54&22=56&23=59&25=61&26=64'