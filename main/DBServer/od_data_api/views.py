from rest_framework.parsers import MultiPartParser, FormParser
from django.http import HttpResponse, JsonResponse
from .serializers import OdDataSerializer
from .models import od_data
from rest_framework import generics
from rest_framework.response import Response
import rest_framework.status as status

# Create your views here.
class OdDataListCreate(generics.ListCreateAPIView):
    queryset = od_data.objects.all()
    serializer_class = OdDataSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        xml = request.FILES['xml']
        file_path = f'media/od_data/{xml.name}'
        with open(file_path, 'wb+') as f:
            for chunk in xml.chunks():
                f.write(chunk)
        serializer.save(xml=file_path)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
class OdDataRetrieveDestroy(generics.RetrieveDestroyAPIView):
    queryset = od_data.objects.all()
    serializer_class = OdDataSerializer
    lookup_field = 'id'
