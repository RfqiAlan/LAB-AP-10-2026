def tampilkan_invoice(id_transaksi):
    lokasi = f"invoice/{id_transaksi}"
    try:
        with open(lokasi, "r") as f:
            return f.read()
    except FileNotFoundError:
        return "\n[Error] Invoice tidak ditemukan! Periksa kembali ID Transaksi."