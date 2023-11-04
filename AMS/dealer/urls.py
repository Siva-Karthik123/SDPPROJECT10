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
    path('',views.dbase,name='dbase'),
    path('dbase/',views.dbase,name='dbase'),
    path('dhome/',views.dhome,name='dhome'),
    path('dmod_home/',views.mod_home,name='dmod_home'),
    path('dslavia/',views.slavia,name='dslavia'),
    path('dkushaq/',views.kushaq,name='dkushaq'),
    path('dkodiaq/',views.kodiaq,name='dkodiaq'),
    path('dsuperb/',views.superb,name='dsuperb'),
    path('dservice_home/', views.service_home, name='dservice_home'),
    path('dservice/', views.service, name='dservice'),
    path('dtowtruck/', views.towtruck, name='dtowtruck'),
    path('ddashboard_home/',views.dashboard_home,name='ddashboard_home'),
    path('dOrders/',views.Orders,name='dOrders'),
    path('dCarOrders/',views.COrders,name='dCarOrders')
]