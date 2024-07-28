from django.shortcuts import render, redirect
from django.utils.timezone import localdate, timedelta
import datetime
from .models import Booking

def booking_calendar(request):
    today = localdate()
    return redirect('booking_calendar_with_date', year=today.year, month=today.month, day=today.day)

def booking_calendar_with_date(request, year, month, day):
    selected_date = datetime.date(year, month, day)
    start_date = selected_date - timedelta(days=selected_date.weekday())
    end_date = start_date + timedelta(days=6)
    week_dates = [start_date + timedelta(days=i) for i in range(7)]

    bookings = Booking.objects.filter(date__range=(start_date, end_date))

    previous_week = selected_date - timedelta(days=7)
    next_week = selected_date + timedelta(days=7)

    slot_choices = [
        (1, "AM09:30 | PM12:00"),
        (2, "PM12:30 | PM14:00"),
        (3, "PM14:30 | PM17:00"),
        (4, "PM17:30 | PM20:30")
    ]

    context = {
        'week_dates': week_dates,
        'bookings': bookings,
        'previous_week': previous_week,
        'next_week': next_week,
        'slot_choices': slot_choices,
    }
    return render(request, 'BookingHome.html', context)
