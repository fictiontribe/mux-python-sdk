import requests

# Mux API credentials
ACCESS_TOKEN = 'YOUR_MUX_ACCESS_TOKEN'
SECRET_KEY = 'YOUR_MUX_SECRET_KEY'

# Mux API URL
LIST_ASSETS_URL = 'https://api.mux.com/video/v1/assets'
UPDATE_MP4_SUPPORT_URL = 'https://api.mux.com/video/v1/assets/{asset_id}/mp4-support'

# Function to list all assets
def list_all_assets():
    response = requests.get(LIST_ASSETS_URL, auth=(ACCESS_TOKEN, SECRET_KEY))
    if response.status_code == 200:
        return response.json().get('data', [])
    else:
        print(f"Failed to list assets: {response.text}")
        return []

# Function to update MP4 support for an asset
def update_mp4_support(asset_id):
    data = {"mp4_support": "standard"}
    response = requests.put(
        UPDATE_MP4_SUPPORT_URL.format(asset_id=asset_id),
        json=data,
        auth=(ACCESS_TOKEN, SECRET_KEY)
    )
    if response.status_code == 200:
        print(f"MP4 support updated for asset {asset_id}")
    else:
        print(f"Failed to update MP4 support for asset {asset_id}: {response.text}")

def main():
    assets = list_all_assets()
    for asset in assets:
        update_mp4_support(asset['id'])

if __name__ == '__main__':
    main()
