from django.urls import path
from .views import product_dashboard

urlpatterns = [
    path('',product_dashboard, name='product_dashboard'),
]
