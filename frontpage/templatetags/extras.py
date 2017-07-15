from django import template
import json
from django.utils.safestring import mark_safe




register = template.Library()


@register.filter
def what_language(path, isChinese):
    return path if isChinese else path + "/eng"



@register.filter
def get_chinese_url(path):
    return path[:-4]