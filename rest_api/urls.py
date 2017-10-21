from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import BucketlistView, BucketlistDetailsView, ItemlistView, ItemlistDetailsView
# from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_jwt import views as jwt_views

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
    url(r'^account/', include('djoser.urls')),
    url(r'^auth/login/', jwt_views.obtain_jwt_token, name='auth'),
    }

urlpatterns = format_suffix_patterns(urlpatterns)
