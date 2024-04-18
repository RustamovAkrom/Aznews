from django.contrib import admin
from .models import Pictures, YouTubeVideoUrl, AnonimusUserEmails


admin.site.register(Pictures)
admin.site.register(YouTubeVideoUrl)
admin.site.register(AnonimusUserEmails)