<p align="center">
  <img width="500" height="480" alt="Screenshot 2025-11-09 at 14 19 33" src="https://github.com/user-attachments/assets/7422b1dd-896c-4746-bb51-918fcf8142bf" />
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

Run the app:
``` bash
$ python3 main.py
```

## Example Usage

You can also use the core `download_video()` function directly in your Python code:
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

```
youtube-video-downloader/
├── downloader/
│   ├── video_downloader.py           # Handles video download logic using yt-dlp
│   ├── audio_downloader.py           # Handles audio (MP3) download logic
│   └── playlist_downloader.py        # Manages playlist downloads (videos or audios)
├── ui/
│   ├── gui_tkinter.py                # Main CustomTkinter GUI interface
│   └── texts.py                      # Multi-language UI text strings
├── utils/
│   ├── helpers.py                    # Utility functions (timestamp, folder check)
│   └── logger.py                     # Logging configuration and helper methods
├── main.py                           # Application entry point that runs the GUI
├── README.md                         # Project documentation and setup guide
├── requirements.txt                  # Python dependencies list
└── LICENSE                           # MIT License for open-source usage
```

## License

This project is licensed under the MIT License.
