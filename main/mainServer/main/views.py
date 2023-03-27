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
def main_post(request):
    parser_classes = [MultiPartParser]
    image= request.FILES.get('image')
    response = requests.post(url=getDB_URL("image"), files={'image': image})
    label=request.POST.get('label')
    response_dict=response.json()
    image_id=response_dict["id"]
    response = requests.post(url=getDB_URL("od_data"),data={'image_id': image_id,"label": label})
    return Response(response.json())


