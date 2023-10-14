from django.contrib import admin
from django.urls import path

from rest_framework import routers
from django.urls import include, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve


urlpatterns = [
  #  path("admin/", admin.site.urls),
    path('api/image/', include('image_api.urls')),
    path("api/od_data/",include('od_data_api.urls')),
    path("api/seg_data/",include('seg_data_api.urls')),
    path("api/report/",include('report_api.urls')),
    path("download/",include('download.urls'))
]
