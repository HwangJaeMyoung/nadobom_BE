from django.db import models
from storages.backends.s3boto3 import S3Boto3Storage

class S3MediaStorage(S3Boto3Storage):
    location = 'media'
    file_overwrite = False

class image(models.Model):
    image = models.ImageField(upload_to='images/',storage=S3MediaStorage())
    created_at = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)
    # image_url = models.URLField(blank=True)
    # def save(self, *args, **kwargs):
    #     if self.image:
    #         self.image_url = self.image.url
    #     super().save(*args, **kwargs)