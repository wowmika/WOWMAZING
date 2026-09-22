import customtkinter as ctk
from core.theme import *
from core.download_queue import DownloadJob, DownloadQueue
from typing import Callable


class DownloadPage(ctk.CTkFrame):

    def __init__(
        self,
        master,
        on_download_completed: Callable[[], None] | None = None,
    ):
        super().__init__(master)

        self.download_queue = DownloadQueue()
        self.on_download_completed = on_download_completed
        self._last_status: dict[str, str] = {}

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

        url_label.pack(
            anchor="w",
            padx=60,
            pady=(20, 5)
        )

        # ===========================
        # URL Entry
        # ===========================

        self.url_entry = ctk.CTkEntry(
            self,
            width=700,
            height=40,
            placeholder_text="Paste YouTube URL here..."
        )

        self.url_entry.pack(
            anchor="w",
            padx=60
        )

        # ===========================
        # Media Type
        # ===========================

        media_label = ctk.CTkLabel(
            self,
            text="Media Type",
            font=("Segoe UI", 16, "bold"),
            text_color=TEXT
        )

        media_label.pack(
            anchor="w",
            padx=60,
            pady=(25, 5)
        )

        self.media_type = ctk.StringVar(
            value="audio"
        )

        audio_radio = ctk.CTkRadioButton(
            self,
            text="🎵 Audio",
            variable=self.media_type,
            value="audio"
        )

        audio_radio.pack(
            anchor="w",
            padx=80
        )

        video_radio = ctk.CTkRadioButton(
            self,
            text="🎥 Video",
            variable=self.media_type,
            value="video"
        )

        video_radio.pack(
            anchor="w",
            padx=80
        )

        # ===========================
        # Start Time
        # ===========================

        start_label = ctk.CTkLabel(
            self,
            text="Start Time (HH:MM:SS)",
            font=("Segoe UI", 16, "bold"),
            text_color=TEXT
        )

        start_label.pack(
            anchor="w",
            padx=60,
            pady=(25, 5)
        )

        self.start_entry = ctk.CTkEntry(
            self,
            width=250,
            height=40,
            placeholder_text="00:00:00"
        )

        self.start_entry.pack(
            anchor="w",
            padx=60
        )

        # ===========================
        # End Time
        # ===========================

        end_label = ctk.CTkLabel(
            self,
            text="End Time (HH:MM:SS)",
            font=("Segoe UI", 16, "bold"),
            text_color=TEXT
        )

        end_label.pack(
            anchor="w",
            padx=60,
            pady=(25, 5)
        )

        self.end_entry = ctk.CTkEntry(
            self,
            width=250,
            height=40,
            placeholder_text="00:00:00"
        )

        self.end_entry.pack(
            anchor="w",
            padx=60
        )

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

        self.download_button.pack(
            pady=30
        )

        # ===========================
        # Progress Bar
        # ===========================

        self.progress_bar = ctk.CTkProgressBar(
            self,
            width=500,
            height=20
        )

        self.progress_bar.set(0)

        self.progress_bar.pack(
            pady=(0, 10)
        )

        # ===========================
        # Status Label
        # ===========================

        self.status_label = ctk.CTkLabel(
            self,
            text="Ready",
            font=("Segoe UI", 14),
            text_color=TEXT
        )

        self.status_label.pack(
            pady=(0, 20)
        )

        queue_title = ctk.CTkLabel(
            self,
            text="Download Queue",
            font=("Segoe UI", 18, "bold"),
            text_color=TEXT,
        )
        queue_title.pack(anchor="w", padx=60, pady=(0, 8))

        self.queue_frame = ctk.CTkScrollableFrame(
            self,
            height=190,
        )
        self.queue_frame.pack(fill="both", expand=True, padx=60, pady=(0, 25))

        self.refresh_queue()

    # ===================================
    # Download Function
    # ===================================

    def download_media(self):

        url = self.url_entry.get().strip()

        media = self.media_type.get()

        start = self.start_entry.get().strip()

        end = self.end_entry.get().strip()

        # ===========================
        # Check URL
        # ===========================

        if url == "":
            self.status_label.configure(
                text="Please enter a YouTube URL."
            )
            return

        self.progress_bar.set(0)
        self.status_label.configure(
            text="Added to download queue."
        )
        self.download_queue.add_job(url, media, start, end)

    # ===================================
    # Queue rendering
    # ===================================

    def refresh_queue(self) -> None:
        jobs = self.download_queue.get_jobs()
        for widget in self.queue_frame.winfo_children():
            widget.destroy()

        if not jobs:
            ctk.CTkLabel(
                self.queue_frame,
                text="No downloads queued.",
                text_color=TEXT,
            ).pack(pady=20)

        for job in jobs:
            self.create_job_row(job)
            previous_status = self._last_status.get(job.id)
            if job.status == "completed" and previous_status != "completed":
                self.status_label.configure(text="Download complete!")
                if self.on_download_completed:
                    self.on_download_completed()
            elif job.status == "failed" and previous_status != "failed":
                self.status_label.configure(text=f"Download failed: {job.error or 'Unknown error'}")
            elif job.status == "cancelled" and previous_status != "cancelled":
                self.status_label.configure(text="Download cancelled.")
            self._last_status[job.id] = job.status

        self.after(250, self.refresh_queue)

    def create_job_row(self, job: DownloadJob) -> None:
        row = ctk.CTkFrame(self.queue_frame)
        row.pack(fill="x", padx=5, pady=5)

        title = job.url if len(job.url) <= 68 else f"{job.url[:65]}..."
        ctk.CTkLabel(
            row,
            text=f"{job.media_type.title()} — {title}",
            anchor="w",
            text_color=TEXT,
        ).pack(fill="x", padx=12, pady=(8, 1))

        detail = job.status.title()
        if job.status in {"downloading", "processing"}:
            detail = f"{detail} — {job.progress:.1f}%"
        elif job.error:
            detail = f"{detail} — {job.error}"

        detail_frame = ctk.CTkFrame(row, fg_color="transparent")
        detail_frame.pack(fill="x", padx=12, pady=(1, 8))
        ctk.CTkLabel(detail_frame, text=detail, text_color=TEXT).pack(side="left")

        if job.status in {"queued", "downloading", "processing"}:
            ctk.CTkButton(
                detail_frame,
                text="Cancel",
                width=75,
                height=28,
                command=lambda job_id=job.id: self.download_queue.cancel_job(job_id),
            ).pack(side="right")

        progress = ctk.CTkProgressBar(row)
        progress.set(job.progress / 100)
        progress.pack(fill="x", padx=12, pady=(0, 10))
