from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

import requests
import json
import torch
from PIL import Image
import matplotlib.pyplot as plt
import os
from django.views.decorators.csrf import csrf_exempt
import zipfile
import shutil



def download_labeled_od_date():
    db_server_url = f"{DB_URL}/download/od_data/labeled"
    response = requests.get(db_server_url)
    if response.status_code == 200:
        zip_filename = f"exported_od_data_images.zip"
        zip_file_path = os.path.join("media", "downloads/od_data", zip_filename)
        with open(zip_file_path, "wb") as f:
            f.write(response.content)
        
        with open(zip_file_path, "rb") as f:
            zip_buffer = BytesIO(f.read())
        response = HttpResponse(zip_buffer.getvalue(), content_type='application/zip')
        response['Content-Disposition'] = f'attachment; filename="{zip_filename}"'
        zip_buffer.close()
        return response
    else:
        return HttpResponse("Failed to download zip file from DB server")



def get_images_from_zip(base_path,zip_file_path):
    extracted_folder_path =os.path.join(base_path,"images")
    if os.path.exists(extracted_folder_path):
        shutil.rmtree(extracted_folder_path)
    print("A")
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(base_path)

    return os.listdir(os.path.join(extracted_folder_path))



def trans_points(array):
    x1,y1,x2,y2= array
    return [(x1+x2)/2,(y1+y2)/2,x2-x1,y2-y1]

def get_label_from_images(images):
    model = torch.hub.load("ultralytics/yolov5", "custom", path=r"media/model/best.pt")
    img_labels=[]
    for image in images:
        img = Image.open(image)
        width, height = img.size
        results = model(img)
        # print()
        boxes = results.pred[0][:, :4].cpu().numpy().tolist()
        labels = results.pred[0][:, -1].cpu().numpy().astype(int).tolist()
        boxes = [trans_points([box[0]/width,box[1]/height,box[2]/width,box[3]/height]) for box in boxes]
        img_labels.append(list(zip(labels,boxes)))

    return img_labels

@csrf_exempt
def get_label_from_zip(request):
    base_path = "media/downloads"
    if not os.path.exists(base_path):
        os.makedirs(base_path)
    zip_file_path=os.path.join(base_path,'temp.zip')
    
    with open(zip_file_path, 'wb') as f:
        # f.write(request.FILES["file"].content)
        for chunk in request.FILES["file"].chunks():
                f.write(chunk)

    images=get_images_from_zip(base_path,zip_file_path)
    img_path = [os.path.join(base_path,"images",img) for img in images]
    
    labels =get_label_from_images(img_path)
    data= dict(zip(images,labels))

    shutil.rmtree(os.path.join(base_path))
    os.makedirs(base_path)
    return JsonResponse(data)
