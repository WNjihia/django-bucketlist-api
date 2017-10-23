from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import BucketlistView, BucketlistDetailsView, ItemlistView, ItemlistDetailsView, UserView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = {
    url(r'^auth/', include('rest_framework.urls',
                           namespace='rest_framework')),
    url(r'^bucketlists/$', BucketlistView.as_view(), name="create"),
    url(r'^bucketlists/(?P<pk>[0-9]+)/$', BucketlistDetailsView.as_view(),
        name="bucketlist_details"),

    url(r'^bucketlists/(?P<bucketlist_id>[0-9]+)/items/$',
        ItemlistView.as_view(), name="create"),
    url(r'^bucketlists/(?P<bucketlist_id>[0-9]+)/items/(?P<pk>[0-9]+)/$',
        ItemlistDetailsView.as_view(), name="bucketlist_items"),
    url(r'^login/', obtain_auth_token, name="get_auth_token"),
    url(r'^register/$', UserView.as_view(), name="register"),
    }

urlpatterns = format_suffix_patterns(urlpatterns)
