from django import template

register = template.Library()


@register.filter
def key(data_dict, type):
    return data_dict.get(type).items()


@register.filter
def data(device):
    if device.date.fiter(model=0):
        return True
    else:
        return False
