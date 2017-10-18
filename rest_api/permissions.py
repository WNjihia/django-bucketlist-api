from rest_framework.permissions import BasePermission
from .models import Bucketlist


class IsOwner(BasePermission):
    """Custom permission class."""

    def has_object_permission(self, request, view, obj):
        """Return True if the current user is the bucketlist owner."""
        if isinstance(obj, Bucketlist):
            return obj.created_by == request.user
        return obj.created_by == request.user
