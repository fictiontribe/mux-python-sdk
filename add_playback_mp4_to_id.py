import requests

# Mux API credentials
ACCESS_TOKEN = 'YOUR_MUX_ACCESS_TOKEN'
SECRET_KEY = 'YOUR_MUX_SECRET_KEY'

# Specific asset ID to update
ASSET_ID = 'VIDEO_ID'

# Mux API URLs
CREATE_PLAYBACK_ID_URL = 'https://api.mux.com/video/v1/assets/{asset_id}/playback-ids'
UPDATE_MP4_SUPPORT_URL = 'https://api.mux.com/video/v1/assets/{asset_id}/mp4-support'

# Function to create a public playback ID for an asset
def create_public_playback_id(asset_id):
    data = {"policy": "public"}
    response = requests.post(
        CREATE_PLAYBACK_ID_URL.format(asset_id=asset_id),
        json=data,
        auth=(ACCESS_TOKEN, SECRET_KEY)
    )
    if response.status_code == 201:
        print(f"Public playback ID created for asset {asset_id}")
    else:
        print(f"Failed to create playback ID for asset {asset_id}: {response.text}")

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
    create_public_playback_id(ASSET_ID)
    update_mp4_support(ASSET_ID)

if __name__ == '__main__':
    main()