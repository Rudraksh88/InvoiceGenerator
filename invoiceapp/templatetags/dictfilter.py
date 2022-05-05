from django.template.defaultfilters import register

@register.filter
def key(d, key_name):
    if str(key_name) in d:
        return d[str(key_name)]
    else:
        return '-'
key = register.filter('key', key)