import os
import requests
import time

# Mux API credentials
ACCESS_TOKEN = 'YOUR_MUX_ACCESS_TOKEN'
SECRET_KEY = 'YOUR_MUX_SECRET_KEY'

# Path to directory containing the MP4 files
DIRECTORY = 'video/upload'

# Mux API URLs
LIST_ASSETS_URL = 'https://api.mux.com/video/v1/assets'
CREATE_PLAYBACK_ID_URL = 'https://api.mux.com/video/v1/assets/{asset_id}/playback-ids'

# Function to list all assets
def list_all_assets():
    response = requests.get(LIST_ASSETS_URL, auth=(ACCESS_TOKEN, SECRET_KEY))
    if response.status_code == 200:
        return response.json().get('data', [])
    else:
        print(f"Failed to list assets: {response.text}")
        return []

# Function to create a public playback ID for an asset
def create_public_playback_id(asset_id):
    data = {
        "policy": "public"
    }
    response = requests.post(
        CREATE_PLAYBACK_ID_URL.format(asset_id=asset_id),
        json=data,
        auth=(ACCESS_TOKEN, SECRET_KEY)
    )
    if response.status_code == 201:
        print(f"Public playback ID created for asset {asset_id}")
    else:
        print(f"Failed to create playback ID for asset {asset_id}: {response.text}")

def main():
    assets = list_all_assets()
    for asset in assets:
        create_public_playback_id(asset['id'])

if __name__ == '__main__':
    main()