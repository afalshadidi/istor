# istor/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from store.views import home_view

urlpatterns = [
    # الصفحة الرئيسية
    path('', home_view, name='home'),

    # لوحة التحكم
    path('admin/', admin.site.urls),

    # المتجر
    path('store/', include('store.urls')),

    # الحسابات (تسجيل الدخول، إنشاء حساب، تسجيل الخروج)
    path('accounts/', include('accounts.urls')),

    # لوحة تحكم المستخدمين
    path('dashboard/', include('dashboard.urls')),
]

# ملفات media أثناء التطوير
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# ملفات static أثناء التطوير (اختياري)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
