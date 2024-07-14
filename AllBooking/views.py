from django.shortcuts import render
from datetime import datetime, timedelta
from .models import Booking, TimeSlot

def booking_calendar(request, base_date=None):
    if base_date is None:
        base_date = datetime.today()
    else:
        base_date = datetime.strptime(base_date, '%Y-%m-%d')

    start_week = base_date - timedelta(days=base_date.weekday())
    end_week = start_week + timedelta(days=6)
    week_dates = [start_week + timedelta(days=i) for i in range(7)]

    bookings = Booking.objects.all()
    slots = TimeSlot.objects.all()
    slot_ids = [slot.slot_id for slot in slots]

    context = {
        'bookings': bookings,
        'week_dates': week_dates,
        'previous_week': (week_dates[0] - timedelta(days=7)).strftime('%Y-%m-%d'),
        'next_week': (week_dates[-1] + timedelta(days=1)).strftime('%Y-%m-%d'),
        'range': range(1, 5),
        'slot_ID': slot_ids,
    }

    return render(request, 'BookingHome.html', context)
