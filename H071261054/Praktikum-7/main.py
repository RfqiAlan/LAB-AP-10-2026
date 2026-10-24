from TP7_1_H071261054 import *
from TP7_2_H071261054 import tampilkan_invoice 
from TP7_3_H071261054 import riwayat_transaksi

print("=" * 50)
print(" " * 17 + "SELAMAT DATANG")
print("=" * 50)

nama_kasir = input("Masukkan Nama Kasir : ").title()

while True:
    print("=" * 50)
    print("Pilih Opsi : ")
    print("1. Transaksi Baru")
    print("2. Cari Transaksi")
    print("3. Keluar")
    print("=" * 50)

    pilihan = input("Masukkan Pilihan (1-3): ")

    if pilihan == "1":
        keranjang = []
        while True:
            data_produk = tambah_produk()
            keranjang.append(data_produk)
            tambah_lagi = input("Tambah Produk Lain? (y/n) : ").lower()
            if tambah_lagi != "y":
                break
        
        file, waktu, total = create_invoice(keranjang, nama_kasir)
        riwayat_transaksi(file, waktu, total)
            
    elif pilihan == "2":
        id_transaksi = input("Masukkan ID Transaksi : \n")
        isi_invoice = tampilkan_invoice(id_transaksi)
        print(isi_invoice)
    elif pilihan == "3":
        print("\nTerima kasih, program selesai.")
        break
    else:
        print("\nPilihan tidak valid, silakan masukkan angka 1-3.")