from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser
from django.http import HttpResponse
import requests
import os
from mainServer.utils import getDB_URL,create_xml
from django.core.files.storage import default_storage

@api_view(['POST'])
def my_view(request):
    parser_classes = [MultiPartParser]
    image= request.FILES.get('image')
    response = requests.post(url=getDB_URL("image"), files={'image': image})
    text=request.POST.get('text')
    response_dict=response.json()
    image_id=response_dict["id"]
    create_xml(image_id,text)
    with open(f'{image_id}.xml', 'rb') as f:
        response = requests.post(url=getDB_URL("od_data"), files={'xml': f}, data={'image_id': image_id})
    if default_storage.exists(f'{image_id}.xml'):
        default_storage.delete(f'{image_id}.xml')
    return Response(response.json())


