from django.contrib import admin

from .models import Link, Profile, User, Task, Student, College

# Register your models here.
admin.site.register(User)
admin.site.register(Task)
admin.site.register(Student)
admin.site.register(College)
admin.site.register(Profile)
admin.site.register(Link)