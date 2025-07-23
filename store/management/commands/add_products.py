from django.core.management.base import BaseCommand
from store.models import Product

class Command(BaseCommand):
    help = 'Add 6 sample products'

    def handle(self, *args, **kwargs):
        products = [
            {"name": "ساعة ذكية", "description": "ساعة ذكية مقاومة للماء بخاصية تتبع اللياقة", "price": 299.99},
            {"name": "سماعات بلوتوث", "description": "سماعات لاسلكية بصوت عالي الجودة", "price": 149.50},
            {"name": "لابتوب حديث", "description": "لابتوب بأداء قوي ومناسب للأعمال", "price": 3899.00},
            {"name": "هاتف ذكي", "description": "هاتف بشاشة كبيرة وكاميرا احترافية", "price": 2499.95},
            {"name": "شاحن متنقل", "description": "باور بانك بسعة 10000mAh", "price": 89.00},
            {"name": "كاميرا رقمية", "description": "كاميرا عالية الدقة للصور والفيديو", "price": 1199.75},
        ]

        for product_data in products:
            Product.objects.create(**product_data)

        self.stdout.write(self.style.SUCCESS('✅ تم إضافة 6 منتجات بنجاح.'))
