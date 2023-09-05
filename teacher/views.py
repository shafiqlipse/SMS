from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import messages

from django.contrib.auth import login
from student.models import Student
from classroom.models import Classroom
from django.shortcuts import render, redirect
from .forms import (
    UserProfileForm,
    SignUpForm,
)
from .models import UserProfile


def register(request):
    if request.method == "POST":
        user_form = SignUpForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            login(request, user)
            return redirect("home")
    else:
        user_form = SignUpForm()
        profile_form = UserProfileForm()
    return render(
        request, "register.html", {"user_form": user_form, "profile_form": profile_form}
    )


# Create your views here.
def home(request):
    return render(request, "dashboard/dashboard.html")


# Create your views here.
@login_required(login_url="login")
def dash(request):
    context = {}
    return render(request, "dashboard/dashboard.html", context)


def search(request):
    # Handle the search logic and return search results
    if request.method == "GET":
        query = request.GET.get("search_query")
        category = request.GET.get("search_category")

        search_results = []

        if category == "students":
            search_results = Student.objects.filter(first_nam__icontains=query)
        elif category == "teachers":
            search_results = User.objects.filter(first_name__icontains=query)

        return render(
            request, "dashboard/search_results.html", {"search_results": search_results}
        )


def teachers(request):
    teachers = User.objects.filter(userprofile__role='Teacher')
    context = {"teachers": teachers}

    return render(request, "teacher/teachers.html", context)


@login_required(login_url="login")
def update_profile(request, id):
    user = User.objects.get(id=id)
    profile = user.userprofile

    if request.method == "POST":
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect(
                "profile", id=id
            )  # Redirect to the user's profile page after updating
    else:
        profile_form = UserProfileForm(instance=profile)

    return render(request, "teacher/updateteacher.html", {"profile_form": profile_form})


@login_required(login_url="login")
def view_profile(request, id):
    teacher = User.objects.get(id=id)
    teacherprofile = teacher.userprofile

    classes = teacherprofile.classes.all()
    subjects = teacherprofile.subjects.all()
    # assigned_tasks = Task.objects.filter(Assigned=teacher)
    profile = UserProfile.objects.get(user_id=id)

    context = {
        "teacher": teacher,
        "classes": classes,
        "subjects": subjects,
        "profile": profile,
        # 'assigned_tasks':assigned_tasks
    }
    return render(request, "teacher/teacher.html", context)


#
# page----------------------------------------------------------------------
# @login_required(login_url="login")
# def ProductUpdate(request, id):
#     band = Product.objects.get(id=id)

#     if request.method == "POST":
#         form = NewProductForm(request.POST, instance=band)
#         if form.is_valid():
#             form.save()

#             return redirect("products")
#     else:
#         form = NewProductForm(instance=band)
#     context = {"form": form}
#     return render(request, "Dashboard/newproduct.html", context)

# def editProfile(request):
#     user = request.user
#     teacher_profile = user.profile

#     if request.method == 'POST':
#         form = AttorneyProfileForm(request.POST, instance=teacher_profile)
#         if form.is_valid():
#             form.save()
#             return redirect('profile')  # Redirect to the profile page after saving
#     else:
#         form = AttorneyProfileForm(instance=teacher_profile)

#     return render(request, 'edit_profile.html', {'form': form})

# # # # Product update page-----------------------------------------------------------------------
# @login_required(login_url="login")
# def CategoryUpdate(request, id):
#     cat = Category.objects.get(id=id)

#     if request.method == "POST":
#         form = NewCatForm(request.POST, instance=cat)
#         if form.is_valid():
#             form.save()

#             return redirect("categories")
#     else:
#         form = NewProductForm(instance=cat)
#     context = {"form": form}
#     return render(request, "Dashboard/createCategory.html", context)


# # def (request,id):------------------------------------------------------------------
# @login_required(login_url="login")
# def Deleteproduct(request, id):
#     stud = Product.objects.get(id=id)
#     if request.method == "POST":
#         stud.delete()
#         return redirect("Products")

#     return render(request, "Dashboard/deleteProduct.html", {"obj": stud})


# #


def login_user(request):
    error_message = None  # Initialize error message as None
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # Authenticate
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In!")
            return redirect("home")
        else:
            return render(
                request,
                "login.html",
                {
                    "error_message": "Login failed - The username or password you entered is incorrect. Please try again.."
                },
            )
            # return redirect('login')
    else:
        return render(request, "login.html", {})
