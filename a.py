def download_zip(request,data):
    if data not in data_names:
        return HttpResponse("data name incorrect ")

    db_server_url = f"{DB_URL}/download/{data}"
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
