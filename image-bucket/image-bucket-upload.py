from google.cloud import storage
import pandas as pd
import requests
from google.cloud import storage
from concurrent.futures import ThreadPoolExecutor

bucket_name = 'bucket-name-goes-here' # Provide your unique bucket name here
CREDENTIALS_FILE = 'credentials.json' # Make sure the file is named the same way
project_id = 'your-gcp-project-id-goes-here' #Provide your project ID here
data = pd.read_csv('song_data.csv') # Make sure the file is named the same way


def upload_blob_from_url(bucket_name, image_url, destination_blob_name, project_id):
    response = requests.get(image_url)
    if response.status_code == 200:
        storage_client = storage.Client.from_service_account_json(CREDENTIALS_FILE, project=project_id)
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(destination_blob_name)
        blob.upload_from_string(response.content, content_type=response.headers['Content-Type'])
        print(f"Uploaded {destination_blob_name}")
    else:
        print(f"Failed to download image from {image_url}")


def upload_song_image(row):
    song_id = row['id']
    img_url = row['img_url']
    destination_blob_name = f"images/{song_id}.jpg"
    print(f"Processing song {song_id}")
    print(f"Downloading image from {img_url}")
    upload_blob_from_url(bucket_name, img_url, destination_blob_name, project_id)


def process_images_concurrently(data):
    with ThreadPoolExecutor(max_workers=10) as executor:  # Adjust max_workers based on your system and network capabilities
        # Use a list of futures for better error handling
        futures = [executor.submit(upload_song_image, row) for index, row in data.iterrows()]
        for future in futures:
            future.result()  # Wait for all threads to complete and catch any exceptions


process_images_concurrently(data)


# This is the single-threaded implementation
'''
for index, row in data.iterrows():
    song_id = row['id']
    img_url = row['img_url']
    destination_blob_name = f"images/{song_id}.jpg"
    print(f"Processing song {song_id}")
    print(f"Downloading image from {img_url}")
    upload_blob_from_url(bucket_name, img_url, destination_blob_name, project_id)
'''