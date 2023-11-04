"""
URL configuration for AMMS project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.base,name='lbase'),
    path('lbase/',views.base,name='lbase'),
    path('lhome/',views.home,name='lhome'),
    path('lmod_home/',views.mod_home,name='lmod_home'),
    path('lslavia/',views.slavia,name='lslavia'),
    path('lkushaq/',views.kushaq,name='lkushaq'),
    path('lkodiaq/',views.kodiaq,name='lkodiaq'),
    path('lsuperb/',views.superb,name='lsuperb'),
    path('lservice_home/', views.service_home, name='lservice_home'),
    path('lservice/', views.service, name='lservice'),
    path('addService/',views.addService,name='addService'),
    path('ltowtruck/', views.towtruck, name='ltowtruck'),
    path('lsuccess/', views.success, name='lsuccess'),
    path('lbooking/', views.booking, name='lbooking'),
    path('laddBooking/', views.addBooking, name='laddBooking'),
]