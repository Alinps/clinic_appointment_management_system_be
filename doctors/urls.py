from django.urls import path

from .views import (
    DoctorCreateAPIView, 
    DoctorUpdateAPIView, 
    DoctorDeactivateAPIView,
    DoctorActivateAPIView,
    DoctorDetailAPIView,
    DoctorListAPIVIew,
    DoctorAvailabitlyCreateAPIView
    
    )

urlpatterns = [
    path("create/",DoctorCreateAPIView.as_view(),name="doctor-create"),
    path("update/<int:pk>/",DoctorUpdateAPIView.as_view(), name="doctor-update"),
    path("<int:pk>/delete/",DoctorDeactivateAPIView.as_view(), name="doctor-delete"),
    path("<int:pk>/details/",DoctorDetailAPIView.as_view(), name="doctor-details"),
    path("<int:pk>/activate/",DoctorActivateAPIView.as_view(),name="doctor-activate"),
    path("list/", DoctorListAPIVIew.as_view(), name="doctor-list"),
    path("<int:pk>/availability/",DoctorAvailabitlyCreateAPIView.as_view(),name="doctor-availability"),
]