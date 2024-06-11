from django.contrib import admin
from .models import Value,Post

class PostAdmin(admin.ModelAdmin):
      list_display=('user_name','message','enabled','pub_time')
      ordering=('-pub_time',)

admin.site.register(Value)
admin.site.register(Post,PostAdmin)