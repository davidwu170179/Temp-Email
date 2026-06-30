# 📨 Tempe Mail Client (Mail.tm Clone)

Aplikasi CLI (Command Line Interface) berbasis Python untuk membuat alamat email sementara (disposable email) secara instan dan memantau kotak masuk secara *real-time* langsung dari terminal.

## ✨ Fitur Utama
- **Generasi Instan**: Membuat akun email acak secara otomatis dalam hitungan detik.
- **Live Monitoring**: Memantau kotak masuk secara *real-time* dengan sistem penyaringan otomatis agar pesan tidak ganda.
- **Bypass WAF**: Menggunakan modifikasi *Header HTTP* browser asli untuk mengurangi risiko pemblokiran otomatis oleh Cloudflare.

## 🛠️ Kebutuhan Sistem & Dependensi
- **OS**: Linux (diuji pada Ubuntu/OSBoxes), macOS, atau Windows.
- **Python**: Versi 3.10 ke atas (diuji pada Python 3.13).
- **Library**: `requests` dan `rich`.

## ⚙️ Cara Instalasi & Menjalankan

Ikuti langkah-langkah berikut untuk menjalankan proyek ini di komputer lokal atau VM Anda:

### 1. Clone Repositori Ini
```bash
git clone https://github.com
cd git_tempe
```

### 2. Buat & Aktifkan Lingkungan Virtual
Sangat disarankan untuk menggunakan `venv` agar library tidak bentrok dengan sistem global.
```bash
python3 -m venv env
source env/bin/activate
```

### 3. Instal Library yang Dibutuhkan
Instal semua dependensi yang terdaftar di dalam `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 4. Jalankan Aplikasi
Eksekusi skrip utama untuk mulai membuat email sementara:
```bash
python tempe.py
```

## 📋 Alur Kerja Aplikasi
1. **Mengambil Domain**: Skrip meminta daftar domain aktif yang tersedia dari server Mail.tm.
2. **Membuat Akun**: Sistem membuat kredensial acak (email & password) dan mendaftarkannya.
3. **Autentikasi**: Skrip menukar kredensial dengan token JWT (Bearer Token) untuk akses kotak masuk.
4. **Live Polling**: Menggunakan fitur `Live` dari library `rich` untuk mengecek dan menampilkan email masuk setiap 5 detik

## 👤 Kontributor
- **David_Wu** - *Developer Utama* - [@username-github-anda](https://github.com)

## 📄 Lisensi
Proyek ini bersifat open-source dan bebas digunakan untuk keperluan pembelajaran atau pengembangan lebih lanjut.
