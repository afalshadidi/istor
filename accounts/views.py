# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# عرض تسجيل مستخدم جديد
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # توجيه المستخدم إلى صفحة تسجيل الدخول بعد التسجيل
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


# عرض تسجيل الدخول
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # توجيه المستخدم إلى الصفحة الرئيسية بعد تسجيل الدخول
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


# تسجيل الخروج
def logout_view(request):
    logout(request)
    return redirect('home')  # توجيه المستخدم إلى الصفحة الرئيسية بعد تسجيل الخروج
