from . import views
from django.urls import path, include
urlpatterns = [path('', views.get_label_from_zip,name="get_label_from_zip"),]
