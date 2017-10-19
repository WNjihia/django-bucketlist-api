from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import BucketlistView, BucketlistDetailsView

urlpatterns = {
    url(r'^auth/', include('rest_framework.urls',
                           namespace='rest_framework')),
    url(r'^bucketlists/$', BucketlistView.as_view(), name="create"),
    url(r'^bucketlists/(?P<pk>[0-9]+)/$', BucketlistDetailsView.as_view(),
        name="bucketlist_details"),
    }

urlpatterns = format_suffix_patterns(urlpatterns)
