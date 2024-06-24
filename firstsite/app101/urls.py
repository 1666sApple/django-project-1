from django.urls import path, include
from app101 import views

app_name = 'app101'
urlpatterns = [
    # app101
    path('', views.home, name='home'),
    
    # app101/
    path('index/', views.index, name='index'),
    path('item/', views.item, name='item'),
    path('item/<int:item_id>/', views.detail, name='detail'),
    path('add/', views.create_item, name='create_item'),
]