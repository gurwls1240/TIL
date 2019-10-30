from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:article_pk>/', views.detail),
    path('create/', views.create),
    path('new/', views.new),
    path('index/', views.index)
]