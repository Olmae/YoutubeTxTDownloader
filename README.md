# YoutubeTxTDownloader

**Description:**

YoutubeTxTDownloader is a Python script that allows you to download videos from YouTube by searching for song titles provided in a text file (`songs.txt`). The script uses `yt-dlp` to search and download videos with a specific "karaoke" keyword, saving them in a designated folder. It supports both downloading the best available video and organizing the downloads by preventing duplicates. The downloaded videos are saved in the folder named `Playlist` located within the same directory as the script, and detailed information about the downloaded songs (title and URL) is logged in a file called `downloaded_songs.txt`.

**Features:**
- Downloads videos from YouTube based on song titles in a text file.
- Adds "karaoke" to the search query for karaoke versions of songs.
- Saves videos in the `Playlist` folder.
- Prevents duplicate downloads by checking already downloaded titles.
- Logs the original song title, downloaded video title, and URL to a text file.
  
**Requirements:**
1. **Python 3.7+**: Ensure that Python is installed on your machine.
2. **yt-dlp**: This library is used to interact with YouTube and handle video downloading. Install it using:
   ```bash
   pip install yt-dlp
   ```
3. **FFmpeg**: Required for post-processing downloaded media. Download and extract [FFmpeg](https://ffmpeg.org/download.html) into the project folder. Ensure that the path to the FFmpeg binary is correctly set in the script.
   
**Setup Instructions:**
1. Place `ffmpeg` binaries in a folder named `ffmpeg-7.0-full_build/bin` within the project directory.
2. Prepare a `songs.txt` file, where each line contains a song title or a keyword you want to search.
3. Run the script, and it will:
   - Search YouTube for karaoke videos based on the titles in `songs.txt`.
   - Download the videos and save them in the `Playlist` folder.
   - Log the results in `downloaded_songs.txt`.

