import os
import random
from datetime import datetime

if not os.path.exists("invoices"):
  os.makedirs("invoices")

HISTORY_FILE = "trx_history.txt"


def buat_inisial(nama):
  words = nama.strip().split()
  if not words:
    return "KSR"
  inisial = "".join([w[0].upper() for w in words])
  inisialnya = inisial[:3] if len(inisial) >= 1 else "KSR"
  return inisialnya

def buat_transaksi():
  print("\n" + "=" * 40)
  print("         BUAT TRANSAKSI BARU")
  print("=" * 40)
  nama_kasir = input("Masukkan Nama Kasir: ").strip()
  if not nama_kasir:
    print("Nama kasir tidak boleh kosong!")
    return

  inisial_kasir = buat_inisial(nama_kasir)

  daftar_belanja = []
  total_nominal = 0

  while True:
    nama_produk = input("Nama Produk (ketik 'selesai' jika sudah cukup): ").strip()
    if nama_produk.lower() == "selesai":
      break
    if not nama_produk:
      print("Nama produk tidak boleh kosong.")
      continue

    try:
      harga = float(input(f"Harga produk '{nama_produk}': Rp "))
      jumlah = int(input(f"Jumlah produk '{nama_produk}': "))
      if harga < 0 or jumlah <= 0:
        print("Harga tidak boleh negatif dan jumlah harus lebih dari 0.")
        continue
    except ValueError:
      print("Input harga atau jumlah harus berupa angka!")
      continue

    subtotal = harga * jumlah
    daftar_belanja.append({"nama": nama_produk, "harga": harga, "jumlah": jumlah, "subtotal": subtotal})
    total_nominal += subtotal
    print(
        f"-> Berhasil ditambahkan: {jumlah}x {nama_produk} @ Rp {harga:,.0f} ="
        f" Rp {subtotal:,.0f}\n"
    )

  if not daftar_belanja:
    print("Transaksi dibatalkan karena tidak ada produk yang diinput.")
    return


  waktu_sekarang = datetime.now()
  waktu_str = waktu_sekarang.strftime("%Y-%m-%d %H:%M:%S")

  tahun = waktu_sekarang.strftime("%y")
  bulan = waktu_sekarang.strftime("%m")
  tanggal = waktu_sekarang.strftime("%d")
  jam_menit = waktu_sekarang.strftime("%H%M")
  rand_num = str(random.randint(100, 999))

  id_transaksi = f"{inisial_kasir}{tahun}{bulan}{tanggal}{jam_menit}{rand_num}"

  invoice_content = []
  invoice_content.append("=" * 50)
  invoice_content.append("                 STRUK BELANJA TOKO                 ")
  invoice_content.append("=" * 50)
  invoice_content.append(f"ID Transaksi : {id_transaksi}")
  invoice_content.append(f"Waktu        : {waktu_str}")
  invoice_content.append(f"Kasir        : {nama_kasir}")
  invoice_content.append("-" * 50)
  invoice_content.append(f"{'Nama Produk':<22} {'Qty':<5} {'Subtotal':<20}")
  invoice_content.append("-" * 50)

  for item in daftar_belanja:
    nama_p = (item["nama"][:20] + ".." if len(item["nama"]) > 22 else item["nama"])
    invoice_content.append(f"{nama_p:<22} {item['jumlah']:<5} Rp {item['subtotal']:,.0f}")

  invoice_content.append("-" * 50)
  invoice_content.append(f"TOTAL PEMBAYARAN: Rp {total_nominal:,.0f}")
  invoice_content.append("=" * 50)
  invoice_content.append("          TERIMA KASIH TELAH BERBELANJA           ")
  invoice_content.append("=" * 50)

  text_invoice = "\n".join(invoice_content)

  file_path = os.path.join("invoices", f"{id_transaksi}.txt")
  with open(file_path, "w", encoding="utf-8") as f:
    f.write(text_invoice)

  history_exists = os.path.exists(HISTORY_FILE)
  with open(HISTORY_FILE, "a", encoding="utf-8") as f:
    if not history_exists:
      f.write(
          "=" * 70
          + "\n"
          + f"| {'Waktu':<19} | {'ID Transaksi':<18} | {'Nominal Transaksi':<20} |\n"
          + "=" * 70
          + "\n"
      )
    f.write(
        f"| {waktu_str} | {id_transaksi:<18} | Rp. {int(total_nominal):<16} |\n"
    )
    f.write("=" * 70 + "\n")

  print("\n[SUKSES] Transaksi Berhasil!")
  print(f"ID Transaksi Anda: {id_transaksi}")
  print("\nPreview Invoice:")
  print(text_invoice)


def cari_invoice():
  print("\n" + "=" * 40)
  print("          CARI INVOICE")
  print("=" * 40)
  id_cari = input("Masukkan ID Transaksi (contoh: KLS2308291250123): ").strip()
  if not id_cari:
    print("ID Transaksi tidak boleh kosong!")
    return

  file_path = os.path.join("invoices", f"{id_cari}.txt")
  if os.path.exists(file_path):
    print(f"\n[DITEMUKAN] Menampilkan Invoice untuk ID: {id_cari}\n")
    with open(file_path, "r", encoding="utf-8") as f:
      print(f.read())
  else:
    print(
        f"\n[GAGAL] Invoice dengan ID '{id_cari}' tidak ditemukan di folder"
        " 'invoices'."
    )


def lihat_riwayat():
  print("\n" + "=" * 40)
  print("         RIWAYAT TRANSAKSI")
  print("=" * 40)
  if not os.path.exists(HISTORY_FILE):
    print("Belum ada riwayat transaksi yang tercatat.")
    return

  with open(HISTORY_FILE, "r", encoding="utf-8") as f:
    print(f.read())


def main():
  while True:
    print("\n========================================")
    print("       APLIKASI KASIR SEDERHANA         ")
    print("========================================")
    print("1. Buat Transaksi Baru (Cetak Invoice)")
    print("2. Cari Invoice Berdasarkan ID")
    print("3. Lihat Riwayat Transaksi (Pemilik Toko)")
    print("4. Keluar")
    
    pilihan = input("Pilih menu (1-4): ").strip()

    if pilihan == "1":
      buat_transaksi()
    elif pilihan == "2":
      cari_invoice()
    elif pilihan == "3":
      lihat_riwayat()
    elif pilihan == "4":
      print("\nTerima kasih telah menggunakan aplikasi kasir!")
      break
    else:
      print("Pilihan tidak valid. Silakan masukkan angka 1 sampai 4.")


if __name__ == "__main__":
  main()