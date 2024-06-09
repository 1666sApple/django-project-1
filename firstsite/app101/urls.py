from django.urls import path, include
from app101 import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.home, name='home'),
    path('item/', views.item, name='item'),
]
