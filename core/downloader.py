import subprocess
import os

DOWNLOAD_FOLDER = "downloads"


def download_media(url, media_type, start="", end=""):

    os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

    output = os.path.join(
        DOWNLOAD_FOLDER,
        "%(title)s.%(ext)s"
    )

    command = [
        "yt-dlp",
        "-o",
        output
    ]

    if media_type == "audio":
        command += [
            "-x",
            "--audio-format",
            "mp3"
        ]

    if start != "" and end != "":
        command += [
            "--download-sections",
            f"*{start}-{end}"
        ]

    command.append(url)

    print("Running command:")
    print(command)

    subprocess.run(command)