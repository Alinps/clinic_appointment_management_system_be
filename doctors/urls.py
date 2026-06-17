from django.urls import path

from .views import (
    DoctorCreateAPIView, 
    DoctorUpdateAPIView, 
    DoctorDeactivateAPIView,
    DoctorDetailAPIView
    
    )

urlpatterns = [
    path("create/",DoctorCreateAPIView.as_view(),name="doctor-create"),
    path("update/<int:pk>/",DoctorUpdateAPIView.as_view(), name="doctor-update"),
    path("<int:pk>/delete/",DoctorDeactivateAPIView.as_view(), name="doctor-delete"),
    path("<int:pk>/details/",DoctorDetailAPIView.as_view(), name="doctor-details")
]