# MUX Batch Uploader / Python Toolset

![MUX Batch Uploader / Python Toolset Banner](https://github.com/fictiontribe/mux-python-sdk/blob/main/mux.jpg?raw=true)

The **MUX Batch Uploader / Python Toolset** is an open-source collection of Python scripts developed at [Fiction Tribe](https://fictiontribe.com) designed to streamline video processing workflows with [Mux.com](https://mux.com), the internet's video infrastructure service. This toolset simplifies batch operations such as video uploads, adding public playback, retrieving MP4 links, updating MP4 support, and enabling playback MP4 for specific video IDs on the Mux platform.

## Installation

To get started with this Python toolset:

1. Clone or download this toolset to your local machine.
2. Ensure Python 3.x is installed on your system.

## Features

This toolset includes a suite of scripts that provide robust functionality for video asset management:

### `upload.py`

This script automates the bulk upload of video files from a local directory to your Mux account, streamlining the process of content delivery.

```python
python upload.py
```

Set the path to the directory containing MP4 files in the script:

```python
# Path to directory containing the MP4 files
DIRECTORY = 'path/to/video/directory'
```

### `add_public_playback.py`

Expands your videos' reach by enabling public playback capability, making them readily accessible for streaming.

```python
python add_public_playback.py
```

### `get_mp4_links.py`

Retrieves MP4 links for each video asset, offering you direct access to various resolutions and quality levels for download or playback.

```python
python get_mp4_links.py
```

### `update_mp4_support.py`

Ensures your videos are optimized for all viewing platforms by updating MP4 support across your Mux video assets.

```python
python update_mp4_support.py
```

### `add_playback_mp4_to_id.py`

Tailors video playback options by adding MP4 playback support to individual videos, allowing for greater control over your content.

```python
python add_playback_mp4_to_id.py
```

Set the specific asset ID in the script:

```python
# Specific asset ID to update
ASSET_ID = 'your_mux_video_id'
```

## Credentials

Securely set your Mux credentials in each script:

```python
# Mux API credentials
ACCESS_TOKEN = 'your_access_token'
SECRET_KEY = 'your_secret_key'
```

Replace `'your_access_token'` and `'your_secret_key'` with the credentials provided by Mux.

## Contributing

We welcome contributions from the developer community. Before submitting new features or scripts, please ensure compatibility with the existing codebase and comprehensive testing.

## License

[MIT License](link-to-license)

---

For more information on Mux's services and how you can leverage them for your video infrastructure needs, visit [Mux.com](https://mux.com).
