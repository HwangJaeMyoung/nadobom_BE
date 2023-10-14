from . import views
from django.urls import path, include
urlpatterns = [path('<str:data>/', views.get_url,name="get_url"),]
