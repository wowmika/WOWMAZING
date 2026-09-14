# PyInstaller build configuration for a Windows WOWMAZING executable.
# Build with: pyinstaller build.spec

from pathlib import Path


project_root = Path(SPECPATH)

a = Analysis(
    [str(project_root / "app.py")],
    pathex=[str(project_root)],
    binaries=[],
    datas=[],
    hiddenimports=["customtkinter", "pygame", "mutagen.mp3", "yt_dlp"],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name="WOWMAZING",
    console=False,
    debug=False,
    strip=False,
    upx=True,
)
