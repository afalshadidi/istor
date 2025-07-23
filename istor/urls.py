# istor/urls.py

from django.contrib import admin
from django.urls import path, include
from store.views import home_view  # استدعاء العرض
from store import views  # أو المسار الصحيح إلى دالة home
urlpatterns = [
    path('', home_view, name='home'),  # هذه السطر مهم ليكون هو المسار الجذري
    path('admin/', admin.site.urls),
    path('store/', include('store.urls')),
    path('register/', include('accounts.urls')),
    path('login/', include('accounts.urls')),
    path('logout/', include('accounts.urls')),
    path('dashboard/', include('dashboard.urls')),
]
