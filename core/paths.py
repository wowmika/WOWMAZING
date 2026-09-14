"""Paths that work both from source and from a PyInstaller bundle."""

from __future__ import annotations

import sys
from pathlib import Path


def resource_path(relative_path: str) -> Path:
    """Return a read-only bundled resource path when the app is frozen."""
    base_path = Path(getattr(sys, "_MEIPASS", Path(__file__).resolve().parent.parent))
    return base_path / relative_path


def app_data_path(relative_path: str) -> Path:
    """Return the persistent application-data path used by source and builds."""
    if getattr(sys, "frozen", False):
        base_path = Path(sys.executable).resolve().parent
    else:
        base_path = Path(__file__).resolve().parent.parent
    return base_path / relative_path
