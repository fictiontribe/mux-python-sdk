import os
import requests
import time

# Mux API credentials
ACCESS_TOKEN = 'YOUR_MUX_ACCESS_TOKEN'
SECRET_KEY = 'YOUR_MUX_SECRET_KEY'

# Path to directory containing the MP4 files
DIRECTORY = 'video/upload'

# Mux API URLs
CREATE_ASSET_URL = 'https://api.mux.com/video/v1/uploads'
LIST_ASSETS_URL = 'https://api.mux.com/video/v1/assets'

# Function to create an asset in Mux
def create_asset(file_name):
    response = requests.post(
        CREATE_ASSET_URL,
        auth=(ACCESS_TOKEN, SECRET_KEY),
        json={
            'input': file_name,
            'playback_policy': ['public'],
            'mp4_support': 'standard'
        }
    )
    return response.json()

# Function to get the asset details from Mux
def get_asset_details(asset_id):
    time.sleep(10)  # Wait for a few seconds before checking the asset details
    response = requests.get(
        f"{LIST_ASSETS_URL}{asset_id}",
        auth=(ACCESS_TOKEN, SECRET_KEY)
    )
    return response.json()
    
def upload_video_to_mux(file_path, upload_url):
    with open(file_path, 'rb') as file:
        response = requests.put(upload_url, data=file)
        return response.status_code == 200

# Modify the upload_files function
def upload_files():
    for file_name in os.listdir(DIRECTORY):
        if file_name.endswith('.mp4'):
            print(f'Uploading {file_name}...')
            file_path = os.path.join(DIRECTORY, file_name)
            asset_response = create_asset(file_path)

            # Extract upload URL and asset ID
            upload_url = asset_response.get('data', {}).get('url')
            asset_id = asset_response.get('data', {}).get('id')

            if upload_url and asset_id:
                # Upload the video file to Mux
                if upload_video_to_mux(file_path, upload_url):
                    print(f'File {file_name} uploaded successfully.')
                else:
                    print(f'Failed to upload file {file_name}.')
            else:
                print(f'Failed to create asset for file {file_name}.')



if __name__ == '__main__':
    upload_files()

