import cloudinary
import cloudinary.uploader
import os
from dotenv import load_dotenv

# تحميل متغيرات .env
load_dotenv()

# إعداد الاتصال بـ Cloudinary
cloudinary.config(
    cloud_name=os.getenv('CLOUDINARY_CLOUD_NAME'),
    api_key=os.getenv('CLOUDINARY_API_KEY'),
    api_secret=os.getenv('CLOUDINARY_API_SECRET'),
)

# رفع صورة للاختبار
response = cloudinary.uploader.upload("test_image.jpg")
print("✅ تم رفع الصورة بنجاح:")
print("📎 رابط الصورة:", response['secure_url'])
