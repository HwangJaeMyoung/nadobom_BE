from django.contrib import admin
from django.urls import path

from rest_framework import routers
from django.urls import include, re_path
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
from download import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/image/', include('image_api.urls')),
    path("api/od_data/",include('od_data_api.urls')),
    path("download/",views.export_images,name="download")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)