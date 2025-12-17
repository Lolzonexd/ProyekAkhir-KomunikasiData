import socket
import os
from datetime import datetime

SERVER_IP = "192.168.1.10"
PORT = 8888
BUFFER_SIZE = 4096
FILENAME = "gambar.png"

try:
    # Cek apakah file ada
    if not os.path.exists(FILENAME):
        print("Error: File tidak ditemukan!")
        exit()

    file_size = os.path.getsize(FILENAME)

    print("=== SERVER FILE TRANSFER ===")
    print(f"Waktu mulai : {datetime.now()}")
    print(f"File : {FILENAME}")
    print(f"Ukuran : {file_size} byte")

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((SERVER_IP, PORT))
    server.listen(1)

    print("Menunggu koneksi dari client...")
    conn, addr = server.accept()
    print(f"Terhubung dengan {addr}")

    # Kirim metadata (nama file + ukuran file)
    sent_size = 0
    metadata = f"{FILENAME}|{file_size}\n"
    conn.sendall(metadata.encode())

    # Kirim isi file per buffer
    with open(FILENAME, "rb") as f:
        while True:
            data = f.read(BUFFER_SIZE)
            if not data:
                break
            conn.sendall(data)
            sent_size += len(data)

            percent = (sent_size / file_size) * 100
            print(f"\rProgress kirim: {percent:.2f}%", end="")

    print("\nFile berhasil dikirim.")
    print(f"Waktu selesai : {datetime.now()}")

    conn.close()
    server.close()

except FileNotFoundError as e:
    print("Error:", e)
except socket.error as e:
    print("Socket error:", e)

# except Exception as e:
#     print("Terjadi kesalahan:", e)
