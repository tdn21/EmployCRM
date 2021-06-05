from django import forms
from students.models import College


class CollegeModelForm(forms.ModelForm):
    class Meta:
        model = College
        fields = (
            'name',
            'city',
            'state'
        )