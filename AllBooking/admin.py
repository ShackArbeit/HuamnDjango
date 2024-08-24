from django.contrib import admin


from django.urls import path

from .models import TimeSlot,Booking





class BookingAdmin(admin.ModelAdmin):
    list_display=('booking_slot','date','day_id','booking_description','is_booking')

  
   
class SlotAdmin(admin.ModelAdmin):
    list_display=('slot_id','slot_description',)
    
admin.site.register(TimeSlot,SlotAdmin)
admin.site.register(Booking,BookingAdmin)