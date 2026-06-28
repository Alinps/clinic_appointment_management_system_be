from django.urls import path

from .views import (AvailableSlotsAPIView)

urlpatterns = [
    path("doctor/<int:pk>/available-slots/", AvailableSlotsAPIView.as_view(), name="available-slots",)
    

]