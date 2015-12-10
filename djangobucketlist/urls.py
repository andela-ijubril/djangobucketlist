from django.conf.urls import include, url
from django.contrib import admin
import bucketlistapp.urls
import bucketlistapi.urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(bucketlistapp.urls)),
    url(r'^api/', include(bucketlistapi.urls)),
]
