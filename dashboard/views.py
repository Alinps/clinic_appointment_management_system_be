from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from accounts.permissions import IsAdmin

from .models import ClinicSettings

from .serializers import ClinicSettingSerializer



class ClinicSettingsAPIView(APIView):

    permission_classes=[IsAdmin]

    def post(self, request):
        
        settings = ClinicSettings.objects.first()

        if settings:

            serializer = ClinicSettingSerializer(settings, data=request.data)

            serializer.is_valid(raise_exception=True)

            serializer.save()

            return Response({

                "success":True,
                "message":"Clinic settings updated successfully.",
                "data":serializer.data

            },
            status=status.HTTP_200_OK
            )
        
        serializer = ClinicSettingSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(
            {
                "success":True,
                "message":"Clinic settings created successfully.",
                "data":serializer.data
            },
            status=status.HTTP_201_CREATED
        )
    

    def get(self, request):

        settings = ClinicSettings.objects.first()

        if not settings:

            return Response(
                {
                    "success":False,
                    "message":"Clinic settings not found."
                },
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = ClinicSettingSerializer(settings)

        return Response(
            {
                "success":True,
                "data":serializer.data
            },
            status=status.HTTP_200_OK
        )
    
    def put(self, request):

        settings = ClinicSettings.objects.first()

        if not settings:

            return Response(
                {
                    "success":False,
                    "message":"Clinic settings not found."
                },
                status=status.HTTP_404_NOT_FOUND
            )
        
        serializer = ClinicSettingSerializer(settings, data=request.data)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(
            {
                "success":True,
                "message":"Clinic settings updated successfully.",
                "data":serializer.data
            }
        )