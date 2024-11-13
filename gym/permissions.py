# permissions.py
from rest_framework.permissions import BasePermission

class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'ADMIN' or request.method in ['GET', 'HEAD', 'OPTIONS']
