from django.utils import timezone

from rest_framework import serializers

from .models import Doctor, DoctorAvailability, DoctorLeave


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
        


class DoctorLeaveSerializer(serializers.ModelSerializer):


    doctor = DoctorSerializer(read_only=True)

    class Meta:
        model = DoctorLeave
        fields = [
            "id",
            "doctor",
            "start_leave_date",
            "end_leave_date",
            "reason",
            "created_at",
            "updated_at"
        ]

        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
            "doctor"
        ]

    def validate_start_leave_date(self, value):

        if value < timezone.now().date():
            raise serializers.ValidationError(
                "Start Leave date cannot be in a past."
            )
        return value
    
    def validate_end_leave_date(self, value):

        if value < timezone.now().date():
            raise serializers.ValidationError(
                "End Leave date cannot be in a past."
            )
        return value
        
    def validate(self, attrs):

        start_leave_date = attrs.get("start_leave_date")
        end_leave_date = attrs.get("end_leave_date")

        if start_leave_date and end_leave_date:

            if end_leave_date < start_leave_date:

                raise serializers.ValidationError(
                    {
                        "end_leave_date":"End leave date must be greater than or equal to start leave date."
                    }
                )
        return attrs






