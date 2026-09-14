"""Persisted application preferences."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path

from core.paths import app_data_path


VALID_QUALITIES = {"128", "192", "320"}
VALID_STARTUP_PAGES = {"home", "download", "library", "settings"}
VALID_THEMES = {"Dark", "Light", "System"}


@dataclass
class AppSettings:
    download_location: str
    audio_quality: str = "192"
    startup_page: str = "home"
    theme: str = "Dark"


class SettingsStore:
    """Loads and saves settings to database/settings.json."""

    def __init__(self, path: Path | None = None) -> None:
        self.path = path or app_data_path("database/settings.json")
        self.settings = self._load()

    def save(self, settings: AppSettings) -> None:
        self._validate(settings)
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("w", encoding="utf-8") as file:
            json.dump(asdict(settings), file, indent=2)
        self.settings = settings

    def update(self, **changes: str) -> AppSettings:
        updated = AppSettings(**{**asdict(self.settings), **changes})
        self.save(updated)
        return updated

    def _load(self) -> AppSettings:
        defaults = AppSettings(download_location=str(app_data_path("downloads")))
        if not self.path.exists():
            return defaults
        try:
            with self.path.open("r", encoding="utf-8") as file:
                raw_settings = json.load(file)
            settings = AppSettings(**{**asdict(defaults), **raw_settings})
            self._validate(settings)
            return settings
        except (OSError, TypeError, ValueError, json.JSONDecodeError):
            return defaults

    @staticmethod
    def _validate(settings: AppSettings) -> None:
        if settings.audio_quality not in VALID_QUALITIES:
            raise ValueError("Unsupported audio quality.")
        if settings.startup_page not in VALID_STARTUP_PAGES:
            raise ValueError("Unsupported startup page.")
        if settings.theme not in VALID_THEMES:
            raise ValueError("Unsupported theme.")
