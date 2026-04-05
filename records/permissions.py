from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    """Allows only admin users."""

    def has_permission(self, request, view):
        return request.user.role == "ADMIN"


class IsTeacherOrAdmin(BasePermission):
    """Allows teacher or admin."""

    def has_permission(self, request, view):
        return request.user.role in ["TEACHER", "ADMIN"]