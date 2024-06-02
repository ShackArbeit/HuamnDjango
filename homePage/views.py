from django.shortcuts import render
from .models import BookingProcess

def index(request):
      bookings=BookingProcess.objects.all()
      return render(request,'./index.html',{'bookings': bookings})
