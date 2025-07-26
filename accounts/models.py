from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} Profile"

# 📬 إرسال إيميل ترحيبي عند إنشاء حساب مستخدم جديد
@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        subject = '🎉 Welcome to iStor!'
        message = f'''
        Hello {instance.username},

        Thank you for registering on iStor.
        We're glad to have you with us!

        📌 Your account has been created successfully.
        '''
        recipient = [instance.email]

        if instance.email:  # للتأكد أن البريد مسجّل
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                recipient,
                fail_silently=False
            )
