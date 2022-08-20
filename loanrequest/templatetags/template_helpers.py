from django.template import Library
from django.template.defaultfilters import stringfilter
from dateutil import parser
from datetime import datetime


register = Library()


@register.filter(is_safe=True)
@stringfilter
def format_id(value: str, type: str):
    if (type.upper() == 'C'):
        return f'{value[:3]}-{value[3:10:]}-{value[-1:]}'

    return value


@register.filter(is_safe=True)
def parse_date(value):
    # parse to datetime since built-in date filter doesn't work properly
    # when using TemplateHTMLRenderer, see the next link for reference
    # https://github.com/encode/django-rest-framework/discussions/8129
    # data needs to be parsed to datetime for the filter to work
    return parser.parse(value)


@register.simple_tag
def define(val=None):
  return val


@register.filter(is_safe=True)
def substract(x:int, y:int):
    return x - y


@register.filter(is_safe=True)
def add(x:int, y:int):
    return x + y

@register.filter(is_safe=True)
def multiply(x:int, y:int):
    return x * y

@register.filter(is_safe=True)
def calculate_age(value):
    born = parser.parse(value)
    today = datetime.today()
    age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    return age


@register.filter(is_safe=True)
def replace_none(value, replacement = ""):
    if (value is None):
        return replacement
    return value
