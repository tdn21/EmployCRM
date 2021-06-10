import datetime
from builtins import staticmethod

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

DURATION_CHOICES=(
    ('0','0'),
    ('1','1'),
    ('2','2'),
    ('4','4'),
    ('6','6'),
)

GENDER_CHOICES=(
    ('Male','Male'),
    ('Female','Female'),
    ('Others','Others'),
)
STATUS_PROJECT_CHOICES=(
    ('Incomplete','Incomplete'),
    ('Partially Completed','Partially Completed'),
    ('Completed','Completed'),
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
    #fields related to Student Information
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(blank=True, max_length=100, default='')
    gender=models.CharField(max_length=10,choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField()
    college_name = models.ForeignKey("College" ,blank=True, null=True, on_delete=models.SET_NULL)
    college_roll_number = models.CharField(max_length=20)
    profile = models.CharField(max_length=100, choices=PROFILE_CHOICES)
    assigned_to = models.CharField(max_length=100, choices=ASSIGNED_TO_CHOICES)
    duration=models.CharField(max_length=2,choices=DURATION_CHOICES)
    #date Fields
    joining_date = models.DateField(blank=True, null=True)
    offer_letter_issue_date = models.DateField(blank=True, null=True)
    completion_letter_issue_date = models.DateField(blank=True, null=True)
    internship_completion_date=models.DateField(blank=True,null=True)
    #data related to internship
    no_of_absents=models.IntegerField(default=0)
    status_of_project=models.CharField(max_length=100,choices=STATUS_PROJECT_CHOICES,default="Incomplete")
    #boolean fields
    is_updated = models.BooleanField("is_updated", default=False)
    #boolean fields related to offer letter
    request_for_offer_letter=models.BooleanField("request_for_offer_letter",default=False)
    is_offer_letter_issued = models.BooleanField("is_offer_letter_issued", default=False)
    enable_offer_letter_download = models.BooleanField("enable_offer_letter_download", default=False)
    # boolean fields related to completion letter
    request_for_completion_letter=models.BooleanField("request_for_completion_letter",default=False)
    is_completion_letter_issued = models.BooleanField("is_completion_letter_issued", default=False)
    enable_completion_letter_download = models.BooleanField("enable_completion_letter_download", default=False)
    #boolean field for urgent approval for download completion letter
    enable_completion_letter_download_urgent=models.BooleanField("enable_completion_letter_download_urgent", default=False)

    @staticmethod
    def get_student_object_by_user(user):
        student=Student.objects.get(user=user)
        return student

    def is_properly_updated(self):
        if (not self.gender) or (not self.duration) or (not self.first_name) or (not self.last_name) or (not self.phone_number) or (not self.email) or (not self.college_name) or (not self.assigned_to) or (not self.college_roll_number) or (not self.profile) or (not self.offer_letter_issue_date) or (not self.joining_date):
            return False
        return True

    def get_end_date(self):
        joining_date = self.joining_date
        internship_duration = (int(self.duration)) * 30
        no_absents = (int(self.no_of_absents))
        days = internship_duration + no_absents;
        end_date = joining_date + datetime.timedelta(days=days)
        return end_date


    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.college_roll_number}"


class College(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    def __str__(self):
        return self.name