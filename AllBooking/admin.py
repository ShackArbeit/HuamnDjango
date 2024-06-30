from django.contrib import admin
from .models import TimeSlot,Booking

class BookingAdmin(admin.ModelAdmin):
    list_display=('booking_slot','Date','Day_id','booking_description','is_booking')
    

class SlotAdmin(admin.ModelAdmin):
    list_display=('start_slot','end_slot','slot_difference','slot_description')
    
admin.site.register(TimeSlot,SlotAdmin)
admin.site.register(Booking,BookingAdmin)