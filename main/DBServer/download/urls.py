from django.urls import path, include
from . import views

urlpatterns = [
    path('od_data', views.export_od_images, name='export_od_data'),
    path('report_data', views.export_report_images, name='export_report_data'),
    path('od_data/labeled', views.export_labeled_od_images, name='export_labeled_od_image_data'),
]