from django.urls import path

from .views import (DoctorCreateAPIView, DoctorUpdateAPIView, DoctorDeactivateAPIView)

urlpatterns = [
    path("create/",DoctorCreateAPIView.as_view(),name="doctor-create"),
    path("update/<int:pk>/",DoctorUpdateAPIView.as_view(), name="doctor-update"),
    path("<int:pk>/delete/",DoctorDeactivateAPIView.as_view(), name="doctor-delete")
]