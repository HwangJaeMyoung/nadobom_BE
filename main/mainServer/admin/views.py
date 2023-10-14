import zipfile
from django.http import HttpResponse
from io import BytesIO
import os
import requests
from mainServer.utils import getDB_URL

import io
from django.http import HttpResponse,JsonResponse
from mainServer.utils import DB_URL
from rest_framework.decorators import api_view
from django.http import FileResponse
import shutil
import csv
import json
from PIL import Image

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

    extracted_folder_path =os.path.join(base_path,"labeled")
    if os.path.exists(extracted_folder_path):
        shutil.rmtree(extracted_folder_path)
    
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        # ZIP 파일의 모든 파일 압축 해제
        zip_ref.extractall(extracted_folder_path)
    return os.listdir(os.path.join(extracted_folder_path,"images"))

def get_img_ids_from_txt(path):
    result_list = []
    with open(path, 'r', newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            image_id = int(row['image_id'])
            image_name = row['image_name']
            result_list.append((image_id, image_name))
    return result_list


def post_img_set(img_set):
    url=f"{DB_URL}/api/od_data/"
    for img_id,img_labels in img_set:
        label=""
        for img_label in img_labels:
            points=img_label[1]
            label+=f"{img_label[0]} {points[0]} {points[1]} {points[2]} {points[3]}\n"
        data = {'image_id':img_id, "label": label}
    
        url=f"{DB_URL}/api/od_data/"
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url=url,data=json.dumps(data),headers=headers)

    #삭제하는 코드 추가
    url=f"{DB_URL}/api/od_data/labeled"
    response = requests.delete(url=url)
    return


def getAI_URL():
    return r"http://114.204.42.173:21329/main/"

def get_label_from_zip(zip_file_path):
    url = getAI_URL()
    with open(zip_file_path, 'rb') as file:
        files = {'file': file}
        response = requests.post(url, files=files)
    return response.json()



def create_od_label(request):
    response=download_labeled_od_date()
    base_path="media/downloads/od_data"
    zip_file_path=os.path.join(base_path,'temp.zip')
    with open(zip_file_path, 'wb') as f:
        f.write(response.content)

    img_list=get_images_from_zip(base_path,zip_file_path)

    img_id_csv_path= os.path.join(base_path,"labeled","img_ids.csv")
    img_ids=get_img_ids_from_txt(img_id_csv_path)
  
    json_data= get_label_from_zip(zip_file_path)

    # with open(r"media/tmp.json", 'r') as file:
    #     json_data = json.load(file)

    img_set = [(img_id,json_data[img_name]) for img_id,img_name in img_ids]
    # print(img_set)
    post_img_set(img_set)


    shutil.rmtree(base_path)
    os.makedirs(base_path)
    os.makedirs(os.path.join(base_path,"labeled"))

    return JsonResponse(dict(img_set))


data_names= {"od_data","seg_data","report_data"}

def download_zip(request,data):
    if data not in data_names:
        return HttpResponse("data name incorrect ")

    if data=="od_data":
        try:
            db_server_url=f"{DB_URL}/api/od_data/labeled"
            response = requests.get(db_server_url)
            json_data=response.json()
            if len(json_data) > 0:
                create_od_label(None)
        except:
            print("DB 서버 연결 오류")

    db_server_url = f"{DB_URL}/download/{data}"
    print(db_server_url)
    response = requests.get(db_server_url)

    if response.status_code == 200:
        zip_filename = f"exported_{data}_images.zip"
        zip_file_path = os.path.join("media", "downloads",data, zip_filename)
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



@api_view(['GET'])
def download_ptl(request):
    file_path="media/ptl/best.torchscript.ptl"
    try:
        file = open(file_path, 'rb')
        response = FileResponse(file)
        
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment; filename="best.torchscript.ptl'
        
        return response
    except IOError:
        # 파일을 찾을 수 없거나 열 수 없을 경우 404 에러를 반환합니다.
        raise Http404







