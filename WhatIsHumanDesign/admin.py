from django.contrib import admin
from .models import LayoutWhat


class WhatAdmin(admin.ModelAdmin):
      list_display=('title','content')
      
admin.site.register(LayoutWhat,WhatAdmin)