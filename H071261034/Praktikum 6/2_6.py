def daftar_kandidat():
    kandidat = set()
    print("--- FASE PENDAFTARAN KANDIDAT ---")
    while True:
        nama = input("Masukkan nama kandidat (kosongkan untuk selesai): ").strip()
        if nama == "":
            if len(kandidat) < 2:
                print("Minimal harus ada 2 kandidat!")
                continue
            break
        nama = nama.capitalize()
        
     
        kandidat.add(nama)
        print(f"'{nama}' berhasil didaftarkan sebagai kandidat!")
    print("Kandidat terdaftar:", (kandidat))
    return kandidat


def pemungutan_suara(kandidat):
    suara = {}  # {nama_pemilih: kandidat_yang_dipilih}
    print("\n--- FASE PEMUNGUTAN SUARA ---")
    while True:
        pemilih = input("Nama pemilih (kosongkan untuk selesai): ").strip().lower()
        if pemilih == "":
            break
        if pemilih in suara:
            print(f"'{pemilih}' sudah memberikan suara! Suara tidak dicatat.")
            continue
        print("Kandidat yang tersedia:", sorted(kandidat))
        pilihan = input("Pilih kandidat: ").strip().capitalize()
        if pilihan not in kandidat:
            print(f"Error: '{pilihan}' tidak ada dalam daftar kandidat! Suara tidak dicatat.")
            continue
        suara[pemilih] = pilihan
        print(f"Suara '{pemilih}' untuk '{pilihan}' berhasil dicatat!")
    return suara


def hitung_hasil(kandidat, suara):
    hitungan = {k: 0 for k in sorted(kandidat)}
    for pilihan in suara.values():
        hitungan[pilihan] += 1

    print("\n" + "=" * 40)
    print("HASIL PEMILIHAN KETUA KELAS")
    print("=" * 40)
    for k, jumlah in hitungan.items():
        print(f"{k}: {jumlah} suara")
    print(f"\nTotal suara masuk: {len(suara)}")

    if len(suara) == 0:
        print("Tidak ada suara masuk. Pemilihan ulang diperlukan!")
        return

    tertinggi = max(hitungan.values())
    pemenang = [k for k, v in hitungan.items() if v == tertinggi]

    if len(pemenang) == 1:
        print(f"PEMENANG: {pemenang[0]} dengan {tertinggi} suara!")
    else:
        print(f"Hasil SERI antara: {', '.join(pemenang)} ({tertinggi} suara)")
        print("Perlu dilakukan pemilihan ulang!")
    print("=" * 40)


def main():
    print("=" * 40)
    print("SISTEM PEMILIHAN KETUA KELAS")
    print("=" * 40)
    kandidat = daftar_kandidat()
    suara = pemungutan_suara(kandidat)
    hitung_hasil(kandidat, suara)


if __name__ == "__main__":
    main()