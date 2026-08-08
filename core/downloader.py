import os
import threading
import yt_dlp


DOWNLOAD_FOLDER = "downloads"


def download_media(url, media_type, start="", end="", progress_callback=None):

    os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

    output = os.path.join(
        DOWNLOAD_FOLDER,
        "%(title)s.%(ext)s"
    )

    def progress_hook(data):

        if data["status"] == "downloading":

            downloaded = data.get("downloaded_bytes", 0)
            total = data.get("total_bytes") or data.get("total_bytes_estimate")

            if total:
                percent = (downloaded / total) * 100

                if progress_callback:
                    progress_callback(percent, "Downloading...")

        elif data["status"] == "finished":

            if progress_callback:
                progress_callback(100, "Processing...")

    ydl_options = {
        "outtmpl": output,
        "progress_hooks": [progress_hook],
        "noplaylist": True,
    }

    # ===========================
    # AUDIO
    # ===========================

    if media_type == "audio":

        ydl_options.update({
            "format": "bestaudio/best",
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
        })

    # ===========================
    # VIDEO
    # ===========================

    else:

        ydl_options.update({
            "format": "bestvideo+bestaudio/best",
            "merge_output_format": "mp4",
        })

    # ===========================
    # TIME CLIPPING
    # ===========================

    if start and end:

        ydl_options["download_sections"] = [
            f"*{start}-{end}"
        ]

        ydl_options["force_keyframes_at_cuts"] = True

    # ===========================
    # DOWNLOAD
    # ===========================

    try:

        with yt_dlp.YoutubeDL(ydl_options) as ydl:

            ydl.download([url])

        if progress_callback:
            progress_callback(100, "Download complete!")

    except Exception as e:

        if progress_callback:
            progress_callback(0, f"Error: {str(e)}")

        print("Download error:", e)