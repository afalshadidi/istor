from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product_name', 'status', 'total_price', 'created_at')  # استخدم أسماء الحقول الفعلية
    list_filter = ('status', 'created_at')
    search_fields = ('user__username', 'product_name')
