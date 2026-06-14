from django.urls import path

from .views import LoginAPIView

urlpatterns = [
    path("admin/login/",LoginAPIView.as_view(),name="login"),
]