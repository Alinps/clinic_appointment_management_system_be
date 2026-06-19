from django.db import models

# Dctor details
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
    





# Doctor working day marking table
class DoctorAvailability(models.Model):

    MONDAY = "MONDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"
    THURSDAY = "THURSDAY"
    FRIDAY = "FRIDAY"
    SATURDAY = "SATURDAY"
    SUNDAY = "SUNDAY"

    WORKING_DAY_CHOICES = [
        (MONDAY, "Monday"),
        (TUESDAY, "Tuesday"),
        (WEDNESDAY, "Wednesday"),
        (THURSDAY, "Thursday"),
        (FRIDAY, "Friday"),
        (SATURDAY, "Saturday"),
        (SUNDAY, "Sunday"),
    ]

    doctor = models.ForeignKey(
        "Doctor",
        on_delete=models.CASCADE,
        related_name="availabilities"
        )

    working_day = models.CharField(
        max_length=20,
        choices=WORKING_DAY_CHOICES
        )

    start_time = models.TimeField()

    end_time = models.TimeField()

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:

        db_table = "doctor_availabilities"

        ordering = [
            "working_day",
            "start_time"
        ]

    def __str__(self):

        return (
            f"{self.doctor.name} - "
            f"{self.working_day} "
            f"({self.start_time} - {self.end_time})"
        )
    







# Doctor leave marking table
class DoctorLeave(models.Model):

    doctor = models.ForeignKey(
        "Doctor",
        on_delete=models.CASCADE,
        related_name="leaves"
    )

    leave_date = models.DateField()

    reason = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        db_table = "doctor_leaves"

        ordering = ["-leave_date"]

        constraints = [
            models.UniqueConstraint(
                fields=["doctor", "leave_date"],
                name="unique_doctor_leave_date"
            )
        ]

    def __str__(self):

        return (
            f"{self.doctor.name} - "
            f"{self.leave_date}"
        )