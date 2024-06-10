from django import forms

class ContactForm(forms.Form):
    user_name = forms.CharField(label='您的姓名', max_length=50, initial='')
    user_book = forms.BooleanField(label='是否第一次預約', required=False)
    user_email = forms.EmailField(label='電子信箱')
    user_message = forms.CharField(label='您的意見', widget=forms.Textarea)
