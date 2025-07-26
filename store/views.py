from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm  # ✅ استدعاء الفورم الجديد لإضافة المنتجات

def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

def home_view(request):
    products = Product.objects.all()[:6]  # أو بدون [:6] لعرض الكل
    return render(request, 'home.html', {'products': products})

def add_product_view(request):  # ✅ عرض نموذج إضافة منتج مع رفع صورة
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # أو أي صفحة أخرى
    else:
        form = ProductForm()
    return render(request, 'store/add_product.html', {'form': form})
