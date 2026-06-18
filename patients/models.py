from django.db import models


class Patient(models.Model):

    MALE = "MALE"
    FEMALE = "FEMALE"
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"

    STATUS_CHOISES = [
        (ACTIVE, "Active"),
        (INACTIVE, "Inactive")
    ]

    GENDER_CHOICES= [
        (MALE, "Male"),
        (FEMALE,"Female"),
    ]

    patient_id = models.CharField(
        max_length=20,
        unique=True
    )

    name = models.CharField(
        max_length=100
    )   

    date_of_birth = models.DateField()


    gender = models.CharField(
        max_length=20,
        choices=GENDER_CHOICES
    )

    phone = models.CharField(
        max_length=15
    )

    email = models.EmailField(
        unique=True
    )

    address = models.TextField()

    emergency_contact = models.CharField(
        max_length=15
    )

    registration_date = models.DateField()


    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOISES,
        default=ACTIVE
    )

    class Meta:

        db_table = "patients"

        ordering = ["name"]

        indexes = [
            models.Index(fields=["name"]),
        ]

    def __str__(self):
        return f"T{self.patient_id} - {self.name}"