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
import json

# 무작위 문자열로 boundary 값을 생성합니다.

@api_view(['POST'])
def main_post(request):
    parser_classes = [MultiPartParser]
    url=getDB_URL("image")
    files = {'image': request.FILES.get('image')}
    response = requests.post(url, files=files)
    image_id=response.json()["id"]
    url = getDB_URL("od_data")+"labeled"
    data = {'image_id': image_id}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url=url, data=json.dumps(data),headers=headers)
    return Response(response.json())


# @api_view(['POST'])
# def main_post(request):
#     parser_classes = [MultiPartParser]
#     url=getDB_URL("image")
#     files = {'image': request.FILES.get('image')}
#     response = requests.post(url, files=files)

#     url=getDB_URL("od_data")
#     label=request.POST.get('label')
#     image_id=response.json()["id"]
#     data = {'image_id': image_id,"label":label}
#     headers = {'Content-Type': 'application/json'}
#     response = requests.post(url=url, data=json.dumps(data),headers=headers)
#     return Response(response.json())



