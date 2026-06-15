from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from .serializers import LoginSerializer
from .serializers import ReceptionistCreateSerializer

from .utls.custom_payload import get_tokens_for_user

from .permissions import IsAdmin




    


class LoginAPIView(APIView):

    authentication_classes = []
    permission_classes = []

    def post(self, request):

        serializer = LoginSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"] # type: ignore

        tokens = get_tokens_for_user(user)

        return Response({
            "success": True,
            "access": tokens["access"],
            "refresh": tokens["refresh"],
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "role": user.role,
            }
        }, status=status.HTTP_200_OK)
    






class ReceptionistCreateAPIView(APIView):

    permission_classes = [IsAdmin]

    def post(self, request):

        serializer = ReceptionistCreateSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        receptionist = serializer.save()

        return Response(
            {
                "success": True,
                "message": "Receptionist created successfully",
                "data": {
                    "id": receptionist.id, # type: ignore
                    "username": receptionist.username, # type: ignore
                    "email": receptionist.email,# type: ignore
                    "role": receptionist.role,# type: ignore
                }
            },
            status=status.HTTP_201_CREATED
        )