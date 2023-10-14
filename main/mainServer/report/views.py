from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser
from django.http import HttpResponse
import requests
from mainServer.utils import getDB_URL
import json
@api_view(['POST'])
def report_post(request):
    parser_classes = [MultiPartParser]

    url=getDB_URL("image")
    files = {'image': request.FILES.get('image')}
    gps=request.POST.get('location')

    response = requests.post(url, files=files)
    image_id=response.json()["id"]
    
    url = getDB_URL("report")
    gps_values=gps.split(",")

    data = {'image_id': image_id, 'latitude': float(gps_values[0]),'longitude': float(gps_values[1]),"location":gps_values[2]}
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url=url, data=json.dumps(data),headers=headers)


    return HttpResponse("성공")


