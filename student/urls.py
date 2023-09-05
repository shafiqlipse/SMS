from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import newStudent, StudentDetail, Deletestudent, Studentlist, StudentUpdate


urlpatterns = [
    path("newstudent/", newStudent, name="newstudent"),
    path("student/<int:id>", StudentDetail, name="student"),
    path("deletestudent", Deletestudent, name="deletestudent"),
    path("students/", Studentlist, name="students"),
    path("updatestudent/<int:id>", StudentUpdate, name="studentupdate"),
]
