from django.urls import path

from .views import (
    LoginAPIView,
    ReceptionistCreateAPIView
)

urlpatterns = [
    path("admin/login/",LoginAPIView.as_view(),name="login"),
    path("receptionists/",ReceptionistCreateAPIView.as_view(),name="create-receptionist"),
]