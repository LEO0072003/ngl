from rest_framework.permissions import BasePermission
from rest_framework.exceptions import APIException


class AdminUserPermission(BasePermission):
    """
    Permission class for Admin Users.
    """
    def has_permission(self, request, view):
        if request.user and request.user.is_authenticated and request.user.is_staff:
            return True
        else:
            raise APIException("Permission limited to authenticated admin user")
