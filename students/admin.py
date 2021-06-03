from django.contrib import admin

from .models import Link, Profile, User, College

# Register your models here.
admin.site.register(User)
admin.site.register(College)
admin.site.register(Profile)
admin.site.register(Link)