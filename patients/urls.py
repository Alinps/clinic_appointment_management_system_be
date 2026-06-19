from django.urls import path

from .views import (
    PatientCreateAPIView,
    PatientUpdateAPIView,
    PatientDeleteAPIView,
    PatientActivateAPIView,
    PatientListAPIView
    )

urlpatterns = [
    path("create/", PatientCreateAPIView.as_view(), name="patient-create"),
    path("<int:pk>/update/", PatientUpdateAPIView.as_view(), name="patient-update"),
    path("<int:pk>/delete/",PatientDeleteAPIView.as_view(),name="patient-name"),
    path("<int:pk>/activate/", PatientActivateAPIView.as_view(),name="patient-activate"),
    path("list/", PatientListAPIView.as_view(),name="patient-list"),

]