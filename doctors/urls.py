from django.urls import path

from .views import DoctorCreateAPIView

urlpatterns = [
    path("create/",DoctorCreateAPIView.as_view(),name="doctor-create"),
]