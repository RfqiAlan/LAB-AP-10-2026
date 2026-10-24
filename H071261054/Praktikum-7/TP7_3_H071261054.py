import os

def riwayat_transaksi(id, waktu, total_bayar):
    nama_file = "trx_history.txt"
    lebar_total = 68
    garis_ganda = "=" * lebar_total + "\n"
    garis_putus = "-" * lebar_total + "\n"
    
    file_baru = not os.path.exists(nama_file) or os.path.getsize(nama_file) == 0
    
    with open(nama_file, "a") as f:
        if file_baru:
            f.write(garis_ganda)
            f.write(f"|{'RIWAYAT TRANSAKSI':^{lebar_total - 2}}|\n")
            f.write(garis_putus)
            f.write(f"| {'Waktu':^18} | {'ID Transaksi':^20} | {'Nominal Transaksi':^20} |\n")
            f.write(garis_putus)

        txt_nominal = f"Rp{total_bayar}"
        f.write(f"| {waktu:<18} | {id:<20} | {txt_nominal:>20} |\n")
        f.write(garis_ganda)

    print("Transaksi baru berhasil ditambahkan ke riwayat!")