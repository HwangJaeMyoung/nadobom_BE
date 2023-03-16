from django.db import models

class Test(models.Model):
    ID= models.CharField(max_length=30,primary_key=True)
    name=models.CharField(max_length=10)

# Create your models here.
