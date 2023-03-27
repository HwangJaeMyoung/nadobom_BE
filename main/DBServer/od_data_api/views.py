from rest_framework.parsers import MultiPartParser, FormParser
from django.http import HttpResponse, JsonResponse
from .serializers import OdDataSerializer
from .models import od_data,image
from rest_framework import generics
from rest_framework.response import Response
import rest_framework.status as status
import os
from django.conf import settings
from io import StringIO
from django.core.files.uploadedfile import InMemoryUploadedFile


class OdDataListCreate(generics.ListCreateAPIView):
    queryset = od_data.objects.all()
    serializer_class = OdDataSerializer
    def post(self, request, *args, **kwargs):
        label = request.POST.get('label')
        image_id = request.POST.get('image_id')
        # image.objects.filter(id=id)
        # "image": "http://127.0.0.1:8000/media/FP5jE4YaIAgXPct.jpg",
        label_file = StringIO(label)
        label_upload_file = InMemoryUploadedFile(
            label_file, None, f'{image_id}.txt', 'text/plain', len(label), None)
        serializer = self.get_serializer(data={"image_id": image_id, "label": label_upload_file})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


    # def post(self, request, *args, **kwargs):
    #     label = request.POST.get('label')

    #     file_path = 'path/to/file.txt'
    #     file_path = 'path/to/file.txt'
    #     with open(file_path, 'w') as f:
    #         f.write(label)

    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     xml = request.FILES['label']
    #     file_path = f'media/od_data/{xml.name}'
    #     with open(file_path, 'wb+') as f:
    #         for chunk in xml.chunks():
    #             f.write(chunk)
    #     serializer.save(xml=file_path)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
class OdDataRetrieveDestroy(generics.RetrieveDestroyAPIView):
    queryset = od_data.objects.all()
    serializer_class = OdDataSerializer
    lookup_field = 'id'


