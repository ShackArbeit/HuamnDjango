# from django.shortcuts import render
# from .models import LayoutWhat,YourBooks,YourType

# def Hover_Layout(request):
#       designs=LayoutWhat.objects.all()
#       return render(request, 'LayoutWhat.html', {'designs': designs})

# # 人類圖是你人生使用說明書的部分
# def Human_Books(request,sub_router):
#       your_books=YourBooks.objects.all()
#       content_url=sub_router
#       layout_url=LayoutWhat.objects.get(content_url=content_url)
#       return render(request,'YourBooks.html',{'layout': layout_url, 'your_books': your_books})

# # 類型 = 你的天職部分
# def Human_Types(request,sub_router2):
#       your_types=YourType.objects.all()
#       content_url=sub_router2
#       layout_url=LayoutWhat.objects.get(content_url=content_url)
#       return render(request,'YourType.html',{'layout':layout_url,'your_types':your_types})

from django.shortcuts import render, get_object_or_404
from .models import LayoutWhat, YourBooks, YourType

def Hover_Layout(request):
    designs = LayoutWhat.objects.all()
    return render(request, 'LayoutWhat.html', {'designs': designs})

# 人類圖是你人生使用說明書的部分
def Human_Books(request, sub_router):
    your_books = YourBooks.objects.all()
    layout_url = get_object_or_404(LayoutWhat, content_url=sub_router)
    return render(request, 'YourBooks.html', {'layout': layout_url, 'your_books': your_books})

# 類型 = 你的天職部分
def Human_Types(request, sub_router2):
    your_types = YourType.objects.all()
    layout_url = get_object_or_404(LayoutWhat, content_url=sub_router2)
    return render(request, 'YourType.html', {'layout': layout_url, 'your_types': your_types})
