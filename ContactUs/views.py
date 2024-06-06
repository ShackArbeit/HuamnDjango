from django.shortcuts import render,redirect





def Contact(request):
    return render(request,'ContactForm.html')

