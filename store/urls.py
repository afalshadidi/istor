# store/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list_view, name='product_list'),
]
