from django.conf.urls import include, url
from django.contrib import admin
from bucketlistapi import views
from bucketlistapp import views as app_view
from rest_framework.authtoken import views as rest_views
from django.contrib.auth.views import logout
import bucketlistapp.urls
import bucketlistapi.urls

urlpatterns = [
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^users/$', views.UserList.as_view(), name='all_users'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^bucketlists/$', views.BucketlistView.as_view(), name='bucket_list'),
    url(r'^bucketlists/(?P<pk>[0-9]+)/$', views.BucketListDetailView.as_view(), name='bucketlist_detail'),
    url(r'^bucketlists/(?P<bucket_id>[0-9]+)/items/$', views.BucketlistItemView.as_view(), name='bucketlist_item'),
    url(r'^bucketlists/(?P<bucket_id>[0-9]+)/items/(?P<item_id>[0-9]+)$', views.BucketlistItemDetailView.as_view(), name='item_detail'),
    url(r'^api_token/$', rest_views.obtain_auth_token),
    url(r'^docs/', include('rest_framework_swagger.urls')),
]