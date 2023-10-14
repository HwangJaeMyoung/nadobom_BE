from rest_framework.parsers import MultiPartParser, FormParser,JSONParser
from django.http import HttpResponse, JsonResponse
from .serializers import ReportSerializer
from .models import image,report
from rest_framework import generics
from rest_framework.response import Response
import rest_framework.status as status
import os
from django.conf import settings
from io import StringIO,BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from rest_framework.parsers import  JSONParser,MultiPartParser

class ReportListCreate(generics.ListCreateAPIView):
    parser_classes = [MultiPartParser, JSONParser]
    queryset = report.objects.all()
    serializer_class = ReportSerializer



