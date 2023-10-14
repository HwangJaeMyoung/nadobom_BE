from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

url_set = {"main":"http://52.79.236.33:8000","DB":'http://54.180.116.44:8000'}

def get_url(request,data):
    return HttpResponse(url_set[data])

    