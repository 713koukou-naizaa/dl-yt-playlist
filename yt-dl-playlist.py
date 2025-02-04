"""
This script uses the Youtube Data API v3 and pytubefix's Youtube class to download all the videos of a Youtube playlist as audio files.

Author: 713koukou-naizaa
Date: 2025-02-04
Contact: nzo.akt@gmail.com
"""

from dotenv import load_dotenv
import requests
import os
from pytubefix import YouTube

load_dotenv()

API_KEY = os.getenv('API_KEY')
API_BASE_URL = os.getenv('API_BASE_URL')
PLAYLIST_ID = os.getenv('PLAYLIST_ID')
BASE_VIDEO_URL = os.getenv('BASE_VIDEO_URL')
DOWNLOAD_DIR = os.getenv('DOWNLOAD_DIR')

def download_videos(videos_urls, download_path):
    """
    Downloads the videos from the given list of video urls into the specified download directory

    Parameters
    ----------
    videos_urls : list
        list of video urls to download
    download_path : str
        path to the directory where the videos should be downloaded
    """
    for index, video_url in enumerate(videos_urls):
        try:
            yt = YouTube(video_url, 'WEB')
            stream = yt.streams.filter(only_audio=True).first()
            stream.download(output_path=download_path)
            print(f"{index + 1}: Downloaded: {video_url}")
        except Exception as e:
            print(f"{index + 1}: Error downloading {video_url}: {e}")

url = f"{API_BASE_URL}/playlistItems?part=snippet&playlistId={PLAYLIST_ID}&key={API_KEY}&maxResults=50"

response = requests.get(url)

videos_url = []

if response.status_code == 200:
    data = response.json()
    for item in data['items']:
        videos_url.append(f"{BASE_VIDEO_URL}{item['snippet']['resourceId']['videoId']}")
else:
    print(f"Error: {response.status_code}")

download_videos(videos_url, DOWNLOAD_DIR)
