from rest_framework.permissions import BasePermission


class CustomIsAdminUser(BasePermission):
    # Add cutome isAdmin check method
    def has_permission(self, request, view):
        try:
            return bool(request.user and request.user.admin)
        except:
            return False
