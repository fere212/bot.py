import os
import subprocess
import time

# Çalıştırılacak dosyalar (sadece .py uzantılı olanlar)
files = [f for f in os.listdir() if f.endswith(".py")]

# Çalışan botları takip etmek için liste
processes = []

# Tüm botları başlat
for file in files:
    process = subprocess.Popen(["python", file])
    processes.append((file, process))

# Sürekli kontrol eden döngü
while True:
    for file, process in processes:
        if process.poll() is not None:  # Eğer bot çöktüyse
            print(f"{file} çöktü, tekrar başlatılıyor...")
            new_process = subprocess.Popen(["python", file])
            processes.append((file, new_process))
    time.sleep(5)  # 5 saniyede bir kontrol et