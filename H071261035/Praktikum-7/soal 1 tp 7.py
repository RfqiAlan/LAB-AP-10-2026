import os
import random
from datetime import datetime


def buat_folder():
  """Membuat folder 'invoices' jika belum ada."""
  if not os.path.exists("invoices"):
    os.makedirs("invoices")


def soal_1_buat_invoice():
  buat_folder()

  print("\n=== SOAL 1: MEMBUAT INVOICE TRANSAKSI ===")
  nama_kasir = input("Masukkan Nama Kasir: ").strip()
  if not nama_kasir:
    print("Nama kasir tidak boleh kosong!")
    return

  inisial_kasir = nama_kasir[:3].upper()

  waktu_sekarang = datetime.now()
  tahun = waktu_sekarang.strftime("%y")
  bulan = waktu_sekarang.strftime("%m")
  tanggal = waktu_sekarang.strftime("%d")
  jam_menit = waktu_sekarang.strftime("%H%M")
  waktu_lengkap = waktu_sekarang.strftime("%Y-%m-%d %H:%M:%S")

  angka_acak = str(random.randint(100, 999))

  id_transaksi = (
      f"{inisial_kasir}{tahun}{bulan}{tanggal}{jam_menit}{angka_acak}"
  )

  daftar_belanja = []
  total_harga = 0

  while True:
    print("\n--- Input Produk ---")
    nama_produk = input("Nama produk (ketik 'selesai' untuk mengakhiri): ")
    if nama_produk.lower() == "selesai":
      break

    try:
      harga_produk = float(input("Harga produk (Rp): "))
      jumlah_produk = int(input("Jumlah produk yang dibeli: "))
      if harga_produk < 0 or jumlah_produk <= 0:
        print("Harga atau jumlah produk tidak valid.")
        continue
    except ValueError:
      print("Input harga atau jumlah harus berupa angka!")
      continue

    subtotal = harga_produk * jumlah_produk
    total_harga += subtotal
    daftar_belanja.append({
        "nama": nama_produk,
        "harga": harga_produk,
        "jumlah": jumlah_produk,
        "subtotal": subtotal,
    })

  if not daftar_belanja:
    print("Transaksi dibatalkan karena tidak ada produk yang diinput.")
    return

  nama_file = f"invoices/{id_transaksi}.txt"
  with open(nama_file, "w", encoding="utf-8") as f:
    f.write("=" * 40 + "\n")
    f.write("             STRUK BELANJA              \n")
    f.write("=" * 40 + "\n")
    f.write(f"ID Transaksi : {id_transaksi}\n")
    f.write(f"Waktu        : {waktu_lengkap}\n")
    f.write(f"Kasir        : {nama_kasir}\n")
    f.write("-" * 40 + "\n")
    for item in daftar_belanja:
      f.write(
          f"{item['nama']} ({item['jumlah']}x @{item['harga']:.0f})\n"
          f"  Subtotal: Rp. {item['subtotal']:.0f}\n"
      )
    f.write("-" * 40 + "\n")
    f.write(f"Total Pembayaran: Rp. {total_harga:.0f}\n")
    f.write("=" * 40 + "\n")

  print(f"\n[Sukses] Invoice berhasil dibuat dengan nama file: {id_transaksi}.txt")
  print(f"Total Belanja: Rp. {total_harga:.0f}")


if __name__ == "__main__":
  soal_1_buat_invoice()