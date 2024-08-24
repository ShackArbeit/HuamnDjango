from django.shortcuts import render, redirect
from django.utils.timezone import localdate, timedelta
import datetime
from django.views.decorators.csrf import csrf_exempt
from .models import Booking,File,TimeSlot
from django.core.mail import EmailMessage
from .forms import ContactForm
from django.http import JsonResponse
import time
import requests
import pandas as pd
import os
from django.conf import settings
from django.db import transaction



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

# 點擊預約按鈕後送至填寫表單的部分
def contact(request):
    message = ''
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            message = "感謝您的預約諮詢，我們會儘速處理您。"
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

# 串接 Line Api 的部分
@csrf_exempt
def send_line_notification(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        user_check = request.POST.get('user_check')
        user_email = request.POST.get('user_email')
        user_line_id = request.POST.get('user_line_id')
        description = request.POST.get('description')
        date = request.POST.get('date')
        access_token = 'PiMeWf841CpGqpXJEvk9VEbL7YTmJyh9tBHgVdTvh1h'  

        # 發送 LINE 通知
        message = f'''
        預約描述: {description}
        預約日期: {date}
        預約者姓名: {user_name}
        電子郵件: {user_email}
        Line ID: {user_line_id} 
        是否第一次預約: {user_check}'''

        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        data = {
            'message': message
        }
        response = requests.post('https://notify-api.line.me/api/notify', headers=headers, data=data)
        
        # 發送電子郵件
        mail_body = message
        email = EmailMessage(
            '來自【人類圖遇見八字】的預約詢問',
            mail_body,
            user_email,
            ['g0972222165@gmail.com']
        )
        try:
            email.send()
            email_status = "郵件發送成功"
        except Exception as e:
            email_status = f"郵件發送失敗: {e}"

        return JsonResponse({'status': response.status_code, 'response': response.json(), 'email_status': email_status})

    return JsonResponse({'error': 'Invalid request'}, status=400)


# 上傳 Excel 部分
def uplad_file(request):
    if request.method=='POST':
        uploaded_file=request.FILES['file']
        file_instance=File(file=uploaded_file)
        file_instance.save()

        # 加入短暫延遲
        time.sleep(2)

        file_path = os.path.join(settings.MEDIA_ROOT, file_instance.file.name)

        try:
            df = pd.read_excel(file_path)
            
            for _, row in df.iterrows():
                try:
                    print(f"Processing row: {row}")
                    timeslot = TimeSlot.objects.get(slot_id=row['booking_slot_id'])
                    Booking.objects.create(
                        date=row['date'],
                        booking_slot=timeslot,
                        day_id=row['day_id'],
                        booking_description=row['booking_description'],
                        is_booking=row['is_booking']
                    )
                    time.sleep(1)  # 每次操作後加入延遲，減少資料庫壓力
                except TimeSlot.DoesNotExist:
                    print(f"TimeSlot with slot_id {row['booking_slot_id']} does not exist.")
                except Exception as e:
                    print(f"Error processing row {row}: {e}")

        except Exception as e:
            print(f"Error reading Excel file: {e}")
        
        print('已經上傳成功了 !')
        return redirect('contact')
    return render(request, 'excel_upload.html')