from django.contrib.auth import authenticate,get_user_model
from rest_framework import serializers




User = get_user_model()

class LoginSerializer(serializers.Serializer):

    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):

        user = authenticate(
            email=attrs["email"],
            password=attrs["password"]
        )

        if not user:
            raise serializers.ValidationError(
                "Invalid email or password"
            )

        attrs["user"] = user

        return attrs
    



class ReceptionistCreateSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True,
        min_length=6
    )

    class Meta:

        model = User

        fields = [
            "username",
            "email",
            "password"
        ]

    def create(self, validated_data):

        password = validated_data.pop("password")

        receptionist = User.objects.create(
            role=User.RECEPTIONIST, # type: ignore
            **validated_data
        )

        receptionist.set_password(password)
        receptionist.save()

        return receptionist
    


