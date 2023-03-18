from django.db import models

class image(models.Model):
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)
