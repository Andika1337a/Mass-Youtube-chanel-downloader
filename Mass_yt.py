from pytube import YouTube, Playlist
import os

def download_video(url, output_path="downloads"):
    """
    Mengunduh satu video YouTube.
    """
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()  # Pilih resolusi tertinggi
        print(f"Mengunduh: {yt.title}")
        stream.download(output_path)
        print(f"Unduhan selesai: {yt.title}")
    except Exception as e:
        print(f"Gagal mengunduh {url}: {e}")

def get_channel_videos(channel_url):
    """
    Mengambil daftar video dari channel YouTube menggunakan playlist upload.
    """
    try:
        # Gunakan playlist upload channel untuk mendapatkan semua video
        playlist = Playlist(channel_url + "/videos")
        return playlist.video_urls
    except Exception as e:
        print(f"Gagal mengambil daftar video: {e}")
        return []

def download_channel_videos(channel_url, output_path="channel_downloads"):
    """
    Mengunduh semua video dari channel YouTube.
    """
    if not os.path.exists(output_path):
        os.makedirs(output_path)  # Buat folder unduhan jika belum ada

    video_urls = get_channel_videos(channel_url)
    if not video_urls:
        print("Tidak ada video yang ditemukan di channel ini.")
        return

    print(f"Menemukan {len(video_urls)} video di channel.")
    for url in video_urls:
        download_video(url, output_path)

# Contoh penggunaan
channel_url = "https://www.youtube.com/@NamaChannel"  # Ganti dengan URL channel YouTube
download_channel_videos(channel_url, output_path="youtube_channel_downloads")
