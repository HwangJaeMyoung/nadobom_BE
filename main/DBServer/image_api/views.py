from rest_framework.parsers import MultiPartParser, FormParser
from django.http import HttpResponse, JsonResponse
from .serializers import ImageSerializer
from .models import image
from rest_framework import generics,status
from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings
from rest_framework.response import Response

s3_storage = S3Boto3Storage()

class ImageListCreate(generics.ListCreateAPIView,generics.DestroyAPIView):
    queryset = image.objects.all()
    serializer_class = ImageSerializer
    parser_classes = [MultiPartParser]
    serializer_class.Meta.fields = ('id', 'image')
    def delete(self, request, *args, **kwargs):
        self.queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ImageRetrieveDestroy(generics.RetrieveDestroyAPIView):
    queryset = image.objects.all()
    serializer_class = ImageSerializer
    lookup_field = 'id'

# class ImageUpdate(generics.UpdateAPIView):
#     queryset = image.objects.all()
#     serializer_class = ImageSerializer
#     parser_classes = [MultiPartParser]

