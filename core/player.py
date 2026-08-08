import os
import pygame


class MusicPlayer:

    def __init__(self):

        # Initialize pygame mixer
        pygame.mixer.init()

        self.current_file = None
        self.is_playing = False
        self.is_paused = False

    # ===================================
    # Play
    # ===================================

    def play(self, filepath):

        if not os.path.exists(filepath):
            print("File not found:")
            print(filepath)
            return False

        try:

            pygame.mixer.music.load(filepath)
            pygame.mixer.music.play()

            self.current_file = filepath
            self.is_playing = True
            self.is_paused = False

            print("Playing:")
            print(filepath)

            return True

        except Exception as e:

            print("Could not play file:")
            print(e)

            return False

    # ===================================
    # Pause
    # ===================================

    def pause(self):

        if self.is_playing:

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

        print("Stopped")

    # ===================================
    # Volume
    # ===================================

    def set_volume(self, volume):

        # volume should be between 0 and 1

        volume = max(
            0,
            min(1, volume)
        )

        pygame.mixer.music.set_volume(volume)

    # ===================================
    # Check Playing Status
    # ===================================

    def is_music_playing(self):

        return pygame.mixer.music.get_busy()