import yt_dlp
import os
import time

def download_video(url, path, resolution="720p", progress_callback=None):
    if resolution == "360p":
        fmt = "bestvideo[height<=360]+bestaudio/best[height<=360]/best[height<=360]"
    elif resolution == "720p":
        fmt = "bestvideo[height<=720]+bestaudio/best[height<=720]/best[height<=720]"
    elif resolution == "1080p":
        fmt = "bestvideo[height<=1080]+bestaudio/best[height<=1080]/best[height<=1080]"
    else:
        fmt = "bestvideo+bestaudio/best"

    ydl_opts = {
        "format": fmt,
        "outtmpl": os.path.join(path, "%(title)s.%(ext)s"),
        "noplaylist": True,
        "quiet": True,
        "progress_hooks": [lambda d: _progress_hook(d, progress_callback)]
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def _progress_hook(d, progress_callback):
    if d["status"] == "downloading" and progress_callback:
        total = d.get("total_bytes") or d.get("total_bytes_estimate")
        downloaded = d.get("downloaded_bytes", 0)
        percent = (downloaded / total * 100) if total else 0
        progress_callback(percent, downloaded_bytes=downloaded, total_bytes=total)