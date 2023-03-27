from rest_framework.parsers import MultiPartParser, FormParser
from django.http import HttpResponse, JsonResponse
from .serializers import ImageSerializer
from .models import image
from rest_framework import generics

class ImageListCreate(generics.ListCreateAPIView):
    queryset = image.objects.all()
    serializer_class = ImageSerializer
    parser_classes = [MultiPartParser]

class ImageRetrieveDestroy(generics.RetrieveDestroyAPIView):
    queryset = image.objects.all()
    serializer_class = ImageSerializer
    lookup_field = 'id'

# class ImageUpdate(generics.UpdateAPIView):
#     queryset = image.objects.all()
#     serializer_class = ImageSerializer
#     parser_classes = [MultiPartParser]