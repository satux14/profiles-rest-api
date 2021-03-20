from django.contrib import admin
from profiles_api import models

admin.site.register(models.UserProfile) # Register model with Django Admin
admin.site.register(models.ProfileFeedItem)
