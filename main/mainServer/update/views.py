from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser
from django.http import HttpResponse,JsonResponse
import requests
import json
from django.http import FileResponse




apk_path = "media/app"

def version_check(version):
    with open(f"{apk_path}/metadata.json","r") as f:
        data=json.load(f)
        server_version=data["elements"][0]["versionCode"]
    return True if server_version <= version else False


@api_view(['GET'])
def update_check(request,version):    
    response = {"version": version_check(version)}
    return JsonResponse(response)


@api_view(['GET'])
def update_excute(request):
    file_path="media/app/nadobom.apk"
    try:
        file = open(file_path, 'rb')
        response = FileResponse(file)
        
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment; filename="nadobom.apk"'
        
        return response
    except IOError:
        # 파일을 찾을 수 없거나 열 수 없을 경우 404 에러를 반환합니다.
        raise Http404

@api_view(['GET'])
def update_excute2(request):
    file_path="media/app/v1.5.apk"
    try:
        file = open(file_path, 'rb')
        response = FileResponse(file)
        
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment; filename="nadobom.apk"'
        
        return response
    except IOError:
        # 파일을 찾을 수 없거나 열 수 없을 경우 404 에러를 반환합니다.
        raise Http404
