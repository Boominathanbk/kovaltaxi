from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    try:
        value = float(value)  # Convert to float if it’s a string
        arg = float(arg)
        return value * arg
    except (ValueError, TypeError):
        return ''