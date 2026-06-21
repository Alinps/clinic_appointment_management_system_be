from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError




class ClinicSettings(models.Model):

    clinic_name = models.CharField(
        max_length=200
    )

    address = models.TextField()

    phone = models.CharField(
        max_length=15
    )

    slot_duration = models.PositiveIntegerField(
        validators=[MinValueValidator(5)],
        help_text="Appointment slot duration in minutes"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        db_table = "clinic_settings"

        verbose_name = "Clinic Settings"

        verbose_name_plural = "Clinic Settings"


    def save(self, *args, **kwargs):

        if not self.pk and ClinicSettings.objects.exists():
            
            raise ValidationError(
                "Only one ClinicSettings instance is allowed."
            )

        return super().save(*args, **kwargs)

    def __str__(self):

        return self.clinic_name