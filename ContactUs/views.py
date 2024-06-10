from django.shortcuts import render

from django.core.mail import EmailMessage


def Contact(request):
    message=''
    if request.method=='POST':
         user_name = request.POST.get('user_name')
         user_check = '是' if 'user_check' in request.POST else '否'
         user_email = request.POST.get('user_email')
         user_message = request.POST.get('user_message')

         if user_name and user_email and user_message:
               mail_body = f'''
                回饋者姓名：{user_name}
                是否第一次預約：{user_check}
                電子郵件：{user_email}
                反應意見:
                {user_message}
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
    return render(request, 'ContactForm.html', {'message': message})