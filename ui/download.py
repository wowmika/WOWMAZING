import customtkinter as ctk
from core.theme import *
from core.downloader import download_media as start_download


class DownloadPage(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        # ===========================
        # Title
        # ===========================

        title = ctk.CTkLabel(
            self,
            text="⬇ Download Media",
            font=("Segoe UI", 30, "bold"),
            text_color=TEXT
        )
        title.pack(pady=30)

        # ===========================
        # URL Label
        # ===========================

        url_label = ctk.CTkLabel(
            self,
            text="YouTube URL",
            font=("Segoe UI", 16, "bold"),
            text_color=TEXT
        )
        url_label.pack(anchor="w", padx=60, pady=(20, 5))

        # ===========================
        # URL Entry
        # ===========================

        self.url_entry = ctk.CTkEntry(
            self,
            width=700,
            height=40,
            placeholder_text="Paste YouTube URL here..."
        )
        self.url_entry.pack(anchor="w", padx=60)

        # ===========================
        # Media Type
        # ===========================

        media_label = ctk.CTkLabel(
            self,
            text="Media Type",
            font=("Segoe UI", 16, "bold"),
            text_color=TEXT
        )
        media_label.pack(anchor="w", padx=60, pady=(25, 5))

        self.media_type = ctk.StringVar(value="audio")

        audio_radio = ctk.CTkRadioButton(
            self,
            text="🎵 Audio",
            variable=self.media_type,
            value="audio"
        )
        audio_radio.pack(anchor="w", padx=80)

        video_radio = ctk.CTkRadioButton(
            self,
            text="🎥 Video",
            variable=self.media_type,
            value="video"
        )
        video_radio.pack(anchor="w", padx=80)

        # ===========================
        # Start Time
        # ===========================

        start_label = ctk.CTkLabel(
            self,
            text="Start Time (HH:MM:SS)",
            font=("Segoe UI", 16, "bold"),
            text_color=TEXT
        )
        start_label.pack(anchor="w", padx=60, pady=(25, 5))

        self.start_entry = ctk.CTkEntry(
            self,
            width=250,
            height=40,
            placeholder_text="00:00:00"
        )
        self.start_entry.pack(anchor="w", padx=60)

        # ===========================
        # End Time
        # ===========================

        end_label = ctk.CTkLabel(
            self,
            text="End Time (HH:MM:SS)",
            font=("Segoe UI", 16, "bold"),
            text_color=TEXT
        )
        end_label.pack(anchor="w", padx=60, pady=(25, 5))

        self.end_entry = ctk.CTkEntry(
            self,
            width=250,
            height=40,
            placeholder_text="00:00:00"
        )
        self.end_entry.pack(anchor="w", padx=60)

        # ===========================
        # Download Button
        # ===========================

        self.download_button = ctk.CTkButton(
            self,
            text="⬇ DOWNLOAD",
            width=250,
            height=45,
            font=("Segoe UI", 18, "bold"),
            fg_color="#1f6aa5",
            hover_color="#144870",
            command=self.download_media
        )
        self.download_button.pack(pady=40)

    # ===================================
    # Download Function
    # ===================================

    def download_media(self):

        url = self.url_entry.get().strip()
        media = self.media_type.get()
        start = self.start_entry.get().strip()
        end = self.end_entry.get().strip()

        if url == "":
            print("Please enter a YouTube URL.")
            return

        try:
            start_download(
                url,
                media,
                start,
                end
            )
            print("Download started...")
        except Exception as e:
            print(f"Error: {e}")