from datetime import datetime

from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from accounts.permissions import IsAdminOrReceptionist

from doctors.models import Doctor

from .service import generate_slots


class AvailableSlotsAPIView(APIView):

    permission_classes = [IsAdminOrReceptionist]

    def get(self,request, pk):

        appointment_date = request.query_params.get("date")

        if not appointment_date:

            return Response(
                {
                    "success":False,
                    "message":"Date is required"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:

            appointment_date = datetime.strptime(appointment_date,"%Y-%m-%d").date()

        except ValueError:
            
            return Response(
                {
                    "success":False,
                    "message":"Invalid date format."
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        
        doctor = get_object_or_404(Doctor,pk=pk)

        slots = generate_slots(doctor,appointment_date)

        return Response(
            {
                "success":True,
                "doctor":doctor.name,
                "appointment_date":appointment_date,
                "available_slots":slots
            },
            status=status.HTTP_200_OK
        )



