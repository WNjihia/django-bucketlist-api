from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import BucketlistView

urlpatterns = {
    url(r'^auth/', include('rest_framework.urls',
                           namespace='rest_framework')),
    url(r'^bucketlists/$', BucketlistView.as_view(), name="create"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
