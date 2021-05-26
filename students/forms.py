from django import forms
from django.forms import fields

from tasks.models import Student


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
            'is_updated',
            'is_offer_letter_issued',
            'is_completion_letter_issued'
        )