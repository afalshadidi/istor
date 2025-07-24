from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from accounts.models import UserProfile

def dashboard_register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            messages.success(request, "تم إنشاء الحساب بنجاح.")
            return redirect('dashboard_login')
    else:
        form = UserCreationForm()
    return render(request, 'dashboard/register.html', {'form': form})

def dashboard_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"مرحباً بك في لوحة التحكم، {user.username}")
            return redirect('home')  # غيّرها إن كانت صفحة مختلفة للمشرف
        else:
            messages.error(request, "بيانات غير صحيحة.")
    else:
        form = AuthenticationForm()
    return render(request, 'dashboard/login.html', {'form': form})
