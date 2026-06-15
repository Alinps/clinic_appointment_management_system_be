from rest_framework import serializers

from .models import Doctor


class DoctoreCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields  =[
            "doctor_id",
            "name",
            "specialization",
            "phone",
            "email",
            "qualification",
            "consultation_fee",
            "joining_date",
            "status"
        ]