import socket
import os

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

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((SERVER_IP, PORT))
    server.listen(1)

    print("Menunggu koneksi dari client...")
    conn, addr = server.accept()
    print(f"Terhubung dengan {addr}")

    # Kirim metadata (nama file + ukuran file)
    metadata = f"{FILENAME}|{file_size}"
    conn.send(metadata.encode())

    # Kirim isi file per buffer
    with open(FILENAME, "rb") as f:
        while True:
            data = f.read(BUFFER_SIZE)
            if not data:
                break
            conn.sendall(data)

    print("File berhasil dikirim.")

    conn.close()
    server.close()

except Exception as e:
    print("Terjadi kesalahan:", e)
