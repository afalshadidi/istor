# store/views.py
from django.shortcuts import render
from .models import Product

def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})
def home_view(request):
    products = Product.objects.all()[:6]  # أو بدون [:6] لعرض الكل
    return render(request, 'home.html', {'products': products})
