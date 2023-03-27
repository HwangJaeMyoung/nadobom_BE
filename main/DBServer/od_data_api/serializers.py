from rest_framework import serializers
from .models import od_data,image

class OdDataSerializer(serializers.ModelSerializer):
    label=serializers.FileField()
    class Meta:
        model = od_data
        fields = "__all__"

    
    
