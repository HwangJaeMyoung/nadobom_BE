from django.urls import path, include
from . import views
urlpatterns = [
    path('download/<str:data>/', views.download_zip,name="download_data"),
    path('download/ptl', views.download_ptl,name="download_ptl"),
    path('download/od_data/labeled', views.create_od_label,name="download_labeled_data"),
]