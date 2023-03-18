from rest_framework import serializers
from .models import od_data,image

class OdDataSerializer(serializers.ModelSerializer):
    xml=serializers.FileField(use_url=True,required=True)
    class Meta:
        model = od_data
        fields = ("image_id","xml")

