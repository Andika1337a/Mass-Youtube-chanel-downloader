# Mass-Youtube-chanel-downloader

# Contoh penggunaan
channel_url = "https://www.youtube.com/@NamaChannel"  # Ganti dengan URL channel YouTube
download_channel_videos(channel_url, output_path="youtube_channel_downloads")
```

---

### Fitur Skrip:
1. **Mengambil Daftar Video dari Channel**:
   - Skrip menggunakan playlist upload channel untuk mendapatkan semua video yang tersedia.

2. **Mengunduh Video dalam Resolusi Tertinggi**:
   - Setiap video akan diunduh dengan resolusi tertinggi yang tersedia.

3. **Membuat Folder Unduhan**:
   - Jika folder output belum ada, skrip akan membuatnya secara otomatis.

4. **Menangani Kesalahan**:
   - Jika terjadi kesalahan saat mengunduh atau mengambil daftar video, skrip akan mencatat pesan kesalahan dan melanjutkan.

---

### Cara Menggunakan:
1. **Install Library `pytube`**:
   Jalankan perintah berikut untuk menginstall library `pytube`:
   ```bash
   pip install pytube
   ```

2. **Siapkan URL Channel**:
   - Ganti `channel_url` dengan URL channel YouTube yang ingin Anda unduh videonya.
   - Contoh:
     ```python
     channel_url = "https://www.youtube.com/@NamaChannel"
     ```

3. **Jalankan Skrip**:
   - Simpan skrip di file Python, misalnya `youtube_channel_downloader.py`.
   - Jalankan skrip dengan perintah:
     ```bash
     python youtube_channel_downloader.py
     ```

4. **Cek Hasil Unduhan**:
   - Video yang berhasil diunduh akan disimpan di folder `youtube_channel_downloads` (atau folder lain yang Anda tentukan).

---
