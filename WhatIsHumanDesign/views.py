from django.shortcuts import render
from .models import LayoutWhat

def Hover_Layout(request):
      designs=LayoutWhat.objects.all()
      return render(request, 'LayoutWhat.html', {'designs': designs})


