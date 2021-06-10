import datetime

from django import template
from tasks.models import Student


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
def check_internship_completed(student):
    today_date=datetime.date.today()
    joining_date=student.joining_date
    internship_duration=(int(student.duration))*30
    no_absents=(int(student.no_of_absents))
    delta=today_date-joining_date
    if (delta.days-no_absents>=internship_duration):
        return True
    else:
        return False