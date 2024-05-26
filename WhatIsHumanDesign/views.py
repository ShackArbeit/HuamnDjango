from django.shortcuts import render
from .models import LayoutWhat,YourBooks

def Hover_Layout(request):
      designs=LayoutWhat.objects.all()
      return render(request, 'LayoutWhat.html', {'designs': designs})

# 人類圖是你人生使用說明書的部分
def Human_Books(request,sub_router):
      your_books=YourBooks.objects.all()
      content_url=sub_router
      layout_url=LayoutWhat.objects.get(content_url=content_url)
      return render(request,'YourBooks.html',{'layout': layout_url, 'your_books': your_books})

