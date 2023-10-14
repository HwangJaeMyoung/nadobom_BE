from rest_framework import serializers
from .models import seg_data,image,S3MediaStorage

class SegDataSerializer(serializers.ModelSerializer):
    label = serializers.FileField()
    class Meta:
        model = seg_data
        fields = ("image_id", "label")

