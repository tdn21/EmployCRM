import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


ASSIGNED_TO_CHOICES = (
    ('Rekha', 'Rekha'),
    ('test', 'test'),
    ('test_1', 'test_1'),
)


GENDER_CHOICES=(
    ('Male','Male'),
    ('Female','Female'),
    ('Others','Others'),
)


class User(AbstractUser):
    is_admin = models.BooleanField(default=True)
    phone_number = models.CharField(max_length=10)
    college_name = models.ForeignKey("College", blank=True, null=True, on_delete=models.SET_NULL)
    college_roll_number = models.CharField(max_length=20)
    gender=models.CharField(max_length=10,choices=GENDER_CHOICES)
    profile = models.ForeignKey("Profile", blank=True, null=True, on_delete=models.SET_NULL)
    assigned_to = models.CharField(max_length=100, choices=ASSIGNED_TO_CHOICES)
    duration = models.IntegerField(blank=True, null=True, default=2)
    leaves = models.IntegerField(blank=True, null=True, default=0)
    joining_date = models.DateField(blank=True, null=True)
    offer_letter_issue_date = models.DateField(blank=True, null=True)
    completion_letter_issue_date = models.DateField(blank=True, null=True)
    internship_completion_date = models.DateField(blank=True, null=True)
    is_updated = models.BooleanField("is_updated", default=False)
    is_offer_letter_requested = models.BooleanField("is_offer_letter_requested", default=False)
    is_completion_letter_requested = models.BooleanField("is_completion_letter_requested", default=False)
    is_offer_letter_issued = models.BooleanField("is_offer_letter_issued", default=False)
    is_completion_letter_issued = models.BooleanField("is_completion_letter_issued", default=False)
    is_completion_letter_denied = models.BooleanField("is_completion_letter_denied", default=False)
    feedback = models.TextField()

    def get_end_date(self):
        joining_date = self.joining_date
        internship_duration = (int(self.duration)) * 30
        no_absents = (int(self.leaves))
        days = internship_duration + no_absents
        end_date = joining_date + datetime.timedelta(days=days)
        return end_date

    def __str__(self):
        username = self.username
        if self.is_admin:
            username = username + ' (admin)'
        return username


class College(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Link(models.Model):
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=250)
    description = models.TextField()
    profile = models.ForeignKey("Profile", blank=True, null=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Profile(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.name}"


class Messages(models.Model):
    origin = models.ForeignKey("User", related_name="origin", on_delete=models.CASCADE)
    destination = models.ForeignKey("User", related_name="destination", on_delete=models.CASCADE)
    message = models.TextField()
    date = models.DateTimeField(default=timezone.now)