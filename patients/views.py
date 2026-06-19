from django.shortcuts import get_object_or_404
from django.db.models import Q

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from accounts.permissions import  IsAdminOrReceptionist

from .serializers import PatientSerializer
from .models import Patient
from doctors.utils.pagination import BasePagination

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
    


class PatientDeleteAPIView(APIView):

    permission_classes=[IsAdminOrReceptionist]

    def delete(self, request, pk):

        patient = get_object_or_404(Patient,pk=pk)

        patient.status = Patient.INACTIVE

        patient.save()

        return Response(
            {
                "success": True,
                "message": "Patient deleted successfully"
            },
            status=status.HTTP_200_OK
        )
    

class PatientActivateAPIView(APIView):

    permission_classes=[IsAdminOrReceptionist]

    def patch(self, request, pk):

        patient = get_object_or_404(Patient, pk=pk)

        patient.status = Patient.ACTIVE

        patient.save()

        return Response(
            {
                "success":True,
                "message":"Patient activated successfully."
            },
            status=status.HTTP_200_OK
        )



class PatientListAPIView(APIView):

    permission_classes=[IsAdminOrReceptionist]

    def get(self, request):

        queryset = Patient.objects.all()

        search = request.query_params.get("search")

        if search:

            queryset = queryset.filter(
                Q(name__icontains=search),
                Q(patient_id__icontains=search),
                Q(email__icontains=search)
            )

        paginator = BasePagination()

        paginated_queryset = paginator.paginate_queryset(queryset, request)

        serializer = PatientSerializer(paginated_queryset, many=True)

        return paginator.get_paginated_response(serializer.data)



class PatientDetailsAPIView(APIView):

    permission_classes=[IsAdminOrReceptionist]

    def get(self, request, pk):

        patient = get_object_or_404(Patient,pk=pk)

        serializer = PatientSerializer(patient)

        return Response(
            {
                "success":True,
                "data":serializer.data
            },
            status=status.HTTP_200_OK
        )


