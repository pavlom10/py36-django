from django import template

register = template.Library()

@register.filter()
def my_background(value):
    try:
        value = float(value)
        if value < 0:
            return '#0f7003'
        elif 1 <= value < 2:
            return '#fbc8c9'
        elif 2 <= value < 5:
            return '#f6777a'
        elif value >= 5:
            return '#fb0407'
        else:
            return '#fff'

    except ValueError:
        return '#fff'




