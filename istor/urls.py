# istor/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from store.views import home_view

urlpatterns = [
    path('', home_view, name='home'),

    # لوحة التحكم
    path('admin/', admin.site.urls),

    # المتجر
    path('store/', include('store.urls')),

    # الحسابات (جميع المسارات من نفس الملف)
    path('', include('accounts.urls')),

    # لوحة التحكم
    path('dashboard/', include('dashboard.urls')),
]

# دعم ملفات media أثناء التطوير
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# دعم ملفات static أثناء التطوير (اختياري إن لم تستخدم collectstatic للعرض المباشر)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
