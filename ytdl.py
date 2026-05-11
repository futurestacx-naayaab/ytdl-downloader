import yt_dlp
import os

def download_video_assets():
    url = input("\n[?] Paste the YouTube URL: ").strip()
    if not url: return

    # Save in the same folder as this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(script_dir, '%(title)s_%(resolution)s.%(ext)s')

    ydl_opts = {
        # 'bestvideo' ensures no audio is downloaded
        'format': 'bestvideo',
        
        # Priority: 4K/2K -> 1080p -> H.264 codec (Best for DaVinci Resolve)
        'format_sort': ['res:2160', 'res:1080', 'codec:h264'],
        
        'outtmpl': output_path,
        
        # --- THE FIX FOR THE ERROR ---
        # It must be a dictionary, not a list.
        'js_runtimes': {
            'node': {}  # Telling it to use the system's Node.js
        }, 
        
        # Converts the final file to MP4 if it's WebM/VP9
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
        
        'noplaylist': True,
        'quiet': False,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print(f"\n[+] Folder: {script_dir}")
            print(f"[+] Using Node.js to solve YouTube JS signatures...")
            ydl.download([url])
            print(f"\n[D] Success! High-res video ready for editing.")
    except Exception as e:
        print(f"\n[X] Error: {e}")

if __name__ == "__main__":
    download_video_assets()