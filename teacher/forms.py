from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile
from classroom.models import Classroom
from subject.models import Subject


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        label="",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Email Address"}
        ),
    )
    first_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "First Name"}
        ),
    )
    last_name = forms.CharField(
        label="",
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Last Name"}
        ),
    )

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["username"].widget.attrs["placeholder"] = "User Name"
        self.fields["username"].label = ""
        self.fields[
            "username"
        ].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password1"].widget.attrs["placeholder"] = "Password"
        self.fields["password1"].label = ""
        self.fields[
            "password1"
        ].help_text = "<ul class=\"form-text text-muted small\"><li>Your password can't be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can't be a commonly used password.</li><li>Your password can't be entirely numeric.</li></ul>"

        self.fields["password2"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["placeholder"] = "Confirm Password"
        self.fields["password2"].label = ""
        self.fields[
            "password2"
        ].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'

class UserProfileForm(forms.ModelForm):
    classes = forms.ModelMultipleChoiceField(
        queryset=Classroom.objects.all(),  # Replace with your queryset
        widget=forms.CheckboxSelectMultiple,
        required=False,  # Mark as required or not based on your needs
    )

    subjects = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.all(),  # Replace with your queryset
        widget=forms.CheckboxSelectMultiple,
        required=False,  # Mark as required or not based on your needs
    )

    class Meta:
        model = UserProfile
        fields = (
            "first_name",
            "last_name",
            "bio",
            "profile_picture",
            "classes",
            "subjects",
            "phone",
            "role",
            "address",'gender',
            "languages",
            "interests",
            "memberships",
        )

SEARCH_CHOICES = [
    ("students", "Students"),
    ("teachers", "Students"),
]


class SearchForm(forms.Form):
    search_query = forms.CharField(max_length=100, label="Search")
    search_category = forms.ChoiceField(choices=SEARCH_CHOICES, label="Search Category")
