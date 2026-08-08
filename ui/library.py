import customtkinter as ctk
from core.theme import *
import os
import subprocess


class LibraryPage(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        # ===========================
        # Title
        # ===========================

        title = ctk.CTkLabel(
            self,
            text="🎵 Library",
            font=("Segoe UI", 30, "bold"),
            text_color=TEXT
        )

        title.pack(pady=(30, 10))

        # ===========================
        # Subtitle
        # ===========================

        subtitle = ctk.CTkLabel(
            self,
            text="Your downloaded media",
            font=("Segoe UI", 15),
            text_color=TEXT
        )

        subtitle.pack(pady=(0, 20))

        # ===========================
        # Refresh Button
        # ===========================

        refresh_button = ctk.CTkButton(
            self,
            text="🔄 Refresh Library",
            width=180,
            height=40,
            font=("Segoe UI", 14, "bold"),
            fg_color="#1f6aa5",
            hover_color="#144870",
            command=self.load_files
        )

        refresh_button.pack(pady=(0, 20))

        # ===========================
        # Files Container
        # ===========================

        self.files_frame = ctk.CTkScrollableFrame(
            self,
            width=800,
            height=450
        )

        self.files_frame.pack(
            fill="both",
            expand=True,
            padx=50,
            pady=(0, 30)
        )

        # ===========================
        # Load Files
        # ===========================

        self.load_files()

    # ===================================
    # Load Downloaded Files
    # ===================================

    def load_files(self):

        # Remove old widgets
        for widget in self.files_frame.winfo_children():
            widget.destroy()

        # Downloads folder
        downloads_folder = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "downloads"
        )

        # Create folder if it doesn't exist
        os.makedirs(downloads_folder, exist_ok=True)

        # Get files
        files = []

        for filename in os.listdir(downloads_folder):

            filepath = os.path.join(
                downloads_folder,
                filename
            )

            if os.path.isfile(filepath):
                files.append(filename)

        # Sort newest first
        files.sort(
            key=lambda filename: os.path.getmtime(
                os.path.join(downloads_folder, filename)
            ),
            reverse=True
        )

        # ===========================
        # Empty Library
        # ===========================

        if not files:

            empty_label = ctk.CTkLabel(
                self.files_frame,
                text="📂 Your library is empty",
                font=("Segoe UI", 20, "bold"),
                text_color=TEXT
            )

            empty_label.pack(pady=100)

            return

        # ===========================
        # Display Files
        # ===========================

        for filename in files:

            self.create_file_row(
                filename,
                downloads_folder
            )

    # ===================================
    # Create File Row
    # ===================================

    def create_file_row(self, filename, downloads_folder):

        row = ctk.CTkFrame(
            self.files_frame,
            height=70
        )

        row.pack(
            fill="x",
            padx=10,
            pady=6
        )

        row.pack_propagate(False)

        # ===========================
        # File Icon
        # ===========================

        extension = os.path.splitext(filename)[1].lower()

        if extension == ".mp3":
            icon = "🎵"
        elif extension in [".mp4", ".webm", ".mkv"]:
            icon = "🎥"
        else:
            icon = "📄"

        icon_label = ctk.CTkLabel(
            row,
            text=icon,
            font=("Segoe UI", 22)
        )

        icon_label.pack(
            side="left",
            padx=(15, 10)
        )

        # ===========================
        # File Name
        # ===========================

        name_label = ctk.CTkLabel(
            row,
            text=filename,
            font=("Segoe UI", 14),
            text_color=TEXT,
            anchor="w"
        )

        name_label.pack(
            side="left",
            fill="x",
            expand=True,
            padx=10
        )

        # ===========================
        # Open Button
        # ===========================

        open_button = ctk.CTkButton(
            row,
            text="▶ Open",
            width=100,
            height=35,
            fg_color="#1f6aa5",
            hover_color="#144870",
            command=lambda: self.open_file(
                os.path.join(
                    downloads_folder,
                    filename
                )
            )
        )

        open_button.pack(
            side="right",
            padx=(5, 15)
        )

    # ===================================
    # Open File
    # ===================================

    def open_file(self, filepath):

        if not os.path.exists(filepath):
            print("File not found:")
            print(filepath)
            return

        try:

            os.startfile(filepath)

        except Exception as e:

            print("Could not open file:")
            print(e)