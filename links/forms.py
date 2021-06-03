from django import forms
from students.models import Link


class LinkModelForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = (
            'name',
            'link',
            'description',
            'profile'
        )