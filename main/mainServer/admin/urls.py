from django.urls import path, include
from . import views
urlpatterns = [
    path('download/od_data/', views.download_zip,name="download")

]