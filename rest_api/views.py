from rest_framework import generics
from .serializers import BucketlistSerializer, ItemSerializer, UserSerializer
from rest_framework import permissions
from .permissions import IsOwner, IsOwnerOrReadOnly
from django.shortcuts import get_object_or_404
from .models import Bucketlist, Item
from django.contrib.auth.models import User
from rest_framework.filters import SearchFilter


class UserView(generics.CreateAPIView):
    """Defines the user view"""
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BucketlistView(generics.ListCreateAPIView):
    """This class creates and retrieves all bucketlists."""
    serializer_class = BucketlistSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)
    filter_backends = [SearchFilter]
    search_fields = ('id', 'name')

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
    filter_backends = [SearchFilter]
    search_fields = ('id', 'name')

    def perform_create(self, serializer):
        """Saves the item details when creating a new bucketlist item."""
        bucketlist_id = self.kwargs.get('bucketlist_id')
        bucketlist = get_object_or_404(Bucketlist, created_by=self.request.user,
                                       id=bucketlist_id)
        serializer.save(bucket=bucketlist)


class ItemlistDetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class retrieves, updates and deletes specific bucketlist items."""

    serializer_class = ItemSerializer

    def get_queryset(self):
        """Returns the item created by current user in specific bucket."""
        bucket = self.kwargs.get('bucketlist_id')
        item = self.kwargs.get('pk')
        bucketlist = get_object_or_404(Bucketlist, created_by=self.request.user,
                                       id=bucket)
        queryset = Item.objects.filter(id=item, bucket=bucketlist)
        return queryset
