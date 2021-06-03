from django import forms
from students.models import Profile


class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'name',
            'description'
        )