"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from pages import views

urlpatterns = [
    path('lotto/<int:n1>/<int:n2>/<int:n3>/<int:n4>/<int:n5>/<int:n6>/<int:n7>/', views.lotto),
    path('ispal/<str:word>/', views.ispal),
    path('isbirth/<int:month>/<int:day>/', views.isbirth),
    path('template_language/', views.template_language),
    path('area/<int:radius>/', views.area),
    path('times/<int:number1>/<int:number2>/', views.times),
    path('introduce2/', views.introduce2),
    path('hello/<str:name>/', views.hello),
    path('image/<int:weight>/<int:height>/', views.image),
    path('dinner/', views.dinner),
    path('introduce/', views.introduce),
    path('index/', views.index),
    path('admin/', admin.site.urls),
]
