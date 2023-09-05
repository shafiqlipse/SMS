from django.db import models
from classroom.models import Classroom

# Create your models here.


class Student(models.Model):
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

    # user = models.OneToOneField(User, on_delete=models.CASCADE)

    passport_picture = models.ImageField(
        upload_to="profile_pics/",
        blank=True,
        null=True,
        default="http://localhost:8000/static/images/profile.png",
    )
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    interests = models.CharField(max_length=255, null=True, blank=True)
    Guardian = models.CharField(max_length=255, null=True, blank=True)
    occupation = models.CharField(max_length=255, null=True, blank=True)
    other_contact = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=30, choices=Gender, blank=True, null=True)
    join_date = models.DateField(auto_now_add=True)
    date_of_birth = models.DateField()

    def __str__(self):
        return self.first_name
