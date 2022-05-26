from django.urls import path
from .views import products, contact, main

urlpatterns = [
    path('', main, name='main'),
    path('products/', products, name='products'),
    path('contact/', contact, name='contact'),
    path('products/<int:pk>/', products, name='category'),
]