from django.shortcuts import render
from datetime import datetime, timedelta
from .models import Booking, TimeSlot

def get_week_dates(base_date=None):
    if base_date is None:
        base_date = datetime.today()
    start_week = base_date - timedelta(days=base_date.weekday())
    return [start_week + timedelta(days=i) for i in range(7)]

def booking_calendar(request, base_date=None):
    if base_date is None:
        base_date = datetime.today()
    else:
        base_date = datetime.strptime(base_date, '%Y-%m-%d')

    start_week = base_date - timedelta(days=base_date.weekday())
    end_week = start_week + timedelta(days=6)
    week_dates = [start_week + timedelta(days=i) for i in range(7)]
  
    bookings = Booking.objects.filter(date__range=[start_week, end_week])

    calendar = []

    for booking in bookings:
        day = booking.date
        day_id = booking.day_id
        slot_id = booking.booking_slot.slot_id
        booking_description = booking.booking_description
        is_booking = booking.is_booking

        for date in week_dates:
            if date.weekday()==0:
                day_id=0
            elif date.weekday()==1:
                day_id=1
            elif date.weekday()==2:
                day_id=2
            elif date.weekday()==3:
                day_id=3
            elif date.weekday()==4:
                day_id=4
            elif date.weekday()==5:
                day_id=5
            else:
                day_id=6

            calendar.append({
                'day': day,
                'day_id': day_id,
                'slot_id': slot_id,
                'booking_description': booking_description,
                'is_booking': is_booking
            })

    context = {
        'calendar':calendar,
        'week_dates': week_dates,
        'previous_week': (week_dates[0] - timedelta(days=7)).strftime('%Y-%m-%d'),
        'next_week': (week_dates[-1] + timedelta(days=1)).strftime('%Y-%m-%d'),
        'range': range(1, 5 + 1)
    }

    return render(request, 'BookingHome.html', context)