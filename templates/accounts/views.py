from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .models import UserProfile

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # إنشاء ملف شخصي للمستخدم
            UserProfile.objects.create(user=user)
            messages.success(request, "تم إنشاء الحساب بنجاح، يمكنك الآن تسجيل الدخول.")
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"مرحبًا بك يا {user.username}")
            return redirect('home')
        else:
            messages.error(request, "بيانات الدخول غير صحيحة.")
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})
