from django.contrib import admin
from .models import FreeVideos


class VideoAdmin(admin.ModelAdmin):
      list_display=('video_title','video_description','video_link','pub_date')

admin.site.register(FreeVideos,VideoAdmin)

