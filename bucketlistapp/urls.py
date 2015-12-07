from django.conf.urls import include, url
from django.contrib import admin
from bucketlistapi import views
from bucketlistapp import views
from rest_framework.authtoken import views as rest_views
from django.contrib.auth.views import logout

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^register$', views.RegisterView.as_view(), name='register'),
    url(r'^login$', views.LoginView.as_view(), name='login'),
    url(r'^logout$', logout, {'next_page': '/'}),

    url(r'^bucketlists/$', views.BucketlistAppView.as_view(), name='bucket_list'),
    url(r'^bucketlists/(?P<bucket_id>[0-9]+)/$', views.UpdateBucketlistView.as_view(), name='update_bucket_list'),
    url(r'^bucketlists/items/$', views.BucketlistItemAppView.as_view(), name='bucket_list'),
    url(r'^bucketlists/(?P<bucketlist>[0-9]+)/items/$', views.BucketlistItemAppView.as_view(), name='bucket_list_item'),
    url(r'^bucketlists/(?P<bucketlist>[0-9]+)/items/(?P<item>[0-9]+)/$', views.UpdateBucketlistItemView.as_view(), name='update_bucketlist_item'),
    url(r'^bucketlists/(?P<bucketlist>[0-9]+)/items/(?P<item>[0-9]+)/status/$', views.ItemStatusView.as_view(), name='bucket_list_item'),
]
