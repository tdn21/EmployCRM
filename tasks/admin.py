from django.contrib import admin

from .models import User, UserProfile, Task, Student

# Register your models here.
admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Task)
admin.site.register(Student)