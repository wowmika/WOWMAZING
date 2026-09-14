import os
from dataclasses import dataclass
from io import BytesIO

import pygame
from mutagen.mp3 import MP3
from PIL import Image, ImageDraw


@dataclass(frozen=True)
class TrackMetadata:
    """Display metadata extracted from a local MP3 file."""

    title: str
    artist: str
    duration: float
    artwork: Image.Image


class MusicPlayer:

    def __init__(self):

        # ===================================
        # Initialize pygame mixer
        # ===================================

        self._mixer_initialized = False

        self.current_file = None
        self.is_playing = False
        self.is_paused = False

        # Song duration
        self.duration = 0

        # Position from which playback started
        self.seek_offset = 0

    def _ensure_mixer(self):
        """Delay audio-device startup until the user actually plays a track."""
        if not self._mixer_initialized:
            pygame.mixer.init()
            self._mixer_initialized = True

    # ===================================
    # Play
    # ===================================

    def play(self, filepath):

        if not os.path.exists(filepath):

            print("File not found:")
            print(filepath)

            return False

        try:

            # ===================================
            # Load music
            # ===================================

            self._ensure_mixer()
            pygame.mixer.music.load(filepath)

            # ===================================
            # Get duration quickly
            # ===================================

            self.duration = self.get_file_duration(
                filepath
            )

            # New song starts at beginning
            self.seek_offset = 0

            # ===================================
            # Start playback
            # ===================================

            pygame.mixer.music.play()

            self.current_file = filepath

            self.is_playing = True
            self.is_paused = False

            print("Playing:")
            print(filepath)

            print(
                f"Duration: {self.duration:.2f} seconds"
            )

            return True

        except Exception as e:

            print("Could not play file:")
            print(e)

            return False

    # ===================================
    # Get MP3 Duration
    # ===================================

    def get_file_duration(self, filepath):

        try:

            audio = MP3(filepath)

            return audio.info.length

        except Exception as e:

            print("Could not read MP3 duration:")
            print(e)

            return 0

    def get_track_metadata(self, filepath: str) -> TrackMetadata:
        """Read MP3 tags and embedded artwork, with useful display fallbacks."""
        title = os.path.splitext(os.path.basename(filepath))[0]
        artist = "Unknown artist"
        duration = self.get_file_duration(filepath)
        artwork = self._default_artwork()

        try:
            audio = MP3(filepath)
            tags = audio.tags
            if tags:
                title_frame = tags.get("TIT2")
                artist_frame = tags.get("TPE1")
                if title_frame and title_frame.text:
                    title = str(title_frame.text[0])
                if artist_frame and artist_frame.text:
                    artist = str(artist_frame.text[0])

                pictures = tags.getall("APIC")
                if pictures:
                    with Image.open(BytesIO(pictures[0].data)) as image:
                        artwork = image.convert("RGB")
        except Exception as error:
            print("Could not read track metadata:")
            print(error)

        return TrackMetadata(title, artist, duration, artwork)

    @staticmethod
    def _default_artwork() -> Image.Image:
        """Create a neutral built-in cover when a track has no embedded art."""
        artwork = Image.new("RGB", (160, 160), "#1f6aa5")
        draw = ImageDraw.Draw(artwork)
        draw.ellipse((35, 35, 125, 125), fill="#252526", outline="#22C55E", width=5)
        draw.rectangle((75, 57, 84, 108), fill="#ffffff")
        draw.ellipse((66, 99, 84, 117), fill="#ffffff")
        return artwork

    # ===================================
    # Pause
    # ===================================

    def pause(self):

        if self.is_playing and not self.is_paused:

            self._ensure_mixer()
            pygame.mixer.music.pause()

            self.is_paused = True

            print("Paused")

    # ===================================
    # Resume
    # ===================================

    def resume(self):

        if self.is_paused:

            self._ensure_mixer()
            pygame.mixer.music.unpause()

            self.is_paused = False

            print("Resumed")

    # ===================================
    # Stop
    # ===================================

    def stop(self):

        if self._mixer_initialized:
            pygame.mixer.music.stop()

        self.is_playing = False
        self.is_paused = False

        self.seek_offset = 0

        print("Stopped")

    # ===================================
    # Volume
    # ===================================

    def set_volume(self, volume):

        try:

            volume = float(volume)

            volume = max(
                0,
                min(1, volume)
            )

            self._ensure_mixer()
            pygame.mixer.music.set_volume(
                volume
            )

        except Exception as e:

            print("Could not set volume:")
            print(e)

    # ===================================
    # Get Current Position
    # ===================================

    def get_position(self):

        if not self.is_playing:

            return self.seek_offset

        try:

            position = pygame.mixer.music.get_pos()

            if position < 0:

                return self.seek_offset

            # pygame returns milliseconds
            elapsed = position / 1000

            # Add seek offset
            current_position = (
                self.seek_offset + elapsed
            )

            # Don't exceed duration
            if self.duration > 0:

                current_position = min(
                    current_position,
                    self.duration
                )

            return current_position

        except Exception as e:

            print("Could not get position:")
            print(e)

            return self.seek_offset

    # ===================================
    # Get Duration
    # ===================================

    def get_duration(self):

        return self.duration

    # ===================================
    # Seek
    # ===================================

    def seek(self, seconds):

        if not self.current_file:

            return False

        try:

            seconds = float(seconds)

            # Keep position inside song
            if self.duration > 0:

                seconds = max(
                    0,
                    min(
                        seconds,
                        self.duration
                    )
                )

            else:

                seconds = max(
                    0,
                    seconds
                )

            # Remember seek position
            self.seek_offset = seconds

            # Start from selected position
            self._ensure_mixer()
            pygame.mixer.music.play(
                start=seconds
            )

            self.is_playing = True
            self.is_paused = False

            print(
                f"Seeked to {seconds:.2f} seconds"
            )

            return True

        except Exception as e:

            print("Could not seek:")
            print(e)

            return False

    # ===================================
    # Check Playing Status
    # ===================================

    def is_music_playing(self):

        try:

            if not self._mixer_initialized:
                return False
            return pygame.mixer.music.get_busy()

        except Exception:

            return False

    # ===================================
    # Check Finished
    # ===================================

    def has_finished(self):

        if not self.current_file:
            return False

        if self.is_paused:
            return False

        if not self.is_playing:
            return False

        return not self.is_music_playing()

    # ===================================
    # Reset
    # ===================================

    def reset(self):

        if self._mixer_initialized:
            pygame.mixer.music.stop()

        self.current_file = None
        self.is_playing = False
        self.is_paused = False

        self.duration = 0
        self.seek_offset = 0
