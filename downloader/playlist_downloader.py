import yt_dlp
import os
from downloader import video_downloader, audio_downloader

def download_playlist(url, path, mode="Video", resolution="720p", progress_callback=None):
    """
    YouTube playlist downloader
    
    Args:
        url (str): Playlist URL
        path (str): Folder to save downloaded files
        mode (str): "Video" or "Audio" download mode
        resolution (str): Desired video resolution
        progress_callback (func): Callback function to update progress, speed and ETA
    """

    # Extract playlist info only (no download yet)
    ydl_opts = {
        "quiet": True,
        "extract_flat": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        entries = info.get("entries", [])

        for entry in entries:
            video_url = f"https://www.youtube.com/watch?v={entry['id']}"
            if mode == "Video":
                video_downloader.download_video(video_url, path, resolution, progress_callback)
            else:
                audio_downloader.download_audio(video_url, path, progress_callback)