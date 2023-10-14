from rest_framework.parsers import MultiPartParser, FormParser,JSONParser
from django.http import HttpResponse, JsonResponse
from .serializers import OdDataSerializer,LabeledOdDataSerializer
from .models import od_data,image,labeled_od_data
from rest_framework import generics
from rest_framework.response import Response
import rest_framework.status as status
import os
from django.conf import settings
from io import StringIO,BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from rest_framework.parsers import  JSONParser,MultiPartParser

class OdDataListCreate(generics.ListCreateAPIView):
    parser_classes = [MultiPartParser, JSONParser]
    queryset = od_data.objects.all()
    serializer_class = OdDataSerializer
    def create_txt(self, data):
        data=data.copy()
        file_content = data['label']
        file_id = data['image_id']
        image_=image.objects.get(id=file_id)
        image_name = os.path.basename(image_.image.name)
        label_name, _ = os.path.splitext(image_name)

        file_name=label_name
        file_content_bytes = file_content.encode('utf-8')
        file_object = BytesIO(file_content_bytes)
        
        in_memory_file = InMemoryUploadedFile(
            file_object, None, f'{file_name}.txt', 'text/plain',
            file_object.getbuffer().nbytes, None)
        data['label'] = in_memory_file
        return data
    def create(self, request, *args, **kwargs):
        data=self.create_txt(request.data)
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
class OdDataRetrieveDestroy(generics.RetrieveDestroyAPIView):
    queryset = od_data.objects.all()
    serializer_class = OdDataSerializer
    lookup_field = 'id'


class LabeledOdDataListCreate(generics.ListCreateAPIView):
    parser_classes = [MultiPartParser, JSONParser]
    queryset =  labeled_od_data.objects.all()
    serializer_class = LabeledOdDataSerializer
    def delete(self, request, *args, **kwargs):
        self.queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LabeledOdDataRetrieveDestroy(generics.RetrieveDestroyAPIView):
    queryset = labeled_od_data.objects.all()
    serializer_class = OdDataSerializer
    lookup_field = 'id'
