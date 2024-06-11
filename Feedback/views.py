from django.shortcuts import render
from Feedback import models

def Feedback(request):
      return render(request,'./Feedback.html',locals())

def Listing(request):
      values=models.Value.objects.all()
      posts=models.Post.objects.filter(enabled=True).order_by('-pub_time')[:150]
      return render(request,'Listing.html',locals())

def Posting(request):
      values=models.Value.objects.all()
      message='如要張貼回饋，每一個欄位都需要填寫!'
      return render(request,'Posting.html',locals())

def del_Post(request):
      pass