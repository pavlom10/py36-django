from django import template
from datetime import datetime


register = template.Library()


@register.filter
def format_date(value):
    now = datetime.now().timestamp()
    sec_ago = now - value

    if sec_ago < 10 * 60:
        value = 'Только что'
    elif sec_ago < 24 * 60 * 60:
        hour = round(sec_ago / 60 / 60)
        value = str(hour) + ' часов назад'
    else:
        date_time = datetime.fromtimestamp(value)
        value = date_time.strftime("%Y-%m-%d")

    return value


@register.filter
def format_score(value, default):
    if value is None:
        return default

    if value < -5:
        value = 'Все плохо'
    elif -5 <= value < 5:
        value = 'Нейтрально'
    elif value > 5:
        value = 'Хорошо'

    return value


@register.filter
def format_num_comments(value):
    if value == 0:
        value = 'Оставьте комментарий'
    elif value > 50:
        value = '50+'

    return value


@register.filter
def format_selftext(value, count):
    words = value.split()
    if len(words) > count + count:
        s = ' '.join(words[:count]) + ' ... ' + ' '.join(words[-count:])
        return s

    return value



