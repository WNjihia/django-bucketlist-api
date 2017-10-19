from rest_framework import generics
from .serializers import BucketlistSerializer, ItemSerializer
from rest_framework import permissions
from .permissions import IsOwner, IsOwnerOrReadOnly
from django.shortcuts import get_object_or_404
from .models import Bucketlist, Item


class BucketlistView(generics.ListCreateAPIView):
    """This class creates and retrieves all bucketlists."""
    serializer_class = BucketlistSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def get_queryset(self):
        """Returns all bucketlists created by the current user."""
        queryset = Bucketlist.objects.filter(created_by=self.request.user)
        return queryset

    def perform_create(self, serializer):
        """Saves the bucketlist details when creating a new bucketlist."""
        serializer.save(created_by=self.request.user)


class BucketlistDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class retrieves, updates and deletes specific bucketlists."""

    serializer_class = BucketlistSerializer

    def get_queryset(self):
        queryset = Bucketlist.objects.filter(created_by=self.request.user)
        return queryset


class ItemlistView(generics.ListCreateAPIView):
    """This class creates and retrieves all bucketlist items."""
    serializer_class = ItemSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)
    queryset = Item.objects.all()

    def perform_create(self, serializer):
        """Saves the item details when creating a new bucketlist item."""
        bucketlist_id = self.kwargs.get('bucketlist_id')
        bucketlist = get_object_or_404(Bucketlist, created_by=self.request.user,
                                       id=bucketlist_id)
        serializer.save(bucket=bucketlist)
