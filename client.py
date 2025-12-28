import socket
import os
from datetime import datetime

SERVER_IP = "192.168.1.10"
PORT = 8888
BUFFER_SIZE = 4096
BASE_DIR = "File"
FILENAME = "gambar.png"

try:
    # Informasi Awal
    print("=== CLIENT FILE TRANSFER ===")
    print(f"Waktu mulai : {datetime.now()}")

    # Setup Socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER_IP, PORT))
    print("Berhasil terhubung ke server")

    # Terima metadata
    buffer = b""
    while b"\n" not in buffer:
        buffer += client.recv(1)

    # Parsing Metadata
    metadata = buffer.decode().strip()
    filename, file_size = metadata.split("|")
    file_size = int(file_size)

    # Ubah nama file
    name, ext = os.path.splitext(FILENAME)
    new_filename = f"{name}_terkirim{ext}"

    # Tentukan folder tujuan
    if not os.path.exists(BASE_DIR):
        os.makedirs(BASE_DIR)
    save_path = os.path.join(BASE_DIR, new_filename)

    # Terima File
    received_size = 0
    with open(save_path, "wb") as f:
        while received_size < file_size:
            data = client.recv(BUFFER_SIZE)
            if not data:
                break
            f.write(data)
            received_size += len(data)

            # Progress Bar
            percent = (received_size / file_size) * 100
            print(f"\rProgress terima: {percent:.2f}%", end="")
    print("\nTransfer selesai.")

    # Validasi File
    if received_size == file_size:
        print("Validasi: File diterima lengkap.")
    else:
        print("Validasi: File TIDAK lengkap.")

    # Informasi Akhir
    print(f"Disimpan sebagai: {save_path}")
    print(f"Waktu selesai : {datetime.now()}")

    # Tutup Koneksi
    client.close()

# Tangkap Error
except ConnectionRefusedError:
    print("Gagal terhubung ke server. Pastikan server sudah berjalan.")
except socket.error as e:
    print("Socket error:", e)

# except Exception as e:
#     print("Gagal terhubung ke server:", e)
