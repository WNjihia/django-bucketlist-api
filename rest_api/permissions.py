from rest_framework.permissions import BasePermission
from .models import Bucketlist, Item


class IsOwner(BasePermission):
    """Custom permission class."""

    def has_object_permission(self, request, view, obj):
        """Return True if the current user is the bucketlist owner."""
        if isinstance(obj, Bucketlist):
            return obj.created_by == request.user
        return obj.created_by == request.user


class IsOwnerOrReadOnly(BasePermission):
    """Setting permission class to isOwner or read only"""
    def has_object_permission(self, request, view, obj):
        if isinstance(obj, Item):
            return obj.bucket.created_by == request.user
        return obj.created_by == request.user
