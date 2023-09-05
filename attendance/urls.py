from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import mark_attendance,attendance_report


urlpatterns = [

    path('attendance/', mark_attendance,name='attendance'),
    
    path('attendance_report/', attendance_report, name='attendance_report'),
    
  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
