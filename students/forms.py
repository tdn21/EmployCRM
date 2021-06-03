from django import forms
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField

User = get_user_model()


class StudentModelForm(forms.ModelForm):
    class Meta:
        model = User
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
        }


class NewStudentModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'college_roll_number',
            'phone_number',
            'email'
        )
        labels = {
            "college_roll_number": "roll number"
        }


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}