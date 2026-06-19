from django.shortcuts import get_object_or_404
from django.db.models import Q

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.permissions import IsAdmin,IsAdminOrReceptionist

from .models import Doctor
from .serializers import DoctorSerializer
from .utils.pagination import BasePagination


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
    

class DoctorActivateAPIView(APIView):

    permission_classes=[IsAdmin]

    def patch(self, request, pk):

        doctor = get_object_or_404(Doctor, pk=pk)

        doctor.status = Doctor.ACTIVE

        doctor.save()

        return Response(
            {
                "success":True,
                "message":"Doctor activated successfully"
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
    



class DoctorListAPIVIew(APIView):

    permission_classes=[IsAdminOrReceptionist]

    def get(self, request):

        queryset = Doctor.objects.all() # fetching all doctors from the db

        search = request.query_params.get("search") # fetching the seach params from the request

        if search:

            queryset = queryset.filter(     # searching the params from the recieved objects
                Q(name__icontains=search) |
                Q(doctor_id__icontains=search) |
                Q(specialization__icontains=search)
            ) 

        paginator = BasePagination()  # creating a paginatior object for implementing pagination

        paginated_queryset = paginator.paginate_queryset(queryset, request) # paginating the searched queryset to divide it upon page numbers

        serializer = DoctorSerializer(paginated_queryset, many=True) # serializing the paginated data

        return paginator.get_paginated_response(serializer.data) 
    

    