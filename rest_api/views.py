from rest_framework import generics
from .serializers import BucketlistSerializer
from rest_framework import permissions
from .permissions import IsOwner
from .models import Bucketlist


class BucketlistView(generics.ListCreateAPIView):
    """This class creates and retrieves all bucketlists."""
    serializer_class = BucketlistSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def get_queryset(self):
        """Returns all bucketlists created by the current user."""
        queryset = Bucketlist.objects.all()
        return queryset

    def perform_create(self, serializer):
        """Save the bucketlist details when creating a new bucketlist."""
        serializer.save(created_by=self.request.user)
