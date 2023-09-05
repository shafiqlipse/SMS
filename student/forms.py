from django import forms
from .models import Student


class NewStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = (
            "first_name",
            "last_name",
            "gender",
            "passport_picture",
            "classroom",
            "date_of_birth",
            "Guardian",
            "occupation",
            "other_contact",
            "phone",
            "email",
            "address",
            "interests",
        )


# class NewReviewForm(forms.ModelForm):
#     class Meta:
#         model = Review
#         fields = ["body"]
