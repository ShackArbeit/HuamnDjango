from django.contrib import admin
from .models import LayoutWhat,YourBooks


class WhatAdmin(admin.ModelAdmin):
      list_display=('title','content')

# 人類圖是你的使用說明部分
class Your_Books(admin.ModelAdmin):
      list_display=('layout_key','title','content','imgs_url')


admin.site.register(LayoutWhat,WhatAdmin)
admin.site.register(YourBooks,Your_Books)