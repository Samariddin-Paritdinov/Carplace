from django import template

register = template.Library()

@register.filter
def price_display(value):
    try:
        value = int(value)
        return "{:,.2f}".format(value / 100)
    except (TypeError, ZeroDivisionError):
        return "0.00"
