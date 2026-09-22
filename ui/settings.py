"""Application preferences and product information."""

from __future__ import annotations

import webbrowser
from collections.abc import Callable
from tkinter import filedialog

import customtkinter as ctk

from core.settings import AppSettings, SettingsStore
from core.theme import TEXT, TEXT_SECONDARY


class SettingsPage(ctk.CTkFrame):
    def __init__(
        self,
        master,
        settings_store: SettingsStore,
        on_settings_saved: Callable[[AppSettings], None],
    ) -> None:
        super().__init__(master)
        self.settings_store = settings_store
        self.on_settings_saved = on_settings_saved
        settings = settings_store.settings

        ctk.CTkLabel(
            self,
            text="⚙ Settings",
            font=("Segoe UI", 30, "bold"),
            text_color=TEXT,
        ).pack(anchor="w", padx=60, pady=(38, 8))
        ctk.CTkLabel(
            self,
            text="Personalize your WOWMAZING experience.",
            font=("Segoe UI", 14),
            text_color=TEXT_SECONDARY,
        ).pack(anchor="w", padx=60, pady=(0, 25))

        panel = ctk.CTkFrame(self)
        panel.pack(fill="x", padx=60, pady=5)

        self._section_label(panel, "Download location")
        location_row = ctk.CTkFrame(panel, fg_color="transparent")
        location_row.pack(fill="x", padx=22, pady=(0, 20))
        self.download_location = ctk.CTkEntry(location_row, height=38)
        self.download_location.insert(0, settings.download_location)
        self.download_location.pack(side="left", fill="x", expand=True, padx=(0, 10))
        ctk.CTkButton(location_row, text="Browse…", width=95, command=self.choose_location).pack(side="right")

        self._section_label(panel, "Preferred audio quality")
        self.quality_option = ctk.CTkOptionMenu(panel, values=["128", "192", "320"])
        self.quality_option.set(settings.audio_quality)
        self.quality_option.pack(anchor="w", padx=22, pady=(0, 20))

        self._section_label(panel, "Default startup page")
        self.startup_option = ctk.CTkOptionMenu(panel, values=["Home", "Download", "Library", "Settings"])
        self.startup_option.set(settings.startup_page.title())
        self.startup_option.pack(anchor="w", padx=22, pady=(0, 20))

        self._section_label(panel, "Theme")
        self.theme_option = ctk.CTkOptionMenu(panel, values=["Dark", "Light", "System"])
        self.theme_option.set(settings.theme)
        self.theme_option.pack(anchor="w", padx=22, pady=(0, 25))

        actions = ctk.CTkFrame(self, fg_color="transparent")
        actions.pack(fill="x", padx=60, pady=(20, 10))
        ctk.CTkButton(actions, text="Save settings", width=155, height=40, command=self.save_settings).pack(side="left")
        ctk.CTkButton(
            actions,
            text="About WOWMAZING",
            width=155,
            height=40,
            fg_color="#333333",
            command=self.show_about,
        ).pack(side="left", padx=12)
        self.status_label = ctk.CTkLabel(actions, text="", text_color="#22C55E")
        self.status_label.pack(side="left", padx=8)

    @staticmethod
    def _section_label(master, text: str) -> None:
        ctk.CTkLabel(master, text=text, font=("Segoe UI", 14, "bold"), text_color=TEXT).pack(
            anchor="w", padx=22, pady=(20, 7)
        )

    def choose_location(self) -> None:
        selected = filedialog.askdirectory(initialdir=self.download_location.get() or None)
        if selected:
            self.download_location.delete(0, "end")
            self.download_location.insert(0, selected)

    def save_settings(self) -> None:
        location = self.download_location.get().strip()
        if not location:
            self.status_label.configure(text="Choose a download location.", text_color="#EF4444")
            return
        settings = self.settings_store.update(
            download_location=location,
            audio_quality=self.quality_option.get(),
            startup_page=self.startup_option.get().lower(),
            theme=self.theme_option.get(),
        )
        self.on_settings_saved(settings)
        self.status_label.configure(text="Saved", text_color="#22C55E")

    def show_about(self) -> None:
        dialog = ctk.CTkToplevel(self)
        dialog.title("About WOWMAZING")
        dialog.geometry("410x250")
        dialog.resizable(False, False)
        dialog.transient(self.winfo_toplevel())
        dialog.grab_set()
        ctk.CTkLabel(dialog, text="WOWMAZING", font=("Segoe UI", 27, "bold"), text_color="#22C55E").pack(pady=(30, 4))
        ctk.CTkLabel(dialog, text="Version 1.0.0", font=("Segoe UI", 14)).pack(pady=3)
        ctk.CTkLabel(dialog, text="Developed by WOWMIKA", font=("Segoe UI", 14)).pack(pady=3)
        ctk.CTkLabel(dialog, text="github.com/wowmika/WOWMAZING", font=("Segoe UI", 13), text_color=TEXT_SECONDARY).pack(pady=(12, 8))
        ctk.CTkButton(
            dialog,
            text="Open GitHub",
            command=lambda: webbrowser.open("https://github.com/wowmika/WOWMAZING"),
        ).pack(pady=7)
