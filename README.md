# ytdl

Small, focused utility to download high-resolution YouTube video assets suitable for editing (e.g., DaVinci Resolve).

## Disclaimer

This project is intended for educational and personal workflow purposes only.

`ytdl` is designed to help creators, editors, and students download high-quality video assets for uses such as:

* Educational content
* Commentary and criticism
* Transformative editing
* Research and analysis
* Video remixing and creative projects

Users are responsible for ensuring they comply with YouTube’s Terms of Service and all applicable copyright laws in their country.

Do not use this tool to redistribute copyrighted material without permission. If you use downloaded content, make meaningful changes or ensure your usage falls under fair use/fair dealing or other applicable legal exceptions.

This repository is provided for learning and technical demonstration purposes only.

## Overview

`ytdl.py` is a minimal Python script that uses `yt-dlp` to download the best available video (no audio) and convert WebM/VP9 outputs to MP4 for compatibility with video editors.

The script saves downloads to the same folder as `ytdl.py` using the pattern `%(title)s_%(resolution)s.%(ext)s`.

## Requirements

- Python 3.8 or newer
- pip
- System dependencies:
  - Node.js (for solving YouTube JS signatures via `js_runtimes`)
  - FFmpeg (for post-processing / conversion to MP4)

Python packages (install with `pip`):

See `requirements.txt`.

## Installation

1. (Optional) Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install Python dependencies:

```bash
pip install -r requirements.txt
```

3. Install system dependencies:

- Node.js: https://nodejs.org/ (ensure `node` is on your PATH)
- FFmpeg: https://ffmpeg.org/ (ensure `ffmpeg` is on your PATH)

On Windows you can use package managers like `scoop` or `choco` to install them, or download installers from upstream sites.

## Usage

Run the script and paste a YouTube URL when prompted:

```bash
python ytdl.py
```

The script will:
- Prompt for a YouTube URL
- Download the best video-only stream (preferring 4K/2K, then 1080p, then H.264)
- Use Node.js to resolve any JS-based signature challenges
- Convert WebM/VP9 outputs to MP4 using FFmpeg

Output is written to the same folder as `ytdl.py`.

## Configuration

You can edit `ytdl.py` to change the `outtmpl` output pattern or the `format_sort` rules if you prefer different format priorities.

## Troubleshooting

- If you see an error mentioning missing `node` or JS runtimes: install Node.js and ensure `node` is on your PATH.
- If conversion fails or `ffmpeg` is not found: install FFmpeg and ensure `ffmpeg` is on your PATH.
- For permission issues on Windows, try running the terminal as Administrator or choose an output folder where you have write access.

## Notes

- This script disables playlist downloads (`noplaylist=True`) to avoid downloading entire channels or long playlists by accident.
- The script intentionally requests video-only formats (so audio is not included). If you need combined audio+video files, change the `format` option in `ydl_opts`.

## Contributing

Small improvements and suggestions are welcome. Please open an issue or submit a PR with a focused change.

## License

This project does not include a license file. Add one if you plan to publish or share this repository publicly.
