from django.shortcuts import render
from .models import FreeVideos


def FreeInfomation(request):
      videos=FreeVideos.objects.all()
      return render(request,'./CardInfo.html',locals())