import os
import pygame
from mutagen.mp3 import MP3


class MusicPlayer:

    def __init__(self):

        # ===================================
        # Initialize pygame mixer
        # ===================================

        pygame.mixer.init()

        self.current_file = None
        self.is_playing = False
        self.is_paused = False

        # Song duration
        self.duration = 0

        # Position from which playback started
        self.seek_offset = 0

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

    # ===================================
    # Pause
    # ===================================

    def pause(self):

        if self.is_playing and not self.is_paused:

            pygame.mixer.music.pause()

            self.is_paused = True

            print("Paused")

    # ===================================
    # Resume
    # ===================================

    def resume(self):

        if self.is_paused:

            pygame.mixer.music.unpause()

            self.is_paused = False

            print("Resumed")

    # ===================================
    # Stop
    # ===================================

    def stop(self):

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

        return not pygame.mixer.music.get_busy()

    # ===================================
    # Reset
    # ===================================

    def reset(self):

        pygame.mixer.music.stop()

        self.current_file = None
        self.is_playing = False
        self.is_paused = False

        self.duration = 0
        self.seek_offset = 0