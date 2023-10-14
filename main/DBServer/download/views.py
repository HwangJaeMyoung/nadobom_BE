import zipfile,csv
from django.http import HttpResponse, FileResponse
from io import BytesIO,StringIO
import requests
# from od_data_api import models
from image_api.models import image
from od_data_api.models import od_data,labeled_od_data
from seg_data_api.models import seg_data
from report_api.models import report
from django.conf import settings
from zipfile import ZipFile
from PIL import Image
from image_api.models import S3MediaStorage
import os

storage = S3MediaStorage()

def export_od_images(request):
    od_data_list = od_data.objects.all()
    zip_filename = 'exported_od_images.zip'
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

def export_seg_images(request):
    seg_data_list = seg_data.objects.all()
    zip_filename = 'exported_seg_images.zip'
    zip_buffer = BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        
        
        for data in seg_data_list:
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

def export_report_images(request):
    report_data_list = report.objects.all()
    zip_filename = 'exported_report_images.zip'
    zip_buffer = BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            csv_data = StringIO()
            csv_data.write(u'\ufeff')
            writer = csv.writer(csv_data)
            writer.writerow(['image', 'latitude', 'longitude', 'location'])
            for data in report_data_list:
                image = data.image_id
                image_path=image.image.name
                image_file = storage.open(image_path)
                image_data = image_file.read()
                zip_file.writestr(image_path, image_data)
                print(data.location)
                writer.writerow([os.path.basename(image_path),data.latitude,data.longitude,data.location])
            zip_file.writestr('report.csv', csv_data.getvalue().encode("utf-8"))

    response = HttpResponse(zip_buffer.getvalue(), content_type='application/zip')
    response['Content-Disposition'] = f'attachment; filename="{zip_filename}"'
    return response



def export_labeled_od_images(request):
    report_data_list = labeled_od_data.objects.all()
    zip_filename = 'exported_labeled_od_images.zip'
    zip_buffer = BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            csv_data = StringIO()
            # csv_data.write(u'\ufeff')
            writer = csv.writer(csv_data)
            writer.writerow(['image_id', 'image_name'])
            for data in report_data_list:
                image = data.image_id
                image_path=image.image.name
                image_file = storage.open(image_path)
                image_data = image_file.read()
                zip_file.writestr(image_path, image_data)
                writer.writerow([image.id,os.path.basename(image_path)])
            zip_file.writestr('img_ids.csv', csv_data.getvalue().encode("utf-8"))

    response = HttpResponse(zip_buffer.getvalue(), content_type='application/zip')
    response['Content-Disposition'] = f'attachment; filename="{zip_filename}"'
    return response