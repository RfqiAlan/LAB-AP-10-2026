def daftar_kandidat(kandidat_set, nama):
    nama_clean = nama.strip().capitalize()
    if nama_clean in kandidat_set:
        print(f"'{nama_clean}' sudah terdaftar sebagai kandidat!")
    else:
        kandidat_set.add(nama_clean)
        print(f"'{nama_clean}' berhasil didaftarkan sebagai kandidat!")

def berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan):
    pemilih_lower = nama_pemilih.strip().lower()
    pilihan_clean = pilihan.strip().capitalize()
    
    if pemilih_lower in rekap_suara:
        print(f"'{nama_pemilih}' sudah memberikan suara sebelumnya!")
        return
        
    if pilihan_clean not in kandidat_set:
        print(f"Error: Kandidat '{pilihan}' tidak ada dalam daftar kandidat!")
        return
        
    rekap_suara[pemilih_lower] = pilihan_clean
    print(f"Suara '{nama_pemilih}' untuk '{pilihan_clean}' berhasil dicatat!")

def hitung_suara(rekap_suara, kandidat_set):
    perolehan = {}
    for kandidat in kandidat_set:
        perolehan[kandidat] = 0
        
    for pemilih, kandidat_dipilih in rekap_suara.items():
        if kandidat_dipilih in perolehan:
            perolehan[kandidat_dipilih] += 1
            
    return perolehan

def tampilkan_hasil(perolehan):
    print("\n===================================")
    print("HASIL PEMILIHAN KETUA KELAS")
    print("===================================")
    
    total_suara = 0
    max_suara = -1
    
    for kandidat, jumlah in perolehan.items():
        print(f"{kandidat}: {jumlah} suara")
        total_suara += jumlah
        if jumlah > max_suara:
            max_suara = jumlah
            
    print(f"Total suara masuk: {total_suara}")
    
    pemenang = []
    for kandidat, jumlah in perolehan.items():
        if jumlah == max_suara and max_suara > 0:
            pemenang.append(kandidat)
            
    if len(pemenang) == 1:
        print(f"PEMENANG: {pemenang[0]} dengan {max_suara} suara!")
    elif len(pemenang) > 1:
        daftar_pemenang = ", ".join(pemenang)
        print(f"Hasil SERI antara: {daftar_pemenang}")
        print("Perlu dilakukan pemilihan ulang!")
    else:
        print("Tidak ada suara yang masuk.")
    print("===================================")

kandidat_set = set()
rekap_suara = {}

print("===================================")
print("SISTEM PEMILIHAN KETUA KELAS")
print("===================================")

print("\nFASE PENDAFTARAN KANDIDAT")
while True:
    nama = input("Masukkan nama kandidat (kosongkan untuk selesai): ")
    if nama.strip() == "":
        if len(kandidat_set) < 2:
            print("Minimal harus ada 2 kandidat sebelum bisa lanjut!")
            continue
        else:
            break
    daftar_kandidat(kandidat_set, nama)

print(f"Kandidat terdaftar: {kandidat_set}")

print("\nFASE PEMUNGUTAN SUARA")
while True:
    nama_pemilih = input("\nNama pemilih (kosongkan untuk selesai): ")
    if nama_pemilih.strip() == "":
        break
    print(f"Kandidat yang tersedia: {kandidat_set}")
    pilihan = input("Pilih kandidat: ")
    berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan)

perolehan = hitung_suara(rekap_suara, kandidat_set)
tampilkan_hasil(perolehan)