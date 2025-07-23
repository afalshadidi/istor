# istor/urls.py

# istor/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from store.views import home_view  # استدعاء العرض

urlpatterns = [
    path('', home_view, name='home'),  # المسار الجذري - الصفحة الرئيسية
    path('admin/', admin.site.urls),
    
    # مسارات تطبيق المتجر
    path('store/', include('store.urls')),

    # مسارات الحسابات
    path('register/', include('accounts.urls')),
    path('login/', include('accounts.urls')),
    path('logout/', include('accounts.urls')),

    # مسارات لوحة التحكم
    path('dashboard/', include('dashboard.urls')),
]

# دعم ملفات media أثناء التطوير فقط
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

