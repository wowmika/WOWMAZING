# WOWMAZING v1.0 Release Candidate

## Highlights

- Download media as MP3 or MP4, with queued jobs, progress, and cancellation.
- Browse local downloads, search, favorite tracks, and maintain playlists.
- Play music with seeking, shuffle, repeat, mini-player controls, and smart playlists.
- Configure download location, audio quality, startup page, and theme.

## Packaging

- Windows executable built with PyInstaller using `build.spec`.
- Runtime data is stored outside the bundled application resources.

## Known requirements

- FFmpeg must be installed and available on `PATH` for yt-dlp audio conversion and video merging.
