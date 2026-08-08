import customtkinter as ctk
from core.theme import *
from core.player import MusicPlayer
import os
import random
import json


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
        # Seek State
        # ===========================

        self.user_seeking = False

        # Prevent multiple automatic next calls
        self.song_change_in_progress = False

        # ===========================
        # Library Search
        # ===========================

        self.all_files = []
        self.search_query = ""

        # ===========================
        # Favorites
        # ===========================

        self.favorites_file = os.path.join(
            os.path.dirname(
                os.path.dirname(__file__)
            ),
            "database",
            "favorites.json"
        )

        self.favorites = set()
        self.favorites_only = False

        self.load_favorites()

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
        # Search Library
        # ===========================

        search_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        search_frame.pack(
            fill="x",
            padx=50,
            pady=(0, 10)
        )

        self.search_entry = ctk.CTkEntry(
            search_frame,
            width=650,
            height=40,
            placeholder_text="🔎 Search your library..."
        )

        self.search_entry.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(0, 10)
        )

        self.search_entry.bind(
            "<KeyRelease>",
            self.search_library
        )

        clear_search_button = ctk.CTkButton(
            search_frame,
            text="✕ Clear",
            width=90,
            height=40,
            command=self.clear_search
        )

        clear_search_button.pack(
            side="right"
        )

        # ===========================
        # Favorites Filter
        # ===========================

        self.favorites_button = ctk.CTkButton(
            self,
            text="⭐ Favorites",
            width=180,
            height=40,
            font=("Segoe UI", 14, "bold"),
            fg_color="#1f6aa5",
            hover_color="#144870",
            command=self.toggle_favorites_filter
        )

        self.favorites_button.pack(
            pady=(0, 10)
        )

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
            height=220
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
        # Progress Time Container
        # ===========================

        time_frame = ctk.CTkFrame(
            self.player_frame,
            fg_color="transparent"
        )

        time_frame.pack(
            fill="x",
            padx=70,
            pady=(5, 0)
        )

        # Current time

        self.current_time_label = ctk.CTkLabel(
            time_frame,
            text="00:00",
            font=("Segoe UI", 12),
            text_color=TEXT
        )

        self.current_time_label.pack(
            side="left"
        )

        # Duration

        self.duration_label = ctk.CTkLabel(
            time_frame,
            text="00:00",
            font=("Segoe UI", 12),
            text_color=TEXT
        )

        self.duration_label.pack(
            side="right"
        )

        # ===========================
        # Progress Slider
        # ===========================

        self.progress_slider = ctk.CTkSlider(
            self.player_frame,
            width=700,
            height=16,
            from_=0,
            to=1,
            command=self.progress_slider_changed
        )

        self.progress_slider.set(0)

        self.progress_slider.pack(
            padx=70,
            pady=(2, 8)
        )

        # Detect when user starts dragging

        self.progress_slider.bind(
            "<ButtonPress-1>",
            self.start_seeking
        )

        # Detect when user releases slider

        self.progress_slider.bind(
            "<ButtonRelease-1>",
            self.finish_seeking
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

        # ===========================
        # Start Progress Updates
        # ===========================

        self.update_progress()

    # ===================================
    # Format Time
    # ===================================

    def format_time(self, seconds):

        try:
            seconds = int(seconds)

        except (TypeError, ValueError):
            seconds = 0

        minutes = seconds // 60
        remaining_seconds = seconds % 60

        hours = minutes // 60
        minutes = minutes % 60

        if hours > 0:

            return (
                f"{hours:02d}:"
                f"{minutes:02d}:"
                f"{remaining_seconds:02d}"
            )

        return (
            f"{minutes:02d}:"
            f"{remaining_seconds:02d}"
        )

    # ===================================
    # Progress Slider Changed
    # ===================================

    def progress_slider_changed(self, value):

        if not self.user_seeking:
            return

        duration = self.player.get_duration()

        if duration <= 0:
            return

        position = float(value)

        self.current_time_label.configure(
            text=self.format_time(position)
        )

    # ===================================
    # Start Seeking
    # ===================================

    def start_seeking(self, event=None):

        self.user_seeking = True

    # ===================================
    # Finish Seeking
    # ===================================

    def finish_seeking(self, event=None):

        self.user_seeking = False

        duration = self.player.get_duration()

        if duration <= 0:
            return

        position = float(
            self.progress_slider.get()
        )

        self.player.seek(position)

    # ===================================
    # Update Progress
    # ===================================

    def update_progress(self):

        try:

            if self.current_file:

                duration = self.player.get_duration()

                position = self.player.get_position()

                # ===========================
                # Update Duration
                # ===========================

                self.duration_label.configure(
                    text=self.format_time(duration)
                )

                # ===========================
                # Update Progress
                # ===========================

                if not self.user_seeking and duration > 0:

                    position = min(
                        position,
                        duration
                    )

                    self.progress_slider.configure(
                        from_=0,
                        to=duration
                    )

                    self.progress_slider.set(
                        position
                    )

                    self.current_time_label.configure(
                        text=self.format_time(position)
                    )

                # ===========================
                # Detect Song Finished
                # ===========================

                if (
                    self.player.is_playing
                    and not self.player.is_paused
                    and self.player.has_finished()
                    and not self.song_change_in_progress
                ):

                    print("Song finished.")

                    self.handle_song_finished()

        except Exception as e:

            print(
                "Progress update error:"
            )

            print(e)

        # Run again after 500 ms

        self.after(
            500,
            self.update_progress
        )

    # ===================================
    # Handle Song Finished
    # ===================================

    def handle_song_finished(self):

        if not self.audio_files:
            return

        # Prevent repeated calls
        self.song_change_in_progress = True

        try:

            # ===========================
            # Repeat Current Song
            # ===========================

            if self.repeat_enabled:

                if self.current_index == -1:

                    return

                filepath = self.audio_files[
                    self.current_index
                ]

                print(
                    "Repeat enabled - replaying current song."
                )

                self.play_file(
                    filepath
                )

                return

            # ===========================
            # Shuffle Mode
            # ===========================

            if self.shuffle_enabled:

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

                    self.current_index = random.choice(
                        possible_indexes
                    )

                filepath = self.audio_files[
                    self.current_index
                ]

                print(
                    "Shuffle enabled - playing random song."
                )

                self.play_file(
                    filepath
                )

                return

            # ===========================
            # Normal Next
            # ===========================

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

            print(
                "Playing next song."
            )

            self.play_file(
                filepath
            )

        finally:

            # Allow future automatic song changes
            self.song_change_in_progress = False

    # ===================================
    # Load Favorites
    # ===================================

    def load_favorites(self):

        try:

            os.makedirs(
                os.path.dirname(
                    self.favorites_file
                ),
                exist_ok=True
            )

            if not os.path.exists(
                self.favorites_file
            ):

                self.favorites = set()
                return

            with open(
                self.favorites_file,
                "r",
                encoding="utf-8"
            ) as file:

                data = json.load(file)

            if isinstance(data, list):

                self.favorites = set(data)

            else:

                self.favorites = set()

        except Exception as e:

            print("Could not load favorites:")
            print(e)

            self.favorites = set()

    # ===================================
    # Save Favorites
    # ===================================

    def save_favorites(self):

        try:

            os.makedirs(
                os.path.dirname(
                    self.favorites_file
                ),
                exist_ok=True
            )

            with open(
                self.favorites_file,
                "w",
                encoding="utf-8"
            ) as file:

                json.dump(
                    sorted(self.favorites),
                    file,
                    indent=4,
                    ensure_ascii=False
                )

        except Exception as e:

            print("Could not save favorites:")
            print(e)

    # ===================================
    # Toggle Favorite
    # ===================================

    def toggle_favorite(self, filename):

        if filename in self.favorites:

            self.favorites.remove(filename)

            print(
                f"Removed from favorites: {filename}"
            )

        else:

            self.favorites.add(filename)

            print(
                f"Added to favorites: {filename}"
            )

        self.save_favorites()

        self.display_files(
            self.search_query
        )

    # ===================================
    # Toggle Favorites Filter
    # ===================================

    def toggle_favorites_filter(self):

        self.favorites_only = (
            not self.favorites_only
        )

        if self.favorites_only:

            self.favorites_button.configure(
                text="⭐ Favorites ON",
                fg_color="#2e8b57",
                hover_color="#246b45"
            )

            print("Favorites filter enabled")

        else:

            self.favorites_button.configure(
                text="⭐ Favorites",
                fg_color="#1f6aa5",
                hover_color="#144870"
            )

            print("Favorites filter disabled")

        self.display_files(
            self.search_query
        )

    # ===================================
    # Load Files
    # ===================================

    def load_files(self):

        for widget in self.files_frame.winfo_children():
            widget.destroy()

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

        for filename in os.listdir(downloads_folder):

            filepath = os.path.join(
                downloads_folder,
                filename
            )

            if os.path.isfile(filepath):
                files.append(filename)

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

        self.all_files = files

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

        if not files:

            empty_label = ctk.CTkLabel(
                self.files_frame,
                text="📂 Your library is empty",
                font=("Segoe UI", 20, "bold"),
                text_color=TEXT
            )

            empty_label.pack(pady=100)
            return

        self.display_files(
            self.search_query
        )

    # ===================================
    # Search Library
    # ===================================

    def search_library(self, event=None):

        self.search_query = (
            self.search_entry.get()
            .strip()
            .lower()
        )

        self.display_files(
            self.search_query
        )

    # ===================================
    # Clear Search
    # ===================================

    def clear_search(self):

        self.search_entry.delete(
            0,
            "end"
        )

        self.search_query = ""

        self.display_files()

        self.search_entry.focus_set()

    # ===================================
    # Display Files
    # ===================================

    def display_files(self, query=""):

        for widget in self.files_frame.winfo_children():
            widget.destroy()

        downloads_folder = os.path.join(
            os.path.dirname(
                os.path.dirname(__file__)
            ),
            "downloads"
        )

        query = query.strip().lower()

        # ===========================
        # Filter by Search + Favorites
        # ===========================

        files = list(self.all_files)

        if query:

            files = [
                filename
                for filename in files
                if query in filename.lower()
            ]

        if self.favorites_only:

            files = [
                filename
                for filename in files
                if filename in self.favorites
            ]

        if not files:

            if query:
                message = f'🔎 No results for "{query}"'
            else:
                message = "📂 Your library is empty"

            empty_label = ctk.CTkLabel(
                self.files_frame,
                text=message,
                font=("Segoe UI", 20, "bold"),
                text_color=TEXT
            )

            empty_label.pack(pady=100)
            return

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
        # Favorite Button
        # ===========================

        is_favorite = (
            filename in self.favorites
        )

        favorite_button = ctk.CTkButton(
            row,
            text="⭐" if is_favorite else "☆",
            width=40,
            height=35,
            fg_color="transparent",
            hover_color="#333333",
            command=lambda:
                self.toggle_favorite(filename)
        )

        favorite_button.pack(
            side="right",
            padx=(5, 5)
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
                padx=(5, 5)
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
                padx=(5, 5)
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

        try:

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

                # ===========================
                # Reset Progress
                # ===========================

                duration = self.player.get_duration()

                self.progress_slider.configure(
                    from_=0,
                    to=max(duration, 1)
                )

                self.progress_slider.set(0)

                self.current_time_label.configure(
                    text="00:00"
                )

                self.duration_label.configure(
                    text=self.format_time(duration)
                )

        except Exception as e:

            print(
                "Could not play song:"
            )

            print(e)

    # ===================================
    # Previous Music
    # ===================================

    def previous_music(self):

        if not self.audio_files:
            return

        self.song_change_in_progress = True

        try:

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

        finally:

            self.song_change_in_progress = False

    # ===================================
    # Next Music
    # ===================================

    def next_music(self):

        if not self.audio_files:
            return

        self.song_change_in_progress = True

        try:

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

        finally:

            self.song_change_in_progress = False

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

        self.progress_slider.set(0)

        self.current_time_label.configure(
            text="00:00"
        )

        self.duration_label.configure(
            text=self.format_time(
                self.player.get_duration()
            )
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

            print(e)