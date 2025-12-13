import socket
import os

SERVER_IP = "127.0.0.1"
PORT = 8888
BUFFER_SIZE = 1024

try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER_IP, PORT))
    print("Berhasil terhubung ke server")

    # Terima metadata
    metadata = client.recv(1024).decode()
    original_name, file_size = metadata.split("|")
    file_size = int(file_size)

    # Tentukan folder tujuan
    base_dir = "File"
    os.makedirs(base_dir, exist_ok=True)  # buat folder jika belum ada

    # Ubah nama file
    name, ext = os.path.splitext(original_name)
    new_filename = name + "_terkirim" + ext

    # Path lengkap: File/gambar_terkirim.png
    save_path = os.path.join(base_dir, new_filename)

    received_size = 0
    with open(save_path, "wb") as f:
        while received_size < file_size:
            data = client.recv(BUFFER_SIZE)
            if not data:
                break
            f.write(data)
            received_size += len(data)

    print(f"File berhasil diterima dan disimpan di folder '{base_dir}'")
    print(f"Nama file: {new_filename}")

    client.close()

except Exception as e:
    print("Gagal terhubung ke server:", e)
