import customtkinter as ctk
from core.theme import *
from core.player import MusicPlayer
import os
import random


class LibraryPage(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        # ===========================
        # Music Player
        # ===========================

        self.player = MusicPlayer()
        self.current_file = None
        self.current_index = -1
        self.audio_files = []

        # ===========================
        # Player Modes
        # ===========================

        self.shuffle_enabled = False
        self.repeat_enabled = False

        # ===========================
        # Title
        # ===========================

        title = ctk.CTkLabel(
            self,
            text="🎵 Library",
            font=("Segoe UI", 30, "bold"),
            text_color=TEXT
        )

        title.pack(pady=(30, 5))

        # ===========================
        # Subtitle
        # ===========================

        subtitle = ctk.CTkLabel(
            self,
            text="Your downloaded media",
            font=("Segoe UI", 15),
            text_color=TEXT
        )

        subtitle.pack(pady=(0, 15))

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

        refresh_button.pack(
            pady=(0, 15)
        )

        # ===========================
        # Files Container
        # ===========================

        self.files_frame = ctk.CTkScrollableFrame(
            self,
            width=800,
            height=350
        )

        self.files_frame.pack(
            fill="both",
            expand=True,
            padx=50,
            pady=(0, 10)
        )

        # ===========================
        # Player Bar
        # ===========================

        self.player_frame = ctk.CTkFrame(
            self,
            height=160
        )

        self.player_frame.pack(
            fill="x",
            padx=50,
            pady=(5, 20)
        )

        self.player_frame.pack_propagate(False)

        # ===========================
        # Current Song
        # ===========================

        self.now_playing = ctk.CTkLabel(
            self.player_frame,
            text="Nothing playing",
            font=("Segoe UI", 15, "bold"),
            text_color=TEXT
        )

        self.now_playing.pack(
            pady=(10, 5)
        )

        # ===========================
        # Controls Container
        # ===========================

        controls = ctk.CTkFrame(
            self.player_frame,
            fg_color="transparent"
        )

        controls.pack()

        # ===========================
        # Previous
        # ===========================

        self.previous_button = ctk.CTkButton(
            controls,
            text="⏮ Previous",
            width=110,
            height=35,
            command=self.previous_music
        )

        self.previous_button.pack(
            side="left",
            padx=4
        )

        # ===========================
        # Play
        # ===========================

        self.play_button = ctk.CTkButton(
            controls,
            text="▶ Play",
            width=90,
            height=35,
            command=self.resume_music
        )

        self.play_button.pack(
            side="left",
            padx=4
        )

        # ===========================
        # Pause
        # ===========================

        self.pause_button = ctk.CTkButton(
            controls,
            text="⏸ Pause",
            width=90,
            height=35,
            command=self.pause_music
        )

        self.pause_button.pack(
            side="left",
            padx=4
        )

        # ===========================
        # Stop
        # ===========================

        self.stop_button = ctk.CTkButton(
            controls,
            text="⏹ Stop",
            width=90,
            height=35,
            command=self.stop_music
        )

        self.stop_button.pack(
            side="left",
            padx=4
        )

        # ===========================
        # Next
        # ===========================

        self.next_button = ctk.CTkButton(
            controls,
            text="Next ⏭",
            width=110,
            height=35,
            command=self.next_music
        )

        self.next_button.pack(
            side="left",
            padx=4
        )

        # ===========================
        # Shuffle
        # ===========================

        self.shuffle_button = ctk.CTkButton(
            controls,
            text="🔀 Shuffle",
            width=100,
            height=35,
            fg_color="#1f6aa5",
            hover_color="#144870",
            command=self.toggle_shuffle
        )

        self.shuffle_button.pack(
            side="left",
            padx=4
        )

        # ===========================
        # Repeat
        # ===========================

        self.repeat_button = ctk.CTkButton(
            controls,
            text="🔁 Repeat",
            width=100,
            height=35,
            fg_color="#1f6aa5",
            hover_color="#144870",
            command=self.toggle_repeat
        )

        self.repeat_button.pack(
            side="left",
            padx=4
        )

        # ===========================
        # Volume
        # ===========================

        self.volume_slider = ctk.CTkSlider(
            controls,
            width=150,
            from_=0,
            to=1,
            command=self.change_volume
        )

        self.volume_slider.set(0.8)

        self.volume_slider.pack(
            side="left",
            padx=12
        )

        # ===========================
        # Load Library
        # ===========================

        self.load_files()

    # ===================================
    # Load Files
    # ===================================

    def load_files(self):

        # Remove existing rows
        for widget in self.files_frame.winfo_children():
            widget.destroy()

        # Downloads folder
        downloads_folder = os.path.join(
            os.path.dirname(
                os.path.dirname(__file__)
            ),
            "downloads"
        )

        os.makedirs(
            downloads_folder,
            exist_ok=True
        )

        files = []

        # Scan downloads folder
        for filename in os.listdir(
            downloads_folder
        ):

            filepath = os.path.join(
                downloads_folder,
                filename
            )

            if os.path.isfile(filepath):

                files.append(
                    filename
                )

        # ===========================
        # Sort Newest First
        # ===========================

        files.sort(
            key=lambda filename:
                os.path.getmtime(
                    os.path.join(
                        downloads_folder,
                        filename
                    )
                ),
            reverse=True
        )

        # ===========================
        # Store Audio Files
        # ===========================

        self.audio_files = []

        for filename in files:

            extension = os.path.splitext(
                filename
            )[1].lower()

            if extension == ".mp3":

                self.audio_files.append(
                    os.path.join(
                        downloads_folder,
                        filename
                    )
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

            empty_label.pack(
                pady=100
            )

            return

        # ===========================
        # Create File Rows
        # ===========================

        for filename in files:

            self.create_file_row(
                filename,
                downloads_folder
            )

    # ===================================
    # Create File Row
    # ===================================

    def create_file_row(
        self,
        filename,
        downloads_folder
    ):

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

        extension = os.path.splitext(
            filename
        )[1].lower()

        # ===========================
        # File Icon
        # ===========================

        if extension == ".mp3":

            icon = "🎵"

        elif extension in [
            ".mp4",
            ".webm",
            ".mkv"
        ]:

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
        # Filename
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
        # MP3 Play Button
        # ===========================

        if extension == ".mp3":

            play_button = ctk.CTkButton(
                row,
                text="▶ Play",
                width=100,
                height=35,
                fg_color="#1f6aa5",
                hover_color="#144870",
                command=lambda:
                    self.play_file(
                        os.path.join(
                            downloads_folder,
                            filename
                        )
                    )
            )

            play_button.pack(
                side="right",
                padx=(5, 15)
            )

        # ===========================
        # Video / Other File
        # ===========================

        else:

            open_button = ctk.CTkButton(
                row,
                text="▶ Open",
                width=100,
                height=35,
                fg_color="#1f6aa5",
                hover_color="#144870",
                command=lambda:
                    self.open_file(
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
    # Play Music
    # ===================================

    def play_file(self, filepath):

        if not os.path.exists(filepath):

            self.now_playing.configure(
                text="File not found"
            )

            return

        success = self.player.play(
            filepath
        )

        if success:

            self.current_file = filepath

            # Find current song index
            if filepath in self.audio_files:

                self.current_index = (
                    self.audio_files.index(
                        filepath
                    )
                )

            filename = os.path.basename(
                filepath
            )

            self.now_playing.configure(
                text=f"🎵 {filename}"
            )

    # ===================================
    # Previous Music
    # ===================================

    def previous_music(self):

        if not self.audio_files:
            return

        # If no song is selected,
        # start from the last song.

        if self.current_index == -1:

            self.current_index = (
                len(self.audio_files) - 1
            )

        else:

            self.current_index -= 1

            # Loop to last song
            if self.current_index < 0:

                self.current_index = (
                    len(self.audio_files) - 1
                )

        filepath = self.audio_files[
            self.current_index
        ]

        self.play_file(
            filepath
        )

    # ===================================
    # Next Music
    # ===================================

    def next_music(self):

        if not self.audio_files:
            return

        # ===========================
        # Repeat Current Song
        # ===========================

        if (
            self.repeat_enabled
            and self.current_index != -1
        ):

            filepath = self.audio_files[
                self.current_index
            ]

            self.play_file(
                filepath
            )

            return

        # ===========================
        # Shuffle Mode
        # ===========================

        if self.shuffle_enabled:

            # Only one song
            if len(self.audio_files) == 1:

                self.current_index = 0

            else:

                possible_indexes = [
                    i
                    for i in range(
                        len(self.audio_files)
                    )
                    if i != self.current_index
                ]

                self.current_index = (
                    random.choice(
                        possible_indexes
                    )
                )

        # ===========================
        # Normal Mode
        # ===========================

        else:

            if self.current_index == -1:

                self.current_index = 0

            else:

                self.current_index += 1

                # Loop to first song
                if (
                    self.current_index
                    >= len(self.audio_files)
                ):

                    self.current_index = 0

        filepath = self.audio_files[
            self.current_index
        ]

        self.play_file(
            filepath
        )

    # ===================================
    # Toggle Shuffle
    # ===================================

    def toggle_shuffle(self):

        self.shuffle_enabled = (
            not self.shuffle_enabled
        )

        if self.shuffle_enabled:

            self.shuffle_button.configure(
                text="🔀 Shuffle ON",
                fg_color="#2e8b57",
                hover_color="#246b45"
            )

            print(
                "Shuffle enabled"
            )

        else:

            self.shuffle_button.configure(
                text="🔀 Shuffle",
                fg_color="#1f6aa5",
                hover_color="#144870"
            )

            print(
                "Shuffle disabled"
            )

    # ===================================
    # Toggle Repeat
    # ===================================

    def toggle_repeat(self):

        self.repeat_enabled = (
            not self.repeat_enabled
        )

        if self.repeat_enabled:

            self.repeat_button.configure(
                text="🔁 Repeat ON",
                fg_color="#2e8b57",
                hover_color="#246b45"
            )

            print(
                "Repeat enabled"
            )

        else:

            self.repeat_button.configure(
                text="🔁 Repeat",
                fg_color="#1f6aa5",
                hover_color="#144870"
            )

            print(
                "Repeat disabled"
            )

    # ===================================
    # Pause
    # ===================================

    def pause_music(self):

        self.player.pause()

    # ===================================
    # Resume
    # ===================================

    def resume_music(self):

        if not self.current_file:
            return

        if self.player.is_paused:

            self.player.resume()

        else:

            self.player.play(
                self.current_file
            )

    # ===================================
    # Stop
    # ===================================

    def stop_music(self):

        self.player.stop()

        self.now_playing.configure(
            text="Nothing playing"
        )

    # ===================================
    # Volume
    # ===================================

    def change_volume(
        self,
        value
    ):

        self.player.set_volume(
            float(value)
        )

    # ===================================
    # Open Video / Other Files
    # ===================================

    def open_file(
        self,
        filepath
    ):

        if not os.path.exists(filepath):

            print(
                "File not found:"
            )

            print(
                filepath
            )

            return

        try:

            os.startfile(
                filepath
            )

        except Exception as e:

            print(
                "Could not open file:"
            )

            print(
                e
            )