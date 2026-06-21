from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError

from accounts.managers import UserManager


class User(AbstractUser):

    ADMIN = "ADMIN"
    RECEPTIONIST = "RECEPTIONIST"

    ROLE_CHOICES = [
        (ADMIN, "Admin"),
        (RECEPTIONIST, "Receptionist"),
    ]

    username = models.CharField(
        max_length=100,
        help_text="User full name"
    )

    email = models.EmailField(
        unique=True
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default=RECEPTIONIST
    )

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = ["username"]

    objects = UserManager() # type: ignore

    def save(self, *args, **kwargs):

        if self.is_superuser:
            self.role = self.ADMIN

        super().save(*args, **kwargs)

    def __str__(self):
        return self.email
    





