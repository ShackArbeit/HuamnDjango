from django.shortcuts import render
from .models import aboutJeorme


def AboutJerome(request):
      abouts=aboutJeorme.objects.all()
      return render(request,'./aboutJerome.html',locals())
