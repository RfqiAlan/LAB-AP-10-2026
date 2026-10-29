import os
import random
from datetime import datetime

GARIS = "=" * 50

# Buat folder "invoices" kalau belum ada
if not os.path.exists("invoices"):
    os.mkdir("invoices")


def tanya(label):
    # Menampilkan pertanyaan dengan titik dua yang sejajar
    return input(label.ljust(25) + ": ")


##############################################
# 1. TRANSAKSI BARU (MEMBUAT INVOICE)
##############################################
def transaksi_baru(nama_kasir):
    daftar_produk = []
    total = 0

    while True:
        nama = tanya("Masukkan nama produk")
        harga = int(tanya("Masukkan harga produk"))
        jumlah = int(tanya("Masukkan jumlah produk"))

        subtotal = harga * jumlah
        total = total + subtotal
        daftar_produk.append((nama, harga, jumlah, subtotal))

        print(GARIS)
        lagi = tanya("Tambah produk? (y/t)")
        print(GARIS)
        if lagi != "y":
            break

    # --- Membuat ID transaksi ---
    sekarang = datetime.now()
    inisial = nama_kasir[0].upper()
    tanggal = sekarang.strftime("%Y%m%d")
    jam = sekarang.strftime("%H%M")
    acak = random.randint(100, 999)
    id_transaksi = inisial + tanggal + jam + str(acak)
    waktu_lengkap = sekarang.strftime("%Y-%m-%d %H:%M:%S")

    
    file_invoice = open("invoices/" + id_transaksi + ".txt", "w")
    file_invoice.write(GARIS + "\n")
    file_invoice.write("INVOICE".center(50) + "\n")
    file_invoice.write(GARIS + "\n")
    file_invoice.write("ID Transaksi : " + id_transaksi + "\n")
    file_invoice.write("Waktu        : " + waktu_lengkap + "\n")
    file_invoice.write("Kasir        : " + nama_kasir + "\n")
    file_invoice.write(GARIS + "\n")
    for produk in daftar_produk:
        file_invoice.write(produk[0] + " | " + str(produk[1]) + " x " + str(produk[2]) + " = " + str(produk[3]) + "\n")
    file_invoice.write(GARIS + "\n")
    file_invoice.write("TOTAL : Rp. " + str(total) + "\n")
    file_invoice.close()

    # --- Catat ke riwayat transaksi (lihat bagian 3) ---
    catat_riwayat(waktu_lengkap, id_transaksi, total)

    print("TRANSAKSI BERHASIL".center(50))
    print(GARIS)


##############################################
# 2. CARI TRANSAKSI (MENAMPILKAN INVOICE)
##############################################
def cari_transaksi():
    cari_id = tanya("Masukkan ID transaksi")
    print(GARIS)
    lokasi_file = "invoices/" + cari_id.replace("#", "") + ".txt"

    if os.path.exists(lokasi_file):
        file_invoice = open(lokasi_file, "r")
        print(file_invoice.read())
        file_invoice.close()
    else:
        print("Invoice tidak ditemukan.")
    print(GARIS)


##############################################
# 3. RIWAYAT TRANSAKSI (trx_history.txt)
##############################################
def catat_riwayat(waktu, id_transaksi, total):
    # Kalau file belum ada, tulis judul tabel dulu
    if not os.path.exists("trx_history.txt"):
        riwayat = open("trx_history.txt", "w")
        riwayat.write(GARIS + "\n")
        riwayat.write("| Waktu               | ID Transaksi      | Nominal Transaksi |\n")
        riwayat.write(GARIS + "\n")
        riwayat.close()

    # Tambahkan satu baris untuk transaksi ini
    riwayat = open("trx_history.txt", "a")   # "a" = tambah baris baru di bawah
    riwayat.write("| " + waktu + " | #" + id_transaksi + " | Rp. " + str(total) + " |\n")
    riwayat.close()


##############################################
# PROGRAM UTAMA (MENU PILIH OPSI)
##############################################
print(GARIS)
print("SELAMAT DATANG".center(50))
print(GARIS)
nama_kasir = tanya("Masukkan nama kasir")
print(GARIS)

while True:
    print("Pilih opsi:")
    print("1. Transaksi baru")
    print("2. Cari transaksi")
    print("3. Keluar")
    print(GARIS)
    pilihan = tanya("Masukkan opsi pilihan")
    print(GARIS)

    if pilihan == "1":
        transaksi_baru(nama_kasir)
    elif pilihan == "2":
        cari_transaksi()
    elif pilihan == "3":
        print("TERIMA KASIH".center(50))
        print(GARIS)
        break
    else:
        print("Opsi tidak valid.")
        print(GARIS)