from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Bucketlist(models.Model):
    """This class represents the bucketlist model."""
    name = models.CharField(max_length=255, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    date_modified = models.DateTimeField(auto_now=True, editable=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,
                                   related_name='bucketlists', editable=False)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)


class Item(models.Model):
    """This class represents the bucketlist item model."""
    name = models.CharField(max_length=255, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    date_modified = models.DateTimeField(auto_now=True, editable=False)
    is_completed = models.BooleanField(default=False)
    bucket = models.ForeignKey(Bucketlist, on_delete=models.CASCADE,
                               related_name='items', editable=False)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
