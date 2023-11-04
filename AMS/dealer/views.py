from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
# Create your views here.
from .models import Service,CarOrders
@login_required()
def dbase(request):
    return render(request,'dealer/base.html')

def dhome(request):
    return render(request,'dealer/home/home.html')

def towtruck(request):
    return render(request,'dealer/service/towtruck.html')

def mod_home(request):
    return render(request,'dealer/models/home.html')

def slavia(request):
    #info = Cars.objects.all()
    return render(request,'dealer/models/slavia.html')

def kushaq(request):
    return render(request,'dealer/models/kushaq.html')
def kodiaq(request):
    return render(request,'dealer/models/kodiaq.html')
def superb(request):
    return render(request,'dealer/models/superb.html')

def login(request):
    return render(request,'dealer/home/login.html')
def service_home(request):
    return render(request,'dealer/service/home.html')
def service(request):
    return render(request,'dealer/service/service.html')
def Orders(request):
    orders = Service.objects.all()
    paginator = Paginator(orders, 8)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,'dealer/dashboard/Orders.html',{'page_obj':page_obj})
def dashboard_home(request):
    orders=Service.objects.count()
    carorders = CarOrders.objects.count()
    return render(request,'dealer/dashboard/home.html',{'orders':orders,'carorders':carorders})

def COrders(request):
    orders =CarOrders.objects.all()
    paginator = Paginator(orders, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, 'dealer/dashboard/CarOrders.html', {'page_obj': page_obj})