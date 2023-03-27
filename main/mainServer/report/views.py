from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser
from django.http import HttpResponse
import requests

@api_view(['POST'])
def my_view(request):
    parser_classes = [MultiPartParser]
    image= request.FILES.get('image')
    response = requests.post(url='http://127.0.0.1:8000/image/', files={'image': image})
    image_id=response.json()
    #신청
    # requests.post(url='http://127.0.0.1:8000/image/', files={'image': image})
    return Response(response.json())



