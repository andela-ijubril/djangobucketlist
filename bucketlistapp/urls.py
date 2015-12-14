from django.conf.urls import url
from bucketlistapp import views
from django.contrib.auth.views import logout

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^register$', views.RegisterView.as_view(), name='register'),
    url(r'^login$', views.LoginView.as_view(), name='login'),
    url(r'^logout$', logout, {'next_page': '/'}),

    url(r'^bucketlists/$', views.BucketlistAppView.as_view(), name='bucketlists'),
    url(r'^bucketlists/(?P<bucket_id>[0-9]+)/$', views.UpdateBucketlistView.as_view(), name='update_bucket_list'),
    url(r'^bucketlists/(?P<bucketlist>[0-9]+)/items/$', views.BucketlistItemAppView.as_view(), name='bucketlist_item'),
    url(r'^bucketlists/(?P<bucketlist>[0-9]+)/items/(?P<item>[0-9]+)/$', views.UpdateBucketlistItemView.as_view(), name='update_bucketlist_item'),
    url(r'^bucketlists/(?P<bucketlist>[0-9]+)/items/(?P<item>[0-9]+)/status/$', views.ItemStatusView.as_view(), name='bucketlist_item_status'),
]
