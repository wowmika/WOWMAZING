import os
from collections.abc import Callable

import yt_dlp


DOWNLOAD_FOLDER = "downloads"
ProgressCallback = Callable[[float, str], None]


class DownloadCancelled(Exception):
    """Raised when a queued download is cancelled by the user."""


def download_media(
    url: str,
    media_type: str,
    start: str = "",
    end: str = "",
    progress_callback: ProgressCallback | None = None,
    is_cancelled: Callable[[], bool] | None = None,
) -> str | None:

    os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

    output = os.path.join(
        DOWNLOAD_FOLDER,
        "%(title)s.%(ext)s"
    )

    def progress_hook(data):

        if is_cancelled and is_cancelled():
            raise DownloadCancelled("Download cancelled by user")

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

            info = ydl.extract_info(url, download=True)

            if is_cancelled and is_cancelled():
                raise DownloadCancelled("Download cancelled by user")

            output_path = ydl.prepare_filename(info)
            if media_type == "audio":
                output_path = os.path.splitext(output_path)[0] + ".mp3"
            else:
                output_path = os.path.splitext(output_path)[0] + ".mp4"

        if progress_callback:
            progress_callback(100, "Download complete!")

        return output_path

    except Exception as e:

        if progress_callback:
            progress_callback(0, f"Error: {str(e)}")

        print("Download error:", e)
        raise
