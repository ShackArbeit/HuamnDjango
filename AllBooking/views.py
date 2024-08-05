from django.shortcuts import render, redirect
from django.utils.timezone import localdate, timedelta
import datetime
from .models import Booking
from django.core.mail import EmailMessage
from .forms import ContactForm


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

def contact(request):
    message = ''
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['user_name']
            user_book = '是' if form.cleaned_data['user_book'] else '否'
            user_email = form.cleaned_data['user_email']
            user_line_id = form.cleaned_data['user_line_id']
            booking_description = form.cleaned_data['booking_description']
            booking_date = form.cleaned_data['booking_date']

            mail_body = f'''
                預約描述：{booking_description}
                預約日期：{booking_date}
                預約者者姓名：{user_name}
                是否第一次預約：{user_book}
                電子郵件：{user_email}
                Line ID：{user_line_id}     
            '''
            
            email = EmailMessage(
                '來自【人類圖遇見八字】的回饋意見',
                mail_body,
                user_email,
                ['g0972222165@gmail.com']
            )
            try:
                email.send()
                message = "感謝您的預約諮詢，我們會儘速處理您。"
            except Exception as e:
                message = f"郵件發送失敗: {e}"
        else:
            message = "請檢查您輸入的資訊是否正確！"
    else:
        booking_description = request.GET.get('booking_description', '')
        booking_date = request.GET.get('booking_date', '')
        form = ContactForm(initial={
            'booking_description': booking_description,
            'booking_date': booking_date,
        })

    return render(request, 'ContactForm.html', {
        'form': form,
        'message': message,
        'booking_description': booking_description,
        'booking_date': booking_date,
    })
