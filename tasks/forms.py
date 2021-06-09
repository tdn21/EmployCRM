from django import forms
from django.forms import fields
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField

from .models import Task

User = get_user_model()


class TaskModelForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = (
            'project_name',
            'task_name',
            'description',
        )


class TaskForm(forms.Form):
    project_name = forms.CharField(max_length=100)
    task_name = forms.CharField(max_length=200)
    description = forms.CharField(max_length=1000)


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}