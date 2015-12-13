from django.conf.urls import include, url
from bucketlistapi import views
from rest_framework.authtoken import views as rest_views

urlpatterns = [
    url(r'^login/$', views.TokenView.as_view(), name='login_user'),
    url(r'^users/$', views.UserList.as_view(), name='all_users'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^bucketlists/$', views.BucketlistView.as_view(), name='bucket_list'),
    url(r'^bucketlists/(?P<bucket_id>[0-9]+)/$', views.BucketListDetailView.as_view(), name='bucketlist_detail'),
    url(r'^bucketlists/(?P<bucket_id>[0-9]+)/items/$', views.BucketlistItemView.as_view(), name='bucketlist_item'),
    url(r'^bucketlists/(?P<bucket_id>[0-9]+)/items/(?P<item_id>[0-9]+)$', views.BucketlistItemDetailView.as_view(), name='item_detail'),
    url(r'^docs/', include('rest_framework_swagger.urls')),
]