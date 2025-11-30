# 📡 PROYEK AKHIR – KOMUNIKASI DATA

Implementasi Sistem Pengiriman File Antar Komputer (Client–Server)

Proyek ini dibuat untuk memenuhi tugas akhir mata kuliah **Komunikasi Data**.  
Tujuan utamanya adalah membuat sistem sederhana yang dapat **mengirim file gambar dari satu komputer ke komputer lain melalui jaringan lokal (LAN)** menggunakan Python.

## 🧾 Informasi Mata Kuliah

- **Mata Kuliah:** Praktikum Komunikasi Data
- **Dosen Pengampu:** Rian Rahmanda Putra, S.Kom., M.Kom
- **Durasi Pengerjaan:** Maksimal 3 minggu
- **Durasi Presentasi:** 10 menit per kelompok
- **Sifat Ujian:** Terbuka (menggunakan komputer)
- **Maksimal Anggota Kelompok:** 2 orang

## 👥 Anggota Kelompok

| Nama                    | Peran     |
| ----------------------- | --------- |
| **A. Hanif Nursyabana** | Developer |
| **Alhakim**             | Developer |

## 📌 Petunjuk Umum Proyek

- Kerjakan secara berkelompok dan pahami seluruh bagian sistem.
- Setiap anggota harus mengerti apa yang dikerjakan tim.
- Gunakan **Python 3.x** untuk pemrograman.
- Wajib menggunakan **dua komputer fisik yang berbeda** dan terhubung ke jaringan lokal yang sama.
- Presentasi wajib dilakukan oleh seluruh anggota tim.

## 📡 Skenario Proyek

Tim diminta membuat sistem yang dapat:

### **📤 Mengirim file gambar dari komputer SERVER ke komputer CLIENT melalui jaringan lokal.**

Dengan aturan jaringan berikut:

- **Alamat Jaringan:** `192.168.1.0/24`
- **IP SERVER:** `192.168.1.10`
- **IP CLIENT:** `192.168.1.20`
- **Port Komunikasi:** `8888`

File yang dikirim harus berupa **gambar (JPG/PNG)** berukuran minimal **1 MB**.

## 🛠 Teknologi & Library

- **Python 3.x**
- `socket` (untuk komunikasi TCP)
- `os` (untuk membaca ukuran file, dsb.)
- `threading` (opsional, untuk handling parallel)
- `time` (opsional, untuk logging transfer)

## 🧪 Pengujian yang Diharapkan

- Pengiriman file minimal 1 MB
- Waktu pengiriman tercatat (opsional)
- File diterima utuh tanpa korupsi
- Keduanya berjalan dalam satu jaringan LAN yang sama

## 📊 Hasil

- Screenshot server & client
- Latency
- Kecepatan transfer
- Hasil pengujian berbagai ukuran file

## 📜 Lisensi

Proyek ini dibuat untuk kepentingan akademik dan tidak untuk penggunaan komersial.
