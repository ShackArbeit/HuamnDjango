from django.shortcuts import render
from .models import BookingProcess,ServiceItems

def index(request):
      bookings=BookingProcess.objects.all()
      services=ServiceItems.objects.all()
      return render(request,'./index.html',{'bookings': bookings,'services':services})
