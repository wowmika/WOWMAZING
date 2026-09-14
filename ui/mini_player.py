"""Persistent application-wide controls for the Library's shared player."""

from __future__ import annotations

import math
import os
import time
from typing import TYPE_CHECKING

import customtkinter as ctk
from PIL import Image

from core.theme import TEXT

if TYPE_CHECKING:
    from ui.library import LibraryPage


class MiniPlayer(ctk.CTkFrame):
    """A compact player that mirrors and controls LibraryPage playback."""

    def __init__(self, master: ctk.CTkBaseClass, library: LibraryPage) -> None:
        super().__init__(master, corner_radius=0, height=105)
        self.library = library
        self._displayed_file: str | None = None
        self._artwork_image: ctk.CTkImage | None = None
        self._wave_bars: list[ctk.CTkFrame] = []
        self._queue_visible = False

        self.queue_panel = ctk.CTkScrollableFrame(self, height=145)

        self.bar = ctk.CTkFrame(self, fg_color="transparent", height=105)
        self.bar.pack(fill="x", padx=20, pady=12)

        self.artwork_label = ctk.CTkLabel(self.bar, text="♫", width=72, height=72)
        self.artwork_label.pack(side="left", padx=(0, 12))

        details = ctk.CTkFrame(self.bar, fg_color="transparent")
        details.pack(side="left", fill="x", expand=True)
        self.title_label = ctk.CTkLabel(
            details,
            text="Nothing playing",
            font=("Segoe UI", 15, "bold"),
            anchor="w",
            text_color=TEXT,
        )
        self.title_label.pack(fill="x")
        self.artist_label = ctk.CTkLabel(
            details,
            text="Choose a song from your Library",
            font=("Segoe UI", 12),
            anchor="w",
            text_color=TEXT,
        )
        self.artist_label.pack(fill="x")
        self.duration_label = ctk.CTkLabel(
            details,
            text="00:00 / 00:00",
            font=("Segoe UI", 12),
            anchor="w",
            text_color=TEXT,
        )
        self.duration_label.pack(fill="x")

        self.waveform = ctk.CTkFrame(self.bar, width=248, height=50, fg_color="transparent")
        self.waveform.pack(side="left", padx=18)
        self.waveform.pack_propagate(False)
        for index in range(24):
            bar = ctk.CTkFrame(self.waveform, width=6, height=5, fg_color="#3B82F6")
            bar.place(x=4 + index * 10, y=42, anchor="sw")
            self._wave_bars.append(bar)

        controls = ctk.CTkFrame(self.bar, fg_color="transparent")
        controls.pack(side="right")
        self._button(controls, "⏮", self.library.previous_music).pack(side="left", padx=3)
        self.play_button = self._button(controls, "▶", self.toggle_play_pause)
        self.play_button.pack(side="left", padx=3)
        self._button(controls, "⏭", self.library.next_music).pack(side="left", padx=3)
        self.shuffle_button = self._button(controls, "🔀", self.library.toggle_shuffle)
        self.shuffle_button.pack(side="left", padx=3)
        self.repeat_button = self._button(controls, "🔁", self.library.toggle_repeat)
        self.repeat_button.pack(side="left", padx=3)
        self.queue_button = self._button(controls, "Up Next ▾", self.toggle_queue, width=95)
        self.queue_button.pack(side="left", padx=(10, 0))

        root = self.winfo_toplevel()
        root.bind_all("<space>", self._on_space)
        root.bind_all("<Control-Right>", self._on_next)
        root.bind_all("<Control-Left>", self._on_previous)
        self._refresh()

    @staticmethod
    def _button(master: ctk.CTkBaseClass, text: str, command, width: int = 42) -> ctk.CTkButton:
        return ctk.CTkButton(master, text=text, width=width, height=36, command=command)

    def toggle_play_pause(self) -> None:
        if self.library.player.is_paused:
            self.library.resume_music()
        elif self.library.player.is_music_playing():
            self.library.pause_music()
        elif self.library.current_file:
            self.library.resume_music()
        else:
            self.library.next_music()

    def toggle_queue(self) -> None:
        self._queue_visible = not self._queue_visible
        if self._queue_visible:
            self.queue_panel.pack(fill="x", padx=20, pady=(0, 12), before=self.bar)
            self.queue_button.configure(text="Up Next ▴")
            self._render_up_next()
        else:
            self.queue_panel.pack_forget()
            self.queue_button.configure(text="Up Next ▾")

    def _render_up_next(self) -> None:
        for widget in self.queue_panel.winfo_children():
            widget.destroy()

        upcoming = self._upcoming_files()
        if not upcoming:
            ctk.CTkLabel(self.queue_panel, text="No songs in the queue.", text_color=TEXT).pack(pady=15)
            return

        for position, filepath in enumerate(upcoming, start=1):
            ctk.CTkLabel(
                self.queue_panel,
                text=f"{position}. {os.path.splitext(os.path.basename(filepath))[0]}",
                anchor="w",
                text_color=TEXT,
            ).pack(fill="x", padx=12, pady=3)

    def _upcoming_files(self) -> list[str]:
        files = self.library.audio_files
        if not files:
            return []
        current = self.library.current_index
        start = 0 if current < 0 else (current + 1) % len(files)
        return [files[(start + offset) % len(files)] for offset in range(min(5, len(files)))]

    def _refresh(self) -> None:
        filepath = self.library.current_file
        if filepath and filepath != self._displayed_file:
            metadata = self.library.player.get_track_metadata(filepath)
            image = metadata.artwork.copy()
            image.thumbnail((72, 72), Image.Resampling.LANCZOS)
            self._artwork_image = ctk.CTkImage(light_image=image, dark_image=image, size=(72, 72))
            self.artwork_label.configure(image=self._artwork_image, text="")
            self.title_label.configure(text=metadata.title)
            self.artist_label.configure(text=metadata.artist)
            self._displayed_file = filepath
        elif not filepath and self._displayed_file:
            self._displayed_file = None
            self.artwork_label.configure(image=None, text="♫")
            self.title_label.configure(text="Nothing playing")
            self.artist_label.configure(text="Choose a song from your Library")

        position = self.library.player.get_position()
        duration = self.library.player.get_duration()
        self.duration_label.configure(text=f"{self._format_time(position)} / {self._format_time(duration)}")
        is_playing = self.library.player.is_music_playing() and not self.library.player.is_paused
        self.play_button.configure(text="⏸" if is_playing else "▶")
        self.shuffle_button.configure(fg_color="#2e8b57" if self.library.shuffle_enabled else "#1f6aa5")
        self.repeat_button.configure(fg_color="#2e8b57" if self.library.repeat_enabled else "#1f6aa5")
        self._animate_waveform(is_playing)
        if self._queue_visible:
            self._render_up_next()
        self.after(150, self._refresh)

    def _animate_waveform(self, is_playing: bool) -> None:
        moment = time.monotonic() * 8
        for index, bar in enumerate(self._wave_bars):
            amplitude = abs(math.sin(moment + index * 0.62)) if is_playing else 0.08
            height = int(5 + amplitude * 36)
            bar.configure(height=height, fg_color="#22C55E" if is_playing else "#3B82F6")
            bar.place_configure(y=44)

    def _on_space(self, event) -> str:
        self.toggle_play_pause()
        return "break"

    def _on_next(self, event) -> str:
        self.library.next_music()
        return "break"

    def _on_previous(self, event) -> str:
        self.library.previous_music()
        return "break"

    @staticmethod
    def _format_time(seconds: float) -> str:
        seconds = max(0, int(seconds))
        return f"{seconds // 60:02d}:{seconds % 60:02d}"
