from rest_framework import permissions


class SellerPermission(permissions.BasePermission):
    def has_permission(self, req, view):
        if req.method in permissions.SAFE_METHODS:
            return True

        if req.user.is_seller == True:
            return True

        return req.user.is_authenticated and req.user.is_superuser


class SellerOwerPermission(permissions.BasePermission):
    def has_permission(self, req, view):
        if req.user.is_seller == True:
            return True

        return req.user.is_authenticated and req.user.is_superuser
