import zipfile
from django.http import HttpResponse
from io import BytesIO
import os
import requests
from mainServer.utils import getDB_URL

import requests
import zipfile
import io


from django.http import HttpResponse

def download_zip(request):
    db_server_url = "http://127.0.0.1:8000/download/"
    response = requests.get(db_server_url)
    if response.status_code == 200:
        zip_filename = "exported_images.zip"
        zip_file_path = os.path.join("media", "downloads", zip_filename)
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
