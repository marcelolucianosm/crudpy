# crud_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_items, name='list_items'),
    path('item/<int:pk>/', views.view_item, name='view_item'),
    path('create/', views.create_item, name='create_item'),
    path('update/<int:pk>/', views.update_item, name='update_item'),
    path('delete/<int:pk>/', views.delete_item, name='delete_item'),
]
