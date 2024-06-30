from django.shortcuts import render
from datetime import datetime, timedelta
from .models import Booking, TimeSlot

def get_week_dates(base_date=None):
    if base_date is None:
        base_date = datetime.today()
    start_week = base_date - timedelta(days=base_date.weekday())
    return [start_week + timedelta(days=i) for i in range(7)]

def booking_list(request, week_offset=0):
    base_date = datetime.today() + timedelta(weeks=week_offset)
    week_dates = get_week_dates(base_date)
    bookings = Booking.objects.filter(Date__in=week_dates).order_by('Date', 'booking_slot__start_slot')
    timeslots = TimeSlot.objects.all().order_by('start_slot')

    context = {
        'week_dates': week_dates,
        'bookings': bookings,
        'timeslots': timeslots,
        'week_offset': week_offset,
    }
    return render(request, 'BookingHome.html', context)
