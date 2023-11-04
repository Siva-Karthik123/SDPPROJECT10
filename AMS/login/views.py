from django.shortcuts import render,redirect
from django.db.models import Q
from .models import Admin,Dealer,Cars
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    #return HttpResponse("<h1>Home Page</h1>")
    return render(request,'login/home/home.html')

def mod_home(request):
    return render(request,'login/models/home.html')

def slavia(request):
    return render(request,'login/models/slavia.html')

def kushaq(request):
    return render(request,'login/models/kushaq.html')
def kodiaq(request):
    return render(request,'login/models/kodiaq.html')
def superb(request):
    return render(request,'login/models/superb.html')

def login(request):
    return render(request,'login/home/login.html')
def service_home(request):
    return render(request,'login/service/home.html')
def service(request):
    return render(request,'login/service/service.html')
def register(request):
    return render(request, "login/home/register.html")

def addregister(request):
    if request.method == 'POST':
        name = request.POST['uname']
        password = request.POST['pwd']
        new_id = Dealer(username=name,password=password)
        new_id.save()
        return redirect('lhome')

def dealeraddregister(request):
    if request.method == 'POST':
        name = request.POST['uname']
        password = request.POST['pwd']
        new_id = Dealer(username=name,password=password)
        new_id.save()
        return redirect('dhome')

def towtruck(request):
    return render(request,'login/service/towtruck.html')

def checklogin(request):
    name = request.POST["uname"]
    password = request.POST["pwd"]
    flag = Admin.objects.filter(Q(username=name) & Q(password=password))
    print(flag)

    if flag:
        return redirect('lhome')
    else:
        return redirect('login')

def dealerchecklogin(request):
    name = request.POST["uname"]
    password = request.POST["pwd"]
    flag = Dealer.objects.filter(Q(username=name) & Q(password=password))
    print(flag)

    if flag:
            return redirect('dhome')
    else:
        return redirect('login')