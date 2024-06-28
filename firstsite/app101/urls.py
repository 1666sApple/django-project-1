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
    #add item
    path('item/add/', views.create_item, name='create_item'),
    #edit Item
    path('item/edit/<int:id>/', views.edit_item, name='edit_item'),
    #delete Item
    path('item/delete/<int:id>/', views.delete_item, name='delete_item'),
]