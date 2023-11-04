from django.shortcuts import render,redirect
from .models import Service,CarOrders

# Create your views here.
def base(request):
    return render(request,'logout/base.html')

def home(request):
    return render(request,'logout/home/home.html')
def towtruck(request):
    return render(request,'logout/service/towtruck.html')

def mod_home(request):
    return render(request,'logout/models/home.html')

def slavia(request):
    #info = Cars.objects.all()
    return render(request,'logout/models/slavia.html')

def kushaq(request):
    return render(request,'logout/models/kushaq.html')
def kodiaq(request):
    return render(request,'logout/models/kodiaq.html')
def superb(request):
    return render(request,'logout/models/superb.html')

def login(request):
    return render(request,'logout/home/login.html')
def service_home(request):
    return render(request,'logout/service/home.html')
def service(request):
    return render(request,'logout/service/service.html')
def addService(request):
    if request.method == 'POST':
        name = request.POST['cname']
        model = request.POST['model']
        email = request.POST['email']
        phno = request.POST['phno']
        regno = request.POST['regno']
        pandd = request.POST['p&d']
        adate = request.POST['adate']
        new_id = Service(Customer_Name=name,Car_Model=model,Email=email,Phone_Number=phno,Registration_Number=regno,Pickup_and_Dropoff=pandd,Appointment_Date=adate)
        new_id.save()
        return redirect('lsuccess')
def success(request):
    return render(request,'logout/service/success.html')
def booking(request):
    return render(request,'logout/home/booking.html')
def addBooking(request):
    if request.method == 'POST':
        name = request.POST['cname']
        model = request.POST['model']
        email = request.POST['mail']
        phno = request.POST['phno']
        new_id = CarOrders(Customer_Name=name,Car_Model=model,Email=email,Phone_Number=phno)
        new_id.save()
        return redirect('lsuccess')