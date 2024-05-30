from django.shortcuts import render
from .models import LayoutWhat,YourBooks,YourType

def Hover_Layout(request):
      designs=LayoutWhat.objects.all()
      return render(request, 'LayoutWhat.html', locals())

# 人類圖是你人生使用說明書的部分
def Human_Books(request):
       your_books=YourBooks.objects.all()
       
       return render(request,'YourBooks.html',locals())

# 類型 = 你的天職部分
def Human_Types(request):
       your_types=YourType.objects.all()
       return render(request,'YourType.html',locals())

