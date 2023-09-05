from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from teacher.views import home, search, login_user, register

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("search_results/", search, name="searchResults"),
    path("login/", login_user, name="login"),
    path("register/", register, name="register"),
    # included urls
    #    cases & client
    path("attendance/", include("attendance.urls")),
    path("classroom/", include("classroom.urls")),
    path("student/", include("student.urls")),
    path("teacher/", include("teacher.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
