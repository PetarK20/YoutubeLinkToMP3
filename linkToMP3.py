import os
from tkinter import Tk, filedialog
from yt_dlp import YoutubeDL

# === Избиране на папка ===
root = Tk()
root.withdraw() 
output_folder = r"C:..................."

if not output_folder:
    print("❌ Не е избрана папка. Програмата спира.")
    exit()

# === YouTube линкове ===
youtube_links = [
 
    # === links ===

]

# === Настройки за сваляне ===
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'ffmpeg_location': r"C:...................",
    'noplaylist': True  # ТОВА е важно
}

# === Изтегляне ===
with YoutubeDL(ydl_opts) as ydl:
    for url in youtube_links:
        print(f"▶️ Свалям: {url}")
        ydl.download([url])

print(f"\n✅ MP3 файловете са запазени в: {output_folder}")

