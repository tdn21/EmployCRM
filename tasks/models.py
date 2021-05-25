from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_admin = models.BooleanField(default=True)
    is_student = models.BooleanField(default=False)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Task(models.Model):
    project_name = models.CharField(max_length=100)
    task_name = models.CharField(max_length=200)
    student = models.ForeignKey("Student", null=True, blank=True, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return f"{self.project_name} {self.task_name}"


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(blank=True, null=True, max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    college_name = models.CharField(max_length=200)
    college_roll_number = models.CharField(max_length=20)
    profile = models.CharField(max_length=100)
    assigned_to = models.CharField(max_length=100)
    joining_date = models.CharField(max_length=20)
    offer_letter_issue_date = models.CharField(blank=True, null=True, max_length=20)
    completion_letter_issue_date = models.CharField(blank=True, null=True, max_length=20)
    is_updated = models.BooleanField("is_updated", default=False)
    is_offer_letter_issued = models.BooleanField("is_offer_letter_issued", default=False)
    is_completion_letter_issued = models.BooleanField("is_completion_letter_issued", default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.user.email}"



def post_user_created_signal(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(post_user_created_signal, sender=User)


class College(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
