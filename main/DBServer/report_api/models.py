from django.db import models
from image_api.models import image

class report(models.Model):
    image_id=models.ForeignKey(image,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_broken = models.BooleanField(default=None)
    is_solved =models.BooleanField(default=None)
