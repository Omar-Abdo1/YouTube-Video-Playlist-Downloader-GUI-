<h1 align="center">YouTube Video & Playlist Downloader (GUI)</h1>
<h3 align="center">A powerful Python-based graphical tool for downloading YouTube videos and playlists with customizable quality options.</h3>
<h3 align="center">Automatically merges video and audio for high-quality downloads using FFmpeg.</h3>
<p align="center">
  <img src="https://img.shields.io/badge/Python-3.6%2B-blue?style=for-the-badge&logo=python" alt="Python Version">
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey?style=for-the-badge" alt="Platform">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License">
</p>

---

## 🚀 Features

- **Intuitive GUI:** No command line required—just paste a URL and click!
- **Download Entire Playlists:** Organizes videos into playlist folders.
- **Download Single Videos:** Works even with playlist URLs containing `&list=` parameters.
- **Multiple Quality Options:** Choose from 360p to 4K, or audio-only.
- **Automatic Merging:** FFmpeg integration for perfect video+audio synchronization.
- **Progress Tracking:** Real-time progress bar and log display.
- **Error Handling:** Continues downloads even if some videos fail.
- **Cross-Platform:** Works on Windows, macOS, and Linux.

---

## 📋 Prerequisites

- **Python 3.6 or higher** ([Download Python](https://www.python.org/downloads/))
- **yt-dlp** ([yt-dlp GitHub](https://github.com/yt-dlp/yt-dlp))
- **FFmpeg** ([Download FFmpeg](https://www.gyan.dev/ffmpeg/builds/))  
  FFmpeg is a free, open-source tool for processing video and audio files.  
  It is required for merging high-quality video and audio streams, and for converting audio to MP3.

### FFmpeg Installation Details

1. Go to [FFmpeg Windows builds](https://www.gyan.dev/ffmpeg/builds/).
2. Download the "release full" zip file.
3. Extract the zip file to a folder, for example: `C:\ffmpeg\`.
4. Inside `C:\ffmpeg\`, find the `bin` folder. The file `ffmpeg.exe` is inside.
5. You can set the location of `ffmpeg.exe` directly in the GUI (no need to add to PATH).
6. If you want FFmpeg available everywhere, add `C:\ffmpeg\bin` to your Windows PATH:
   - Search for "Environment Variables" in Windows.
   - Edit the "Path" variable and add `C:\ffmpeg\bin`.
   - Click OK and restart your computer.

---

## 🔧 Installation

### For Users With No GitHub or Command Line Experience

1. **Download the program files**  
   - Ask the author for a ZIP file, or download from the "Code" button on GitHub (choose "Download ZIP").
   - Extract the ZIP file to a folder (e.g., `C:\YouTubeDownloaderGUI`).

2. **Install Python**  
   - Download Python from [python.org](https://www.python.org/downloads/).
   - Run the installer and check "Add Python to PATH" during installation.

3. **Install yt-dlp**  
   - Open the folder where you extracted the program.
   - Double-click the file named `install_dependencies.bat` (if provided), or:
   - Open a terminal in that folder and run:
     ```
     pip install yt-dlp
     ```
   - If you see "pip not found", reinstall Python and make sure "Add to PATH" is checked.

4. **Install FFmpeg**  
   - Follow the FFmpeg instructions above.

5. **Run the Program**  
   - Double-click `youtube_downloader_gui.py` (if Python is installed correctly).
   - Or right-click the file and choose "Open with > Python".

---

## 🎯 Usage

1. **Paste your YouTube video or playlist URL.**
2. Click "Auto-Detect Type" or manually select "Single Video" or "Playlist".
3. Choose your desired quality.
4. Select the download folder.
5. (Optional) Set the FFmpeg executable location if not in PATH.
6. Click "Start Download".
7. Monitor progress and logs in the GUI.

---

## ⚙️ Quality Options

- **Best available (4K/1440p/1080p)**
- **1440p QHD**
- **1080p Full HD**
- **720p HD**
- **480p**
- **360p**
- **Audio only (MP3, 192kbps)**

---

## 📁 Output Structure

```
Your-Download-Folder/
├── Playlist Name/
│   ├── Video Title 1.mp4
│   ├── Video Title 2.mp4
│   └── ...
└── Single Video Title.mp4
```
- **Playlists:** Saved in folders named after the playlist.
- **Single Videos:** Saved directly in the chosen folder.
- **Audio Only:** Saved as `.mp3`.

---

## 🔍 Troubleshooting

- **FFmpeg not found:** Set the correct path in the GUI or add to system PATH.
- **yt-dlp errors:** Update yt-dlp: `pip install --upgrade yt-dlp`
- **Module not found:** Install requirements: `pip install yt-dlp`
- **Other issues:** Check the log area in the GUI for error messages.

---

## ⚠️ Legal Disclaimer

This tool is intended for personal use only.  
Please respect copyright laws and YouTube's Terms of Service.

---

## 🤝 Contributing

Contributions are welcome!  
Feel free to report issues, suggest features, or submit pull requests.

---

## 📄 License

This project is licensed under the MIT License.

---

**Happy Downloading! 🎬**
