from django import forms
from tasks.models import Link


class LinkModelForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = (
            'name',
            'link',
            'description'
        )