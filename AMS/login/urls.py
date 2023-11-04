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
    path('',views.home,name='home'),
    path('home/',views.home,name='home'),
    path('mod_home/',views.mod_home,name='mod_home'),
    path('login/',views.login,name='login'),
    path('slavia/',views.slavia,name='slavia'),
    path('kushaq/',views.kushaq,name='kushaq'),
    path('kodiaq/',views.kodiaq,name='kodiaq'),
    path('superb/',views.superb,name='superb'),
    path('service_home/',views.service_home,name='service_home'),
    path('service/',views.service,name='service'),
    path('towtruck/',views.towtruck,name='towtruck'),
    path('register/',views.register,name='register'),
    path('checklogin/',views.checklogin,name='check_login'),
    path('dealerchecklogin/',views.dealerchecklogin,name='dealercheck_login'),
    path('addregister/',views.addregister,name='addregister'),
    path('dealeraddregister/',views.dealeraddregister,name='dealeraddregister'),
]
