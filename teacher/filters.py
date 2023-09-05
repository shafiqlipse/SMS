import django_filters

from .models import *


class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = UserProfile
        fields = ("last_name", "first_name", "classroom", "gender")
