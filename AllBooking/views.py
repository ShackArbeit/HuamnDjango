from django.shortcuts import render
from datetime import datetime, timedelta
from .models import Booking

def get_week_dates(start_date):
    return [start_date + timedelta(days=i) for i in range(7)]

def booking_calendar(request, year=None, month=None, day=None):
    if year is None or month is None or day is None:
        today = datetime.today()
        start_date = datetime(today.year, today.month, today.day)
    else:
        start_date = datetime(year, month, day)

    week_dates = get_week_dates(start_date)

    bookings = Booking.objects.filter(date__range=[week_dates[0], week_dates[-1]])

    context = {
        'week_dates': week_dates,
        'bookings': bookings,
        'previous_week': start_date - timedelta(days=7),
        'next_week': start_date + timedelta(days=7),
    }

    return render(request, 'BookingHome.html', context)
