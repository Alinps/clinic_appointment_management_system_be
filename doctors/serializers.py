from rest_framework import serializers

from .models import Doctor, DoctorAvailability


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
    



class DoctorAvailabilitySerializer(serializers.ModelSerializer):

    class Meta:
        
        model=DoctorAvailability
        
        fields=[
            "id",
            "working_day",
            "start_time",
            "end_time"
        ]


        def validate(self, attrs):

            start_time = attrs["start_time"]
            end_time = attrs["end_time"]

            if start_time > end_time:
                raise serializers.ValidationError(
                    "End time must be greater than start time."
                )
            
            return attrs





