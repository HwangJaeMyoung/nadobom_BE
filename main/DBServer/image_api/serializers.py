from rest_framework import serializers
from .models import image



class ImageSerializer(serializers.ModelSerializer):
    # image_url = serializers.SerializerMethodField()
    class Meta:
        model = image
        fields = ("id", "image", "created_at", "is_processed")
    # def get_image_url(self, obj):
    #     return obj.image.url

# class ReportSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = report
#         fields = ("image_id","created_at","is_broken","is_solved")

# class server_model_update_Serializer(serializers.ModelSerializer):
#     xml=serializers.FileField()
#     class Meta:
#         model = server_model_update
#         fields = ("image_id","xml")

# class mobile_model_update_Serializer(serializers.ModelSerializer):
#     xml=serializers.FileField()
#     class Meta:
#         model = mobile_model_update
#         fields = ("image_id","xml")


