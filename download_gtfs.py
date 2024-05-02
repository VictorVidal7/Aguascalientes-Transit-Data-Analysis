import requests
import zipfile
import os

def download_and_extract(url, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    local_file = os.path.join(output_directory, "aguascalientes_gtfs.zip")
    
    print("Downloading the file...")
    response = requests.get(url)
    with open(local_file, 'wb') as file:
        file.write(response.content)
    print("Download completed.")
    
    print("Extracting the file...")
    with zipfile.ZipFile(local_file, 'r') as zip_ref:
        zip_ref.extractall(output_directory)
    print("Extraction completed.")
    
    print("Extracted files:")
    for file in os.listdir(output_directory):
        print(file)

url_gtfs = "https://s3.gtfs.pro/files/uran/improved-gtfs-mx-aguascalientes.zip"
output_directory = "aguascalientes_gtfs"

download_and_extract(url_gtfs, output_directory)
