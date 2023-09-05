from django.db import models

# Create your models here.
# from .models import AttorneyProfile
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from classroom.models import Classroom
from subject.models import Subject


class UserProfile(models.Model):
    first_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )
    Gender = (
        ("Male", "Male"),
        ("Female", "Female"),
    )
    Roles = (
        ("Teacher", "Teacher"),
        ("Instructor", "Instructor"),
        ("Trainee", "Trainee"),
        ("Staff", "Staff"),
    )
    role = models.CharField(max_length=255, choices=Roles, null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add additional fields for the user profile
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(
        upload_to="teacher_pics/",
        blank=True,
        null=True,
    )
    classes = models.ManyToManyField(Classroom, related_name="classroom", blank=True)
    subjects = models.ManyToManyField(Subject, related_name="classroom", blank=True)
    phone = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    languages = models.CharField(max_length=255, null=True, blank=True)
    interests = models.CharField(max_length=255, null=True, blank=True)
    memberships = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=30, choices=Gender, blank=True, null=True)
    join_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username


# # # Create your models here.
# # from django.db import models
# # from django.contrib.auth.models import User
