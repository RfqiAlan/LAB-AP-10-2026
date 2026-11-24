import os


def soal_2_cari_invoice():
  print("\n=== SOAL 2: MENCARI DAN MENAMPILKAN INVOICE ===")
  id_input = input(
      "Masukkan ID Transaksi (contoh: KLS2308291250123): "
  ).strip()

  nama_file = f"invoices/{id_input}.txt"

  if os.path.exists(nama_file):
    print(f"\n--- Isi Invoice untuk ID: {id_input} ---")
    with open(nama_file, "r", encoding="utf-8") as f:
      print(f.read())
  else:
    print(
        f"\n[Error] Invoice dengan ID '{id_input}' tidak ditemukan di folder"
        " invoices."
    )


if __name__ == "__main__":
  soal_2_cari_invoice()