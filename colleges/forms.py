from django import forms
from tasks.models import College


class CollegeModelForm(forms.ModelForm):
    class Meta:
        model = College
        fields = (
            'name',
            'city',
            'state'
        )