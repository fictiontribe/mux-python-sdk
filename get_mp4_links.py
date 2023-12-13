import os
import time
import requests

# Mux API credentials
ACCESS_TOKEN = 'YOUR_MUX_ACCESS_TOKEN'
SECRET_KEY = 'YOUR_MUX_SECRET_KEY'

# Mux API URLs
LIST_ASSETS_URL = 'https://api.mux.com/video/v1/assets'

# Function to list all assets
def list_all_assets():
    response = requests.get(LIST_ASSETS_URL, auth=(ACCESS_TOKEN, SECRET_KEY))
    if response.status_code == 200:
        return response.json().get('data', [])
    else:
        print(f"Failed to list assets: {response.text}")
        return []

# Function to get MP4 links for an asset
def get_mp4_links(asset):
    asset_id = asset['id']
    playback_id = asset['playback_ids'][0]['id'] if asset['playback_ids'] else None
    static_renditions = asset.get('static_renditions', {}).get('status')

    if playback_id and static_renditions == 'ready':
        print(f"Asset ID: {asset_id}")
        for quality in ['low', 'medium', 'high']:
            print(playback_id)
            print(f"Link ({quality.capitalize()}): https://stream.mux.com/{playback_id}/{quality}.mp4")
    else:
        print(f"No MP4 links available for asset ID: {asset_id}")

def main():
    assets = list_all_assets()
    for asset in assets:
        get_mp4_links(asset)

if __name__ == '__main__':
    main()
