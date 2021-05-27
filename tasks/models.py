from django.db import models
from django.contrib.auth.models import AbstractUser


PROFILE_CHOICES = (
    ('Developer', 'Developer'),
    ('AI', 'AI'),
)

ASSIGNED_TO_CHOICES = (
    ('Rekha', 'Rekha'),
    ('test', 'test'),
)


class User(AbstractUser):
    is_admin = models.BooleanField(default=True)
    phone_number = models.CharField(max_length=10)


class Task(models.Model):
    project_name = models.CharField(max_length=100)
    task_name = models.CharField(max_length=200)
    student = models.ForeignKey("Student", null=True, blank=True, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return f"{self.project_name} : {self.task_name}"


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(blank=True, max_length=100, default='')
    phone_number = models.CharField(max_length=10)
    email = models.EmailField()
    college_name = models.ForeignKey("College" ,blank=True, null=True, on_delete=models.SET_NULL)
    college_roll_number = models.CharField(max_length=20)
    profile = models.CharField(max_length=100, choices=PROFILE_CHOICES)
    assigned_to = models.CharField(max_length=100, choices=ASSIGNED_TO_CHOICES)
    joining_date = models.DateField(blank=True, null=True)
    offer_letter_issue_date = models.DateField(blank=True, null=True)
    completion_letter_issue_date = models.DateField(blank=True, null=True)
    is_updated = models.BooleanField("is_updated", default=False)
    is_offer_letter_issued = models.BooleanField("is_offer_letter_issued", default=False)
    is_completion_letter_issued = models.BooleanField("is_completion_letter_issued", default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.college_roll_number}"


class College(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    def __str__(self):
        return self.name