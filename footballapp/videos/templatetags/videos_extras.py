from django import template

register = template.Library()

@register.filter
def zip_lists(a, b):
    """Custom template filter to zip two lists."""
    return zip(a, b)
