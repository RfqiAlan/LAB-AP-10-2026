import os


def soal_3_catat_dan_lihat_riwayat(waktu, id_transaksi, nominal):
  """Fungsi untuk mencatat riwayat transaksi baru ke file trx_history.txt"""
  file_riwayat = "trx_history.txt"
  file_baru = not os.path.exists(file_riwayat)

  with open(file_riwayat, "a", encoding="utf-8") as f:
    if file_baru:
      f.write(
          "=" * 65 + "\n"
          f"| {'Waktu':<19} | {'ID Transaksi':<16} | {'Nominal Transaksi':<18} |\n"
          + "=" * 65 + "\n"
      )
    f.write(
        f"| {waktu:<19} | {id_transaksi:<16} | Rp. {nominal:<14.0f} |\n"
        + "=" * 65 + "\n"
    )


def soal_3_tampilkan_riwayat():
  """Fungsi untuk menampilkan riwayat transaksi kepada pemilik toko."""
  file_riwayat = "trx_history.txt"
  print("\n=== SOAL 3: RIWAYAT TRANSAKSI PEMILIK TOKO ===")
  if os.path.exists(file_riwayat):
    with open(file_riwayat, "r", encoding="utf-8") as f:
      print(f.read())
  else:
    print(
        "Belum ada riwayat transaksi yang tercatat (file trx_history.txt belum"
        " ada)."
    )


if __name__ == "__main__":
  soal_3_tampilkan_riwayat()