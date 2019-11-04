from django.contrib import admin
from django.urls import path, include
from . import views

app_name="articles"
urlpatterns = [
    path('index/', views.index, name="index"),    # READ -> List
    # path('new/', views.new, name="new"),        # CREATE -> 생성 폼을 던져주는 
    path('create/', views.create, name="create"),      # CREATE -> 폼 데이터를 받아서 DB 저장
    path('<int:article_pk>/', views.detail, name="detail"),    # READ -> Detail
    path('<int:article_pk>/delete/', views.delete, name="delete"),
    # path('<int:article_pk>/edit/', views.edit, name="edit"),    # UPDATE -> 수정 폼 던져주기
    path('<int:article_pk>/update/', views.update, name="update"),    # UPDATE -> 폼 데이터 받아서 DB 저장
]