from django.contrib import admin
from .models import aboutJeorme

class aboutAdmin(admin.ModelAdmin):
      list_display=('id','about_title','about_year','about_content')

admin.site.register(aboutJeorme,aboutAdmin)
