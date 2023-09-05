from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import login
from student.models import Student
from django.shortcuts import render, redirect
from .forms import NewStudentForm
from .filters import StudentFilter


# # Students details......................................................
def StudentDetail(request, id):
    student = get_object_or_404(Student, id=id)
    relatedstudents = Student.objects.filter(classroom=student.classroom).exclude(id=id)
    # comments = Comment.objects.filter(student=student).order_by('-Created')
    # new_comment = None
    # recent = Student.objects.all().order_by('-Created')[:10]
    # # new_comment_reply = None

    # if request.method == 'POST':
    #     cform = NewCommentForm(request.POST, request.FILES)

    #     if cform.is_valid():
    #         new_comment = cform.save(commit=False)
    #         new_comment.student = student
    #         new_comment.author = request.user
    #         new_comment.save()
    #         return HttpResponseRedirect(reverse('studentDetail',args=[int(pk)]))
    # else:
    #     cform = NewCommentForm()

    context = {"student": student, "relatedstudents": relatedstudents}

    return render(request, "student/student.html", context)


# create new student.....................................................
# @login_required(login_url='login')
def newStudent(request):
    if request.method == "POST":
        form = NewStudentForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("students")
    else:
        form = NewStudentForm()

    return render(request, "student/newstudent.html", {"form": form})


# students list


# @login_required(login_url='login')
def Studentlist(request):
    students = Student.objects.all()
    myFilter = StudentFilter(request.GET, queryset=students)
    studentlist = myFilter.qs
    paginator = Paginator(studentlist, 10)  # Show 10 posts per page

    page = request.GET.get("page")
    try:
        studs = paginator.page(page)
    except PageNotAnInteger:
        studs = paginator.page(1)
    except EmptyPage:
        studs = paginator.page(paginator.num_pages)
    context = {"studs": studs, "myFilter": myFilter, "studentlist": studentlist}
    return render(request, "student/students.html", context)


# # Student update page-----------------------------------------------------------------------
# @login_required(login_url='login')
def StudentUpdate(request, id):
    band = Student.objects.get(id=id)

    if request.method == "POST":
        form = NewStudentForm(request.POST,request.FILES, instance=band)
        if form.is_valid():
            form.save()

            return redirect("student", id=id)
    else:
        form = NewStudentForm(instance=band)
    context = {"form": form}
    return render(request, "student/updatestudent.html", context)


# delete (request,id):------------------------------------------------------------------
# @login_required(login_url='login')
def Deletestudent(request, id):
    stud = Student.objects.get(id=id)
    if request.method == "POST":
        stud.delete()
        return redirect("Students")

    return render(request, "student/deleteStudent.html", {"obj": stud})
