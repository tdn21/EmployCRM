from django import forms
from django import forms
from django.contrib.auth import get_user_model

from tasks.models import Student


User = get_user_model()


profile_choices = (
    ("Developer", "Developer"),
    ("AI", "AI")
)


class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = (
            'first_name',
            'last_name',
            'phone_number',
            'email',
            'college_name',
            'college_roll_number',
            'profile',
            'assigned_to',
            'joining_date',
            'offer_letter_issue_date',
            'completion_letter_issue_date',
            # 'is_updated',
            'is_offer_letter_issued',
            'is_completion_letter_issued'
        )
        widgets = {
            'joining_date': forms.DateInput(format=('%Y-%m-%d'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'offer_letter_issue_date': forms.DateInput(format=('%Y-%m-%d'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'completion_letter_issue_date': forms.DateInput(format=('%Y-%m-%d'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            # 'Profile': forms.MultipleChoiceField(choices=profile_choices)
        }


class NewStudentModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'username',
            'phone_number',
            'email'
        )
        labels = {
            "username": "roll number"
        }