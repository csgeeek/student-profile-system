from rest_framework.permissions import BasePermission


class CustomPermission(BasePermission):
    def has_permission(self, request, view):
        SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
        if request.method in SAFE_METHODS and request.user.is_authenticated:
            return True
        elif request.user and request.user.is_staff:
            return True
        return False
