from django import forms
from student.models import Student

class AttendanceForm(forms.Form):
    student = forms.ModelChoiceField(queryset=Student.objects.all(), empty_label="Select a student")
    status = forms.ChoiceField(choices=[('Present', 'Present'), ('Absent', 'Absent')])
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
