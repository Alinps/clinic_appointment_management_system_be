from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.permissions import IsAdmin

from .models import Doctor
from .serializers import DoctorSerializer


class DoctorCreateAPIView(APIView):

    permission_classes = [IsAdmin]

    def post(self, request):

        serializer = DoctorSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)

        doctor = serializer.save()

        return Response (
            {
                "success": True,
                "message": "Doctor created successfully",
                "data": serializer.data
            },
            status = status.HTTP_201_CREATED
        )
    

    



class DoctorUpdateAPIView(APIView):

    permission_classes=[IsAdmin]

    def put(self, request, pk):

        doctor = get_object_or_404(Doctor, pk=pk)

        serializer = DoctorSerializer(doctor, data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(
            {
                "success":True,
                "message":"Doctor updated successfully",
                "data":serializer.data

            },
            status=status.HTTP_200_OK
        )
    



    def patch(self, request, pk):

        doctor = get_object_or_404(Doctor, pk=pk)

        serializer = DoctorSerializer(doctor,data=request.data,partial=True)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(
            {
                "success":True,
                "message":"Doctor updated successfully",
                "data": serializer.data
            },
            status = status.HTTP_200_OK
        )





class DoctorDeactivateAPIView(APIView):

    permission_classes=[IsAdmin]

    def delete(self, request, pk):

        doctor = get_object_or_404(Doctor, pk=pk)

        doctor.status = Doctor.INACTIVE

        doctor.save()

        return Response(
            {
                "success":True,
                "message":"Doctor deactivated successfully"
            },
            status=status.HTTP_200_OK
        )




class DoctorDetailAPIView(APIView):

    permission_classes=[IsAdmin]

    def get(self, request, pk):

        doctor = get_object_or_404(Doctor, pk=pk)

        serializer = DoctorSerializer(doctor)

        return Response(
            {
                "success":True,
                "data": serializer.data
            },
            status=status.HTTP_200_OK
        )
    

    