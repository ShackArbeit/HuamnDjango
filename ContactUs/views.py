from django.shortcuts import render
from . import forms
from django.core.mail import EmailMessage





def Contact(request):
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            message = "感謝您的來信，我們會儘速處理您的寶貴意見。"
            user_name = form.cleaned_data['user_name']
            user_book = form.cleaned_data['user_school']
            user_email  = form.cleaned_data['user_email']
            user_message = form.cleaned_data['user_message']
            mail_body = u'''
回饋者姓名：{}
是否第一次預約：{}
電子郵件：{}
反應意見：如下
{}'''.format(user_name, user_book, user_email, user_message)

            email = EmailMessage(   '來自【人類圖遇見八字】的回饋意見', 
                                    mail_body, 
                                    user_email,
                                    ['g0972222165@gmail.com']
                                    )
            email.send()
        else:
            message = "請檢查您輸入的資訊是否正確！"
    else:
        form = forms.ContactForm()
    return render(request, 'ContactForm.html', locals())


