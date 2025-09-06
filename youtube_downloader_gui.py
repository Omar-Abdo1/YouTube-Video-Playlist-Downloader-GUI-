import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import threading
import os
import yt_dlp
import subprocess
import sys

class YouTubeDownloaderGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Video & Playlist Downloader")
        self.root.geometry("600x500")
        self.root.resizable(True, True)
        
        # FFmpeg path variable
        self.ffmpeg_path_var = tk.StringVar(value="ffmpeg")  # Default to system ffmpeg
        
        # Configure style
        style = ttk.Style()
        style.configure('TFrame', background='#f0f0f0')
        style.configure('TLabel', background='#f0f0f0', font=('Arial', 10))
        style.configure('TButton', font=('Arial', 10))
        style.configure('Header.TLabel', font=('Arial', 14, 'bold'))
        
        # Check FFmpeg
        self.ffmpeg_available = self.check_ffmpeg(self.ffmpeg_path_var.get())
        
        self.create_widgets()
        
    def check_ffmpeg(self, ffmpeg_path):
        """Check if FFmpeg is available at the given path"""
        try:
            subprocess.run([ffmpeg_path, '-version'], capture_output=True, check=True)
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            return False

    def create_widgets(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Header
        header = ttk.Label(main_frame, text="YouTube Video & Playlist Downloader", style='Header.TLabel')
        header.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # URL input
        url_label = ttk.Label(main_frame, text="YouTube URL:")
        url_label.grid(row=1, column=0, sticky=tk.W, pady=(0, 5))
        
        self.url_var = tk.StringVar()
        url_entry = ttk.Entry(main_frame, textvariable=self.url_var, width=60)
        url_entry.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 15))
        
        # Auto-detect type
        detect_btn = ttk.Button(main_frame, text="Auto-Detect Type", command=self.auto_detect_type)
        detect_btn.grid(row=3, column=0, sticky=tk.W, pady=(0, 15))
        
        # Download type
        type_frame = ttk.Frame(main_frame)
        type_frame.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        type_label = ttk.Label(type_frame, text="Download Type:")
        type_label.grid(row=0, column=0, sticky=tk.W)
        
        self.download_type = tk.StringVar(value="auto")
        type_auto = ttk.Radiobutton(type_frame, text="Auto-Detect", variable=self.download_type, value="auto")
        type_auto.grid(row=0, column=1, sticky=tk.W, padx=(10, 0))
        
        type_video = ttk.Radiobutton(type_frame, text="Single Video", variable=self.download_type, value="video")
        type_video.grid(row=0, column=2, sticky=tk.W, padx=(10, 0))
        
        type_playlist = ttk.Radiobutton(type_frame, text="Playlist", variable=self.download_type, value="playlist")
        type_playlist.grid(row=0, column=3, sticky=tk.W, padx=(10, 0))
        
        # Quality selection
        quality_label = ttk.Label(main_frame, text="Quality:")
        quality_label.grid(row=5, column=0, sticky=tk.W, pady=(0, 5))
        
        self.quality_var = tk.StringVar(value="720p")
        quality_combo = ttk.Combobox(main_frame, textvariable=self.quality_var, 
                                    values=["Best", "1440p", "1080p", "720p", "480p", "360p", "Audio only"], 
                                    state="readonly", width=15)
        quality_combo.grid(row=6, column=0, sticky=tk.W, pady=(0, 15))
        
        # FFmpeg status
        ffmpeg_status = "Available" if self.ffmpeg_available else "Not Found - Some features limited"
        ffmpeg_color = "green" if self.ffmpeg_available else "red"
        ffmpeg_label = ttk.Label(main_frame, text=f"FFmpeg: {ffmpeg_status}", foreground=ffmpeg_color)
        ffmpeg_label.grid(row=6, column=1, sticky=tk.E, pady=(0, 15))
        
        # Folder selection
        folder_label = ttk.Label(main_frame, text="Download Folder:")
        folder_label.grid(row=7, column=0, sticky=tk.W, pady=(0, 5))
        
        self.folder_var = tk.StringVar(value=os.path.expanduser("~/Downloads"))
        folder_entry = ttk.Entry(main_frame, textvariable=self.folder_var, width=40)
        folder_entry.grid(row=8, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        
        browse_btn = ttk.Button(main_frame, text="Browse", command=self.browse_folder)
        browse_btn.grid(row=8, column=1, sticky=tk.W, padx=(5, 0), pady=(0, 10))
        
        # Progress bar
        self.progress_var = tk.DoubleVar()
        progress_bar = ttk.Progressbar(main_frame, variable=self.progress_var, maximum=100)
        progress_bar.grid(row=9, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(10, 5))
        
        # Status label
        self.status_var = tk.StringVar(value="Ready to download")
        status_label = ttk.Label(main_frame, textvariable=self.status_var)
        status_label.grid(row=10, column=0, columnspan=2, pady=(0, 5))
        
        # Type indicator
        self.type_indicator_var = tk.StringVar(value="Type: Not determined")
        type_indicator = ttk.Label(main_frame, textvariable=self.type_indicator_var, foreground="blue")
        type_indicator.grid(row=11, column=0, columnspan=2, pady=(0, 10))
        
        # Log area
        log_label = ttk.Label(main_frame, text="Download Log:")
        log_label.grid(row=12, column=0, sticky=tk.W, pady=(0, 5))
        
        self.log_text = scrolledtext.ScrolledText(main_frame, height=8, width=70)
        self.log_text.grid(row=13, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 15))
        self.log_text.config(state=tk.DISABLED)
        
        # Download button
        download_btn = ttk.Button(main_frame, text="Start Download", command=self.start_download)
        download_btn.grid(row=14, column=0, columnspan=2, pady=(0, 10))
        
        # FFmpeg path selection
        ffmpeg_path_label = ttk.Label(main_frame, text="FFmpeg Location (ffmpeg.exe):")
        ffmpeg_path_label.grid(row=15, column=0, sticky=tk.W, pady=(0, 5))
        
        ffmpeg_path_entry = ttk.Entry(main_frame, textvariable=self.ffmpeg_path_var, width=40)
        ffmpeg_path_entry.grid(row=16, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        
        ffmpeg_browse_btn = ttk.Button(main_frame, text="Browse", command=self.browse_ffmpeg)
        ffmpeg_browse_btn.grid(row=16, column=1, sticky=tk.W, padx=(5, 0), pady=(0, 10))
        
        # FFmpeg status
        self.ffmpeg_status_label = ttk.Label(main_frame, text="", foreground="green")
        self.ffmpeg_status_label.grid(row=17, column=0, columnspan=2, sticky=tk.W, pady=(0, 10))
        self.update_ffmpeg_status()
        
        # Configure grid weights
        main_frame.columnconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        
    def log_message(self, message):
        """Add a message to the log area"""
        self.log_text.config(state=tk.NORMAL)
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)
        self.log_text.config(state=tk.DISABLED)
        
    def browse_folder(self):
        folder = filedialog.askdirectory(initialdir=self.folder_var.get())
        if folder:
            self.folder_var.set(folder)
            
    def browse_ffmpeg(self):
        ffmpeg_path = filedialog.askopenfilename(title="Select ffmpeg.exe", filetypes=[("ffmpeg.exe", "*.exe")])
        if ffmpeg_path:
            self.ffmpeg_path_var.set(ffmpeg_path)
            self.ffmpeg_available = self.check_ffmpeg(ffmpeg_path)
            self.update_ffmpeg_status()

    def update_ffmpeg_status(self):
        ffmpeg_status = "Available" if self.ffmpeg_available else "Not Found - Some features limited"
        ffmpeg_color = "green" if self.ffmpeg_available else "red"
        self.ffmpeg_status_label.config(text=f"FFmpeg: {ffmpeg_status}", foreground=ffmpeg_color)

    def auto_detect_type(self):
        url = self.url_var.get().strip()
        if not url:
            messagebox.showinfo("Info", "Please enter a YouTube URL first")
            return
            
        if "list=" in url and ("watch?" in url or "playlist?" in url):
            self.download_type.set("playlist")
            self.type_indicator_var.set("Type: Playlist detected")
            self.log_message("Auto-detected: Playlist")
        else:
            self.download_type.set("video")
            self.type_indicator_var.set("Type: Single video detected")
            self.log_message("Auto-detected: Single video")
            
    def start_download(self):
        url = self.url_var.get().strip()
        if not url:
            messagebox.showerror("Error", "Please enter a YouTube URL")
            return
            
        folder = self.folder_var.get()
        if not os.path.exists(folder):
            try:
                os.makedirs(folder)
            except:
                messagebox.showerror("Error", "Cannot create download folder")
                return
                
        # Clear log
        self.log_text.config(state=tk.NORMAL)
        self.log_text.delete(1.0, tk.END)
        self.log_text.config(state=tk.DISABLED)
        
        # Check FFmpeg availability
        self.ffmpeg_available = self.check_ffmpeg(self.ffmpeg_path_var.get())
        self.update_ffmpeg_status()
        
        # Start download in a separate thread to avoid freezing the GUI
        thread = threading.Thread(target=self.download, args=(url, folder))
        thread.daemon = True
        thread.start()
        
    def download(self, url, folder):
        try:
            self.status_var.set("Preparing download...")
            self.log_message("Starting download process...")
            
            # Determine download type
            dl_type = self.download_type.get()
            if dl_type == "auto":
                if "list=" in url and ("watch?" in url or "playlist?" in url):
                    dl_type = "playlist"
                else:
                    dl_type = "video"
            
            self.log_message(f"Download type: {dl_type}")
            
            # Map quality selection to yt-dlp format
            quality_map = {
                "Best": "bestvideo+bestaudio/best",
                "1440p": "bestvideo[height<=1440]+bestaudio/best",
                "1080p": "bestvideo[height<=1080]+bestaudio/best",
                "720p": "bestvideo[height<=720]+bestaudio/best",
                "480p": "best[height<=480]",
                "360p": "best[height<=360]",
                "Audio only": "bestaudio/best"
            }
            
            format_selection = quality_map.get(self.quality_var.get(), "bestvideo+bestaudio/best")
            
            # Prepare yt-dlp options
            ffmpeg_path = self.ffmpeg_path_var.get()
            ydl_opts = {
                'outtmpl': os.path.join(folder, '%(title)s.%(ext)s'),
                'format': format_selection,
                'progress_hooks': [self.progress_hook],
                'quiet': True,
                'no_warnings': False,
                'ffmpeg_location': ffmpeg_path,  # Pass user FFmpeg path to yt-dlp
            }
            
            # Add merge options if FFmpeg is available and not audio only
            if self.ffmpeg_available and self.quality_var.get() != "Audio only":
                ydl_opts['merge_output_format'] = 'mp4'
                self.log_message("FFmpeg available - will merge video and audio streams")
            else:
                self.log_message("FFmpeg not available - using pre-merged formats")
                # Fall back to formats that don't require merging
                if self.quality_var.get() == "Best":
                    format_selection = "best[ext=mp4]"
                elif self.quality_var.get() == "1440p":
                    format_selection = "best[height<=1440][ext=mp4]"
                elif self.quality_var.get() == "1080p":
                    format_selection = "best[height<=1080][ext=mp4]"
                elif self.quality_var.get() == "720p":
                    format_selection = "best[height<=720][ext=mp4]"
                elif self.quality_var.get() == "480p":
                    format_selection = "best[height<=480][ext=mp4]"
                elif self.quality_var.get() == "360p":
                    format_selection = "best[height<=360][ext=mp4]"
                
                ydl_opts['format'] = format_selection
            
            # Set output template based on type
            if dl_type == "playlist":
                ydl_opts['outtmpl'] = os.path.join(folder, '%(playlist_title)s', '%(title)s.%(ext)s')
                self.log_message("Downloading as playlist")
            else:
                # For single videos, remove playlist parameters
                if "&list=" in url:
                    url = url.split("&list=")[0]
                if "&index=" in url:
                    url = url.split("&index=")[0]
                ydl_opts['noplaylist'] = True
                self.log_message("Downloading as single video")
                
            if self.quality_var.get() == "Audio only":
                ydl_opts.update({
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }]
                })
                self.log_message("Downloading audio only (MP3)")
            
            self.status_var.set("Downloading...")
            self.log_message(f"Downloading from: {url}")
            self.log_message(f"Saving to: {folder}")
            self.log_message(f"Quality: {self.quality_var.get()}")
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                title = info.get('title', 'Unknown')
                
                if dl_type == "playlist":
                    count = len(info.get('entries', []))
                    self.log_message(f"Playlist: {title} with {count} videos")
                else:
                    self.log_message(f"Video: {title}")
                
                ydl.download([url])
                
            self.status_var.set("Download completed!")
            self.log_message("Download completed successfully!")
            messagebox.showinfo("Success", "Download completed successfully!")
            self.progress_var.set(0)
            
        except Exception as e:
            error_msg = f"Error: {str(e)}"
            self.status_var.set(error_msg)
            self.log_message(f"ERROR: {str(e)}")
            messagebox.showerror("Error", f"Download failed: {str(e)}")
            self.progress_var.set(0)
            
    def progress_hook(self, d):
        if d['status'] == 'downloading':
            # Update progress bar
            if 'total_bytes' in d and d['total_bytes'] > 0:
                percent = d['downloaded_bytes'] / d['total_bytes'] * 100
                self.progress_var.set(percent)
                self.status_var.set(f"Downloading: {percent:.1f}%")
                
                # Update log with progress
                filename = os.path.basename(d.get('filename', 'Unknown'))
                self.log_message(f"Progress: {filename} - {percent:.1f}%")
        elif d['status'] == 'finished':
            self.progress_var.set(100)
            self.status_var.set("Finalizing download...")
            self.log_message("Finalizing download...")

if __name__ == "__main__":
    root = tk.Tk()
    app = YouTubeDownloaderGUI(root)
    root.mainloop()
