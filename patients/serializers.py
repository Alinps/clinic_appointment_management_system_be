from rest_framework import serializers

from .models import Patient

class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model=Patient
        fields = "__all__"
        read_only_field=[
            "id",
            "created_at",
            "updated_at"
        ]

    def validate_phone(self, value):

        if not value.isdigit():
            raise serializers.ValidationError(
                "Phone number must contain only digits."
            )
        return value
    



