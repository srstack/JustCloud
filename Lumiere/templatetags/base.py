from django import template

register = template.Library()


@register.filter
def key(data_dict, type):
    return data_dict.get(type).items()


