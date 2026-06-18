from django.urls import path

from .views import (PatientCreateAPIView)

urlpatterns = [
    path("create/", PatientCreateAPIView.as_view(), name="patient-create")
]