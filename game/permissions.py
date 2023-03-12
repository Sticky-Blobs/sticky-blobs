from rest_framework import permissions


class IsAdminOrRetrieveOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if request.user.is_authenticated:
            if request.user.is_staff != True:
                return False

            return True

        return False