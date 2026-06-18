from django.urls import path

from .views import (PatientCreateAPIView, PatientUpdateAPIView)

urlpatterns = [
    path("create/", PatientCreateAPIView.as_view(), name="patient-create"),
    path("<int:pk>/update/", PatientUpdateAPIView.as_view(), name="patient-update")
]