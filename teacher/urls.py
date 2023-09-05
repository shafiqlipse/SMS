from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from .views import home, view_profile, update_profile, teachers

urlpatterns = [
    path("", home, name="home"),
    path("profile/<int:id>", view_profile, name="profile"),
    path("profile_update/<int:id>", update_profile, name="profile_update"),
    path("teachers/", teachers, name="teachers"),
    # included urls
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
