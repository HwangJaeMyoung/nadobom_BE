from rest_framework.parsers import MultiPartParser, FormParser
from django.http import HttpResponse, JsonResponse
from .serializers import ImageSerializer
from .models import image
from rest_framework import generics
from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings

s3_storage = S3Boto3Storage()

class ImageListCreate(generics.ListCreateAPIView):
    queryset = image.objects.all()
    serializer_class = ImageSerializer
    parser_classes = [MultiPartParser]
    serializer_class.Meta.fields = ('id', 'image')
    # def perform_create(self, serializer):
    #     serializer.save()

    # def get_serializer_context(self):
    #     context = super().get_serializer_context()
    #     context['request'] = self.request
    #     return context

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     for obj in qs:
    #         obj.image_url = settings.AWS_S3_CUSTOM_DOMAIN + obj.image.name
    #     return qs

class ImageRetrieveDestroy(generics.RetrieveDestroyAPIView):
    queryset = image.objects.all()
    serializer_class = ImageSerializer
    lookup_field = 'id'

# class ImageUpdate(generics.UpdateAPIView):
#     queryset = image.objects.all()
#     serializer_class = ImageSerializer
#     parser_classes = [MultiPartParser]