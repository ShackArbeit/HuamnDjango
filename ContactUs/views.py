from django.shortcuts import render
from django.core.mail import EmailMessage
from .forms import ContactForm


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
                回饋者姓名：{user_name}
                是否第一次預約：{user_book}
                電子郵件：{user_email}
                Line ID：{user_line_id}
                預約描述：{booking_description}
                預約日期：{booking_date}
            '''
            
            email = EmailMessage(
                '來自【人類圖遇見八字】的回饋意見',
                mail_body,
                user_email,
                ['g0972222165@gmail.com']
            )
            try:
                email.send()
                message = "感謝您的來信，我們會儘速處理您的寶貴意見。"
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
