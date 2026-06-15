from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.permissions import IsAdmin

from .serializers import DoctoreCreateSerializer


class DoctorCreateAPIView(APIView):

    permission_classes = [IsAdmin]

    def post(self, request):

        serializer = DoctoreCreateSerializer(data = request.data)
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