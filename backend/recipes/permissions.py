from rest_framework import permissions


class ReadOnly(permissions.BasePermission):
    """
    Разрешение только на чтение для всех пользователей.
    """
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Разрешение либо авторам, либо только на чтение.
    """
    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user or request.user.is_superuser
        )
