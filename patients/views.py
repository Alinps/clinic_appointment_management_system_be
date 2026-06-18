from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from accounts.permissions import  IsAdminOrReceptionist

from .serializers import PatientSerializer
from .models import Patient


class PatientCreateAPIView(APIView):

    permission_classes=[IsAdminOrReceptionist]

    def post(self, request):

        serializer = PatientSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        patient = serializer.save()

        return Response(
            {
                "success": True,
                "message":"Patient created successfully",
                "data": serializer.data
            },
            status=status.HTTP_201_CREATED
        )
    


class PatientUpdateAPIView(APIView):

    permission_classes = [IsAdminOrReceptionist]

    def put(self, request, pk):

        patient = get_object_or_404(Patient,pk=pk)

        serializer = PatientSerializer(patient, data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(
            {
                "success":"True",
                "message": "Patient updated successfully.",
                "data":serializer.data
            },
            status=status.HTTP_200_OK
        )
    

    def patch(self, request, pk):

        patient = get_object_or_404(Patient, pk=pk)

        serializer = PatientSerializer(patient, data=request.data, partial=True)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(
            {
                "success":True,
                "message":"Patient updated successfully.",
                "data":serializer.data
            },
            status=status.HTTP_200_OK
        )
    
