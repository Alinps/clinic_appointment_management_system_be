from django.db import models


class Doctor(models.Model):

    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"

    STATUS_CHOICES = [
        (ACTIVE, "Active"),
        (INACTIVE, "Inactive"),
    ]

    doctor_id = models.CharField(
        max_length=20,
        unique=True
    )

    name = models.CharField(
        max_length=100
    )

    specialization = models.CharField(
        max_length=100
    )

    phone = models.CharField(
        max_length=15
    )

    email = models.EmailField(
        unique=True
    )

    qualification = models.CharField(
        max_length=255
    )

    consultation_fee = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    joining_date = models.DateField()



    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=ACTIVE
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        db_table = "doctors"

        ordering = ["name"]

        indexes = [
            models.Index(fields=["doctor_id"]),
            models.Index(fields=["name"]),
            models.Index(fields=["specialization"]),
        ]

    def __str__(self):
        return f"{self.doctor_id} - {self.name}"