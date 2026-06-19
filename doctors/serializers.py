from rest_framework import serializers

from .models import Doctor


class DoctorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = "__all__"
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]

    def validate_phone(self, value):

        if not value.isdigit():
            raise serializers.ValidationError(
                "Phone number must contain only digits."
            )

        return value

    def validate_consultation_fee(self, value):

        if value <= 0:
            raise serializers.ValidationError(
                "Consultation fee must be greater than zero."
            )

        return value
    



