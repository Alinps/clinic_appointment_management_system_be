from django.urls import path

from .views import (ClinicSettingsAPIView)

urlpatterns = [
    path("clinic-settings/",ClinicSettingsAPIView.as_view(), name="clinic-settings")
]