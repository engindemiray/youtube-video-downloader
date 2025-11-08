import yt_dlp
import os
import time

def download_audio(url, path, progress_callback=None):
    ydl_opts = {
        "format": "bestaudio/best",
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