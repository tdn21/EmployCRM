import datetime

from django import template
from django.contrib.auth import get_user_model

User = get_user_model()


register = template.Library()

@register.filter(name='upperCase')
def upperCase(str):
    return str.upper()

@register.filter(name='lowerCase')
def lowerCase(str):
    return str.lower()

@register.filter(name='concat')
def concat(str1,str2):
    return str1+" "+str2

@register.filter(name='his_or_her')
def his_or_her(gender):
    if gender=="Male":
        return "His"
    else:
        return "Her"

@register.filter(name='him_or_her')
def him_or_her(gender):
    if gender=="Male":
        return "Him"
    else:
        return "Her"


@register.filter(name='check_internship_completed')
def check_internship_completed(user):
    today_date=datetime.date.today()
    joining_date=user.joining_date
    internship_duration=(int(user.duration))*30
    no_absents=(int(user.leaves))
    delta=today_date-joining_date
    if (delta.days-no_absents>=internship_duration):
        return True
    else:
        return False