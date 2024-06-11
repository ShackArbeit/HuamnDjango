from django.shortcuts import render


def UserBack(request):
      return render(request,'UserBack.html',locals())