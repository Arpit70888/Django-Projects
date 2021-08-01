from django.contrib import admin
from django.urls import path,include
from rest_framework import views
from .import views

urlpatterns = [
    path('list/', views.ShowAll, name='list'),
    path('product/<int:pk>', views.ShowOne, name='product'),
    path('insertProduct', views.insertProduct, name='insertProduct'),
    path('update/<int:pk>', views.UpdateProduct, name='update'),
    path('delete/<int:pk>', views.DeleteProduct, name='delete')


]