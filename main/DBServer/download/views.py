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

def export_images(request):
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
            zip_file.write(label_path, f"labels/{label_name}.txt")

    response = HttpResponse(zip_buffer.getvalue(), content_type='application/zip')
    response['Content-Disposition'] = f'attachment; filename="{zip_filename}"'
    return response