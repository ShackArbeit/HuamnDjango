from django.shortcuts import render
from .models import LayoutWhat,YourBooks,YourType,YourRole,YourAuth,YourEnergy,YourRoad,YourMin,YourFather

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

# 人生角色 的部分
def Human_Roles(request):
       your_roles=YourRole.objects.all()
       return render(request,'YourRole.html',locals())

# 內在權威 = 做決定的方法 的部分
def Human_Auths(request):
       your_auths=YourAuth.objects.all()
       return render(request,'YourAuth.html',locals())

# 能量中心 = 你的強弱 的部分
def Human_Energys(request):
       your_enrygys=YourEnergy.objects.all()
       return render(request,'YourEnergy.html',locals())

# 通道 = 你的天賦 的部分
def Human_Roads(request):
       your_roads=YourRoad.objects.all()
       return render(request,'YourRoad.html',locals())

# 輪迴交叉 = 你的命運 的部分
def Human_Mins(request):
       your_mins=YourMin.objects.all()
       return render(request,'YourMins.html',locals())

 # Ra Uru Hu = 引進人類圖 的部分
def Human_Father(request):
       your_fathers=YourFather.objects.all()
       return render(request,'YourFather.html',locals())