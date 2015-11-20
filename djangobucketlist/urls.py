"""djangobucketlist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from bucketlistapi import views
from bucketlistapp import views as app_view
from rest_framework.authtoken import views as rest_views
from django.contrib.auth.views import logout

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', app_view.IndexView.as_view(), name='index'),
    url(r'^register$', app_view.RegisterView.as_view(), name='register'),
    url(r'^login$', app_view.LoginView.as_view(), name='login'),
    url(r'^logout$', logout, {'next_page': '/'}),

    url(r'^bucketlists/$', app_view.BucketlistAppView.as_view(), name='bucket_list'),



    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/users/$', views.UserList.as_view()),
    url(r'^api/users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    url(r'^api/bucketlists/$', views.BucketlistView.as_view(), name='bucket_list'),
    url(r'^api/bucketlists/(?P<pk>[0-9]+)/$', views.BucketListDetailView.as_view(), name='bucket_list_detail'),
    url(r'^api/bucketlists/(?P<pk>[0-9]+)/items/$', views.BucketListDetailView.as_view(), name='bucket_list_detail'),
    url(r'^api/bucketlists/(?P<pk>[0-9]+)/items/(?P<id>[0-9]+)$', views.BucketListDetailView.as_view(), name='bucket_list_detail'),
    url(r'^api_token/$', rest_views.obtain_auth_token),

]
