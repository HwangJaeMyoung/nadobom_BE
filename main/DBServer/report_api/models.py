from django.db import models
from image_api.models import image

class report(models.Model):
    image_id=models.ForeignKey(image,on_delete=models.CASCADE)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    location = models.CharField(max_length=255, default='0')
    created_at = models.DateTimeField(auto_now_add=True)
    is_broken = models.BooleanField(default=False)
    is_solved =models.BooleanField(default=False)