from django import forms
from django.forms import fields
from .models import Task


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