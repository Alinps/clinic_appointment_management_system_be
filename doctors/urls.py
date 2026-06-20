from django.urls import path

from .views import (
    DoctorCreateAPIView, 
    DoctorUpdateAPIView, 
    DoctorDeactivateAPIView,
    DoctorActivateAPIView,
    DoctorDetailAPIView,
    DoctorListAPIVIew,
    DoctorAvailabitlyCreateAPIView,
    DoctorLeaveCreateAPIView,
    DoctorLeaveUpateAPIView,
    DoctorLeaveDeleteAPIView,
    DoctorLeaveListAPIView
    
    )

urlpatterns = [
    path("create/",DoctorCreateAPIView.as_view(),name="doctor-create"),
    path("update/<int:pk>/",DoctorUpdateAPIView.as_view(), name="doctor-update"),
    path("<int:pk>/delete/",DoctorDeactivateAPIView.as_view(), name="doctor-delete"),
    path("<int:pk>/details/",DoctorDetailAPIView.as_view(), name="doctor-details"),
    path("<int:pk>/activate/",DoctorActivateAPIView.as_view(),name="doctor-activate"),
    path("list/", DoctorListAPIVIew.as_view(), name="doctor-list"),
    path("<int:pk>/availability/",DoctorAvailabitlyCreateAPIView.as_view(),name="doctor-availability"),
    path("<int:pk>/leave/", DoctorLeaveCreateAPIView.as_view(), name="doctor-leave"),
    path("<int:pk>/leave/update/", DoctorLeaveUpateAPIView.as_view(), name="doctor-leave-update"),
    path("<int:pk>/leave/delete/",DoctorLeaveDeleteAPIView.as_view(), name="doctor-leave-cancel"),
    path("leave/list/", DoctorLeaveListAPIView.as_view(), name="doctor-leave-list")
]