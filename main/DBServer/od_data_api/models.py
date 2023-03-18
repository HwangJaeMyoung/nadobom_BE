from django.db import models
from image_api.models import image

class od_data(models.Model):
    image_id=models.ForeignKey(image,on_delete=models.CASCADE)
    xml = models.FileField(upload_to='od_data/')