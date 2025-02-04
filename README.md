# dl-yt-playlist

This script uses the YouTube Data API v3 and `pytubefix`'s `YouTube` class to download all the videos of a YouTube playlist as audio files.

## Author

- **713koukou-naizaa**
- **Date**: 2025-02-04
- **Contact**: nzo.akt@gmail.com

## Prerequisites

- Python 3.x
- `pytubefix` library
- `requests` library
- `python-dotenv` library

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/713koukou-naizaa/dl-yt-playlist.git
    cd dl-yt-playlist
    ```

2. Install the required libraries:
    ```bash
    pip install pytubefix requests python-dotenv
    ```

3. Create a .env file in the root directory of the project and add the following environment variables:
    ```properties
    API_KEY="your_api_key_here"
    API_BASE_URL="https://www.googleapis.com/youtube/v3"
    PLAYLIST_ID="your_playlist_id_here"
    BASE_VIDEO_URL="https://www.youtube.com/watch?v="
    DOWNLOAD_DIR="path_to_your_download_directory"
    ```

## Usage

1. Ensure that the .env file is correctly configured with your API key, playlist ID, and other necessary information.

2. Run the script:
    ```bash
    python yt-dl-playlist.py
    ```

3. The script will download all the videos from the specified YouTube playlist as audio files into the specified download directory.

## Script Explanation

- The script loads environment variables from the .env file using load_dotenv.
- It retrieves the playlist items from the YouTube Data API.
- It iterates through the video URLs and downloads the audio streams using pytubefix.

## Error Handling

- The script handles errors during the download process and prints appropriate error messages.