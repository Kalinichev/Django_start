from django.urls import path
from .views import products, contact

urlpatterns = [
    path('products/', products, name='products'),
    path('contact/', contact, name='contact'),
]