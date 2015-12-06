from django.contrib import admin
from .models import Bucketlist, BucketlistItem


class Items(admin.TabularInline):
    model = BucketlistItem


class BucketListAdmin(admin.ModelAdmin):
    inlines = [Items]
    list_display = ('name', 'created_date', 'modified_date')

admin.site.register(Bucketlist, BucketListAdmin)
