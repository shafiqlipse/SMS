from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Classroom(models.Model):
    name = models.CharField(max_length=100)
    class_teacher = models.ForeignKey(
        User, related_name="classteacher", blank=True,null=True, on_delete=models.CASCADE
    )
    description = models.TextField()

    def __str__(self):
        return self.name
