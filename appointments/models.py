from django.db import models


class Appointment(models.Model):

    PENDING = "PENDING"
    CONFIRMED = "CONFIRMED"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"

    STATUS_CHOICES = [
        (PENDING,"Pending"),
        (CONFIRMED,"Confirmed"),
        (COMPLETED, "Completed"),
        (CANCELLED, "Cancelled")
    ]

    appointment_id = models.CharField(max_length=20,unique=True)
    patient = models.ForeignKey("patients.Patient",on_delete=models.CASCADE,related_name="appointments")
    doctor = models.ForeignKey("doctors.Doctor",on_delete=models.CASCADE,related_name="appointments")
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    reason = models.TextField()
    status = models.CharField(max_length=20,choices = STATUS_CHOICES,default=PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:

        db_table = "appointments"

        ordering = [
            "-appointment_date",
            "-appointment_time"
        ]