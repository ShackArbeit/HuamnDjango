from django.contrib import admin
from .models import LayoutWhat,YourBooks,YourType,YourRole,YourRoad,YourAuth,YourEnergy


class WhatAdmin(admin.ModelAdmin):
      list_display=('id','title','content')

# 人類圖是你的使用說明部分
class Your_Books(admin.ModelAdmin):
      list_display=('id','layout_key','title','content','imgs_url')
      
# 類型 = 你的天職部分
class Your_Type(admin.ModelAdmin):
      list_display=('id','layout_key','title','content','imgs_url')

# 人生角色 的部分
class Your_Role(admin.ModelAdmin):
      list_display=('id','layout_key','title','content','imgs_url')

# 內在權威 = 做決定的方法 的部分
class Your_Auth(admin.ModelAdmin):
      list_display=('id','layout_key','title','content','imgs_url')

# 能量中心 = 你的強弱 的部分
class Your_Energy(admin.ModelAdmin):
       list_display=('id','layout_key','title','content','imgs_url')

# 通道 = 你的天賦 的部分
class Your_Road(admin.ModelAdmin):
      list_display=('id','layout_key','title','content','imgs_url')


admin.site.register(LayoutWhat,WhatAdmin)
admin.site.register(YourBooks,Your_Books)
admin.site.register(YourType,Your_Type)
admin.site.register(YourRole,Your_Role)
admin.site.register(YourAuth,Your_Auth)
admin.site.register(YourEnergy,Your_Energy)
admin.site.register(YourRoad,Your_Road)