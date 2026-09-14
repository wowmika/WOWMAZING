"""Persistent user playlists and playback-powered smart collections."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from uuid import uuid4


@dataclass(frozen=True)
class Playlist:
    """A named, ordered collection of downloaded song filenames."""

    id: str
    name: str
    created_at: str
    songs: list[str]


class PlaylistStore:
    """Manages playlists plus the local history required for smart playlists."""

    def __init__(self, path: Path | None = None) -> None:
        self.path = path or Path(__file__).resolve().parent.parent / "database" / "playlists.json"
        self._data = self._load()

    def get_playlists(self) -> list[Playlist]:
        return [Playlist(**playlist) for playlist in self._data["playlists"]]

    def get_playlist(self, playlist_id: str) -> Playlist | None:
        return next((playlist for playlist in self.get_playlists() if playlist.id == playlist_id), None)

    def create_playlist(self, name: str) -> Playlist:
        normalized_name = name.strip()
        if not normalized_name:
            raise ValueError("Playlist name cannot be empty.")
        playlist = Playlist(
            id=uuid4().hex,
            name=normalized_name,
            created_at=datetime.now(timezone.utc).isoformat(),
            songs=[],
        )
        self._data["playlists"].append(asdict(playlist))
        self._save()
        return playlist

    def rename_playlist(self, playlist_id: str, name: str) -> None:
        normalized_name = name.strip()
        if not normalized_name:
            raise ValueError("Playlist name cannot be empty.")
        playlist = self._find_mutable_playlist(playlist_id)
        playlist["name"] = normalized_name
        self._save()

    def delete_playlist(self, playlist_id: str) -> None:
        before = len(self._data["playlists"])
        self._data["playlists"] = [
            playlist for playlist in self._data["playlists"] if playlist["id"] != playlist_id
        ]
        if len(self._data["playlists"]) != before:
            self._save()

    def add_song(self, playlist_id: str, filename: str) -> None:
        playlist = self._find_mutable_playlist(playlist_id)
        if filename not in playlist["songs"]:
            playlist["songs"].append(filename)
            self._save()

    def record_play(self, filename: str) -> None:
        history = self._data["play_history"]
        if filename in history:
            history.remove(filename)
        history.insert(0, filename)
        del history[100:]
        play_counts = self._data["play_counts"]
        play_counts[filename] = int(play_counts.get(filename, 0)) + 1
        self._save()

    def recently_played(self, limit: int = 50) -> list[str]:
        return self._data["play_history"][:limit]

    def most_played(self, limit: int = 50) -> list[str]:
        counts = self._data["play_counts"]
        return sorted(counts, key=lambda filename: counts[filename], reverse=True)[:limit]

    def _find_mutable_playlist(self, playlist_id: str) -> dict[str, object]:
        playlist = next(
            (playlist for playlist in self._data["playlists"] if playlist["id"] == playlist_id),
            None,
        )
        if playlist is None:
            raise KeyError("Playlist was not found.")
        return playlist

    def _load(self) -> dict[str, object]:
        if not self.path.exists():
            return self._empty_data()
        try:
            with self.path.open("r", encoding="utf-8") as file:
                data = json.load(file)
            if not isinstance(data, dict):
                return self._empty_data()
            return {
                "playlists": data.get("playlists", []),
                "play_history": data.get("play_history", []),
                "play_counts": data.get("play_counts", {}),
            }
        except (OSError, json.JSONDecodeError):
            return self._empty_data()

    def _save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with self.path.open("w", encoding="utf-8") as file:
            json.dump(self._data, file, indent=2, ensure_ascii=False)

    @staticmethod
    def _empty_data() -> dict[str, object]:
        return {"playlists": [], "play_history": [], "play_counts": {}}
