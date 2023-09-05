from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import AttendanceForm
from .models import Attendance
from classroom.models import Classroom


def mark_attendance(request):
    if request.method == "POST":
        form = AttendanceForm(request.POST)
        if form.is_valid():
            student = form.cleaned_data["student"]
            status = form.cleaned_data["status"]
            date = form.cleaned_data["date"]

            # Create or update the attendance record for the selected student and date.
            Attendance.objects.update_or_create(
                student=student, date=date, defaults={"status": status}
            )
            return redirect(
                "attendance_report"
            )  # Redirect to a success page or another view.
    else:
        form = AttendanceForm()

    return render(request, "mark_attendace.html", {"form": form})


from .models import  Attendance
from django.db.models import Count


from django.db.models import Q

# ...

def attendance_report(request):
    # Query the database to get attendance data grouped by class.
    attendance_data = Attendance.objects.all()

    return render(request, 'attendance_report.html', {'attendance_data': attendance_data})
