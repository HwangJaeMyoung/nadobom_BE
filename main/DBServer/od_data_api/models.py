from django.db import models
from image_api.models import image,S3MediaStorage

class od_data(models.Model):
    image_id = models.ForeignKey(image, on_delete=models.CASCADE)
    label = models.FileField(upload_to='od_data/labels/', storage=S3MediaStorage())