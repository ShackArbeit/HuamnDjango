from django.contrib import admin
from .models import LayoutWhat,YourBooks,YourType


class WhatAdmin(admin.ModelAdmin):
      list_display=('id','title','content')

# 人類圖是你的使用說明部分
class Your_Books(admin.ModelAdmin):
      list_display=('id','layout_key','title','content','imgs_url')
      
# 類型 = 你的天職部分
class Your_Type(admin.ModelAdmin):
      list_display=('id','layout_key','title','content','imgs_url')


admin.site.register(LayoutWhat,WhatAdmin)
admin.site.register(YourBooks,Your_Books)
admin.site.register(YourType,Your_Type)