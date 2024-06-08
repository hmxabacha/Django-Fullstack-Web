from django.shortcuts import render
from .models import BookingModel
from .forms import BookingForm
from django.contrib import messages

# Create your views here.

def booking(request):
    
    form=BookingForm()
    if request.method == 'POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Booking Successful!")
    return render(request,"booking.html",{'form':form}) 

def reservations(request):
    data = BookingModel.objects.all()
    return render(request,"reservations.html",{'data':data})

       
    
