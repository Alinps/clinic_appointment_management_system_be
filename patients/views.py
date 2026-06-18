from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from accounts.permissions import  IsAdminOrReceptionist

from .serializers import PatientSerializer


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

