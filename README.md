<p align="center">
  <img src="Screenshot 2025-11-09 at 14 19 33" src="https://github.com/user-attachments/assets/12ef387c-67df-458b-80c7-40ba63af6dc3"" width="500" height="531">
</p>

## Tech Stack

- Python
- Tkinter / CustomTkinter
- yt-dlp

## Installation

Clone the repository:
``` bash
$ git clone https://github.com/engindemiray/youtube-video-downloader.git
cd youtube-video-downloader
```

Install required packages:
``` bash
$ pip3 install -r requirements.txt
```

Run the app with this command:
``` bash
$ python3 main.py
```

## Example Usage

```python
from downloader.video_downloader import download_video

def progress(percent, downloaded_bytes=None, total_bytes=None):
    print(f"{percent}%")

download_video(
    "https://www.youtube.com/watch?v=XXXXXX",
    path="./downloads",
    resolution="720p",
    progress_callback=progress
)
```

## Project Structure

youtube-video-downloader/
├─ downloader/
│  ├─ __pycache__.py
│  ├─ video_downloader.py
│  ├─ audio_downloader.py
│  └─ playlist_downloader.py
├─ ui/
│  ├─ __pycache__.py
│  ├─ gui_tkinter.py
│  └─ texts.py
├─ utils/
│  ├─ helpers.py
│  └─ logger.py
├─ main.py
├─ README.md
└─ requirements.txt

## License

This project is licensed under the MIT License.
