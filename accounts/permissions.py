from django.contrib.auth import get_user_model
from rest_framework.permissions import BasePermission

User = get_user_model()


class IsAdmin(BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == User.ADMIN # type: ignore
        )


class IsReceptionist(BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == User.RECEPTIONIST # type: ignore
        )


class IsAdminOrReceptionist(BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role in [
                User.ADMIN, # type: ignore
                User.RECEPTIONIST # type: ignore
            ]
        )