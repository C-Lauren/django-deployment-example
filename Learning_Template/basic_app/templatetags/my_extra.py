from django import template

register = template.Library()

@register.filter(name='cutit')
def cutit(value,arg):
    """
    This cuts out all 'arg' from the string!
    """
    return value.replace(arg,'')
