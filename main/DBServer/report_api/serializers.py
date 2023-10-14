from rest_framework import serializers
from image_api.models import image
from .models import report


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = report
        fields = '__all__'

