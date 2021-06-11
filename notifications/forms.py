from django import forms
from django.contrib.auth import get_user_model
from students.models import Message


User = get_user_model()


class AdminCreateMessageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AdminCreateMessageForm, self).__init__(*args, **kwargs)
        self.fields['destination'].queryset = User.objects.filter(is_admin = False)

    class Meta:
        model = Message
        fields = (
            'destination',
            'message'
        )


class StudentCreateMessageForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(StudentCreateMessageForm, self).__init__(*args, **kwargs)
        self.fields['destination'].queryset = User.objects.filter(is_admin = True)

    class Meta:
        model = Message
        fields = (
            'destination',
            'message'
        )


class CreateMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = (
            'message',
        )