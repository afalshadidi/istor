from django.db import models
from cloudinary.models import CloudinaryField  # ✅ لإدارة الصور عبر Cloudinary

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # ✅ حقل الصورة عبر Cloudinary
    image = CloudinaryField('image', blank=True, null=True)

    def __str__(self):
        return self.name
