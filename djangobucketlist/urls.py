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

urlpatterns = [
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^bucketlists/$', views.BucketlistView.as_view(), name='bucket_list'),
    url(r'^bucketlists/(?P<pk>[0-9]+)/$', views.BucketListDetailView.as_view(), name='bucket_list_detail'),
    url(r'^bucketlists/(?P<pk>[0-9]+)/items/$', views.BucketListDetailView.as_view(), name='bucket_list_detail'),
    # url(r'^bucketlists/(?P<pk>[0-9]+)/items/(?P<pk>[0-9]+)/$', views.BucketListDetailView.as_view(), name='bucket_list_detail'),
    url(r'^api_token/$', rest_views.obtain_auth_token),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),

    url(r'^buckettemp/$', app_view.BucketlistAppView.as_view(), name='bucket_list'),
]
