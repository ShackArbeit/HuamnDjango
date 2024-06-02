from django.contrib import admin
from .models import BookingProcess,ServiceItems



class Process_Admin(admin.ModelAdmin):
      list_display=('id','porcess_title','process_content','process_icon')


class Service_Admin(admin.ModelAdmin):
      list_display=('id','service_title','service_content')

admin.site.register(BookingProcess,Process_Admin)
admin.site.register(ServiceItems,Service_Admin)
