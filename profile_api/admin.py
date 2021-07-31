from django.contrib import admin

from .models import ProfileFeedItem, UserProfile

# Register your models here.


admin.site.register(UserProfile)
admin.site.register(ProfileFeedItem)
