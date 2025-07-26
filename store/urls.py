from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list_view, name='product_list'),
    path('products/add/', views.add_product_view, name='add_product'),  # ✅ إضافة مسار لإضافة منتج
]
