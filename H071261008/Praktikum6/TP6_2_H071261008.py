def daftar_kandidat(kandidat_set, nama):
    nama = nama.capitalize()
    if nama in kandidat_set:
        print(f"'{nama}' sudah terdaftar!")
    else:
        kandidat_set.add(nama)
        print(f"'{nama}' berhasil didaftarkan sebagai kandidat!")

def berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan):
    pemilih = nama_pemilih.lower()
    pilihan = pilihan.capitalize()
    if pemilih in rekap_suara:
        print(f"'{nama_pemilih.capitalize()}' sudah memberikan suara sebelumnya!")
    elif pilihan not in kandidat_set:
        print(f"Error: kandidat '{pilihan}' tidak ada!")
    else:
        rekap_suara[pemilih] = pilihan
        print(f"Suara '{nama_pemilih.capitalize()}' untuk '{pilihan}' berhasil dicatat!")

def hitung_suara(rekap_suara, kandidat_set):
    perolehan = {}
    for k in sorted(kandidat_set):
        perolehan[k] = 0
    for pilihan in rekap_suara.values():
        perolehan[pilihan] += 1
    return perolehan

def tampilkan_hasil(perolehan):
    print("=" * 40)
    print(" HASIL PEMILIHAN KETUA KELAS")
    print("=" * 40)
    for k, jumlah in perolehan.items():
        print(f" {k}: {jumlah} suara")
    print(f"Total suara masuk: {sum(perolehan.values())}")
    tertinggi = max(perolehan.values())
    pemenang = [k for k, v in perolehan.items() if v == tertinggi]
    if len(pemenang) > 1:
        print("Hasil SERI antara:", ", ".join(pemenang))
        print("Perlu dilakukan pemilihan ulang!")
    else:
        print(f"PEMENANG: {pemenang[0]} dengan {tertinggi} suara!")
    print("=" * 40)

kandidat_set = set()
rekap_suara = {}

print("=" * 40)
print(" SISTEM PEMILIHAN KETUA KELAS")
print("=" * 40)

print("--- FASE PENDAFTARAN KANDIDAT ---")
while True:
    nama = input("Masukkan nama kandidat (kosongkan untuk selesai): ").strip()
    if nama == "":
        if len(kandidat_set) < 2:
            print("Minimal harus ada 2 kandidat!")
        else:
            break
    else:
        daftar_kandidat(kandidat_set, nama)
print("Kandidat terdaftar:", kandidat_set)

print("--- FASE PEMUNGUTAN SUARA ---")
while True:
    nama_pemilih = input("Nama pemilih (kosongkan untuk selesai): ").strip()
    if nama_pemilih == "":
        break
    print("Kandidat yang tersedia:", kandidat_set)
    pilihan = input("Pilih kandidat: ").strip()
    berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan)

perolehan = hitung_suara(rekap_suara, kandidat_set)
tampilkan_hasil(perolehan)