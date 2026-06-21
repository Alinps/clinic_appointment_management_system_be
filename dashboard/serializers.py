from .models import ClinicSettings

from rest_framework import serializers


class ClinicSettingSerializer(serializers.ModelSerializer):

    class Meta:

        model=ClinicSettings
        fields=[
            "id",
            "clinic_name",
            "address",
            "phone",
            "slot_duration",
            "created_at",
            "updated_at"
        ]

        read_only_fields=[
            "id",
            "created_at",
            "updated_at"
        ]