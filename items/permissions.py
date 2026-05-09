from rest_framework.permissions import BasePermission, IsAuthenticated


class IsAdminOrStaff(BasePermission):
    """
    Allows access only to admin or staff users.
    """
    def has_permission(self, request, view):
        return bool(
            request.user and
            request.user.is_authenticated and
            (request.user.is_staff or request.user.is_superuser)
        )


class IsAuthenticatedReadOnly(BasePermission):
    """
    Allows any authenticated user to read (GET).
    Only admin/staff can write (POST, PUT, PATCH, DELETE).
    """
    SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        if request.method in self.SAFE_METHODS:
            return True
        return request.user.is_staff or request.user.is_superuser