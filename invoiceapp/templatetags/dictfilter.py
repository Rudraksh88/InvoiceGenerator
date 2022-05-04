from django.template.defaultfilters import register

@register.filter
def key(d, key_name):
    return d[str(key_name)]
key = register.filter('key', key)