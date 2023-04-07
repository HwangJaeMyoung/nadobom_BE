import zipfile
from django.http import HttpResponse, FileResponse
from io import BytesIO,StringIO
import requests
# from od_data_api import models
from image_api.models import image
from od_data_api.models import od_data
import os
from django.conf import settings
from zipfile import ZipFile
from PIL import Image
from image_api.models import S3MediaStorage

storage = S3MediaStorage()

def export_images(request):
    s3_client = boto3.client('s3')
    od_data_list= od_data.objects.all()
    zip_filename = 'exported_images.zip'
    zip_buffer = BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for data in od_data_list:
            image=data.image_id
            image_name = os.path.basename(image.image.name)
            image_path = image.image.path
            zip_file.write(image_path, f"image/{image_name}")
            label_name,_=os.path.splitext(image_name)
            label_path = data.label.path
            zip_file.write(label_path, f"od_data/labels/{label_name}.txt")

    response = HttpResponse(zip_buffer.getvalue(), content_type='application/zip')
    response['Content-Disposition'] = f'attachment; filename="{zip_filename}"'
    return response

def export_images(request):
    od_data_list = od_data.objects.all()
    zip_filename = 'exported_images.zip'
    zip_buffer = BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for data in od_data_list:
            image = data.image_id
            image_path=image.image.name
            label_path = data.label.name

            image_file = storage.open(image_path)
            image_data = image_file.read()
            zip_file.writestr(image_path, image_data)

            label_file = storage.open(label_path)
            label_data = label_file.read()
            zip_file.writestr(label_path, label_data)

    response = HttpResponse(zip_buffer.getvalue(), content_type='application/zip')
    response['Content-Disposition'] = f'attachment; filename="{zip_filename}"'
    return response