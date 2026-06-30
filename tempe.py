import random
import string
import time
import sys

# MENGGUNAKAN CURL_CFFI AGAR TETAP AMAN DARI DETEKSI BOT CLOUDFLARE
from curl_cffi import requests 

# Mengimpor komponen tampilan dari Rich
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.live import Live
from rich.text import Text

console = Console()

# Beralih ke 1secmail API yang tidak membutuhkan pembuatan akun / token login
BASE_URL = "https://1secmail.com"

# Daftar domain resmi dari 1secmail
LIST_DOMAINS = ["1secmail.com", "1secmail.org", "1secmail.net"]

HEADERS_DEFAULT = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Accept": "application/json"
}

def generate_random_username(length=8):
    characters = string.ascii_lowercase + string.digits
    return ''.join(random.choices(characters, k=length))

def cek_kotak_masuk(username, domain):
    try:
        # Endpoint 1secmail untuk mengecek daftar pesan masuk
        url = f"{BASE_URL}?action=getMessages&login={username}&domain={domain}"
        res = requests.get(url, headers=HEADERS_DEFAULT, impersonate="chrome")
        
        if res.status_code == 200:
            return res.json()
        return []
    except Exception:
        return []

# ==========================================
# ALUR TAMPILAN UTAMA (UI LOGIC)
# ==========================================
if __name__ == "__main__":
    console.clear()
    
    banner_text = Text("1SECMAIL AUTOMATION CLIENT", style="bold white")
    console.print(Panel(banner_text, subtitle="v2.0.0 - Stable Registrationless Temp Mail", style="bold cyan", expand=False))
    
    # 1secmail tidak membutuhkan request ke server untuk mendaftar akun baru
    # Kita bisa langsung membuat alamat email acak secara instan di sisi lokal client
    username_aktif = generate_random_username(8)
    domain_aktif = random.choice(LIST_DOMAINS)
    email_address = f"{username_aktif}@{domain_aktif}"

    detail_akun = (
        f"[bold white]Alamat Email :[/] [bold green]{email_address}[/]\n\n"
        f"[dim white]Status       : Aktif & Memantau Kotak Masuk...[/]"
    )
    console.print(Panel(detail_akun, title="[bold green] Email Instan Siap Digunakan [/]", expand=False, border_style="green"))
    console.print("\n[dim cyan][*] Tekan CTRL + C untuk menghentikan program.[/]\n")

    table = Table(title="KOTAK MASUK (INBOX)", title_style="bold cyan", border_style="cyan")
    table.add_column("Waktu Pengecekan", style="dim cyan", width=20)
    table.add_column("Pengirim (From)", style="yellow", width=30)
    table.add_column("Subjek Email", style="white")

    pesan_terbaca = set()

    with Live(table, refresh_per_second=1) as live:
        try:
            while True:
                inbox = cek_kotak_masuk(username_aktif, domain_aktif)
                ada_pesan_baru = False
                
                for pesan in inbox:
                    id_pesan = pesan.get("id")
                    if id_pesan not in pesan_terbaca:
                        waktu_sekarang = time.strftime("%H:%M:%S")
                        pengirim = pesan.get('from', 'Unknown')
                        subjek = pesan.get('subject', '(Tanpa Subjek)')
                        
                        table.add_row(waktu_sekarang, pengirim, subjek)
                        pesan_terbaca.add(id_pesan)
                        ada_pesan_baru = True
                
                if ada_pesan_baru:
                    live.update(table)
                    
                time.sleep(5)
                
        except KeyboardInterrupt:
            console.print("\n[bold red][-] Program dihentikan oleh pengguna. Sampai jumpa![/]")

