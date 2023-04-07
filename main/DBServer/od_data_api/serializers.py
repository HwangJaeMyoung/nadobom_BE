from rest_framework import serializers
from .models import od_data,image,S3MediaStorage
class OdDataSerializer(serializers.ModelSerializer):
    label = serializers.FileField()
    class Meta:
        model = od_data
        fields = ("image_id", "label")
        
# class OdDataSerializer(serializers.ModelSerializer):
#     label = serializers.FileField(write_only=True)
    
#     class Meta:
#         model = od_data
#         fields = ("image_id", "label")

#     def create(self, validated_data):
#         label_file = validated_data.pop('label')
#         storage = CustomS3Boto3Storage()
#         label_path = f'media/od_data/labels/{label_file.name}'
#         storage.save(label_path, label_file)
#         validated_data['label'] = label_path
#         return super().create(validated_data)