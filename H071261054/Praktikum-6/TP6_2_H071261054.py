daftar_kandidat = set()
rekap_suara = {}

print("=" * 40)
print("SISTEM PEMILIHAN KETUA KELAS")
print("=" * 40)

def daftarkan_kandidat(kandidat_set, nama):
    nama_clean = nama.strip().capitalize()
    kandidat_set.add(nama_clean)
    return nama_clean
    
def berikan_suara(rekap_suara, kandidat_set, nama_pemilih, pilihan):
    nama_pemilih_clean = nama_pemilih.strip().lower()
    pilihan_capitalize = pilihan.strip().capitalize()
    
    if nama_pemilih_clean in rekap_suara:
        print(f"Gagal! Pemilih '{nama_pemilih.strip().capitalize()}' sudah pernah memilih.")
        return False
            
    if pilihan_capitalize not in kandidat_set:
        print(f"Gagal! Kandidat '{pilihan_capitalize}' tidak ditemukan.")
        return False
    
    rekap_suara[nama_pemilih_clean] = pilihan_capitalize
    print(f"Suara dari '{nama_pemilih.strip().capitalize()}' untuk '{pilihan_capitalize}' berhasil dicatat!")
    return True

def hitung_suara(kandidat_set, rekap_suara):
    perolehan_suara = {kandidat: 0 for kandidat in kandidat_set}
    for kandidat in rekap_suara.values():
        if kandidat in perolehan_suara:
            perolehan_suara[kandidat] += 1
    
    tampilkan_hasil(perolehan_suara,rekap_suara)
    return perolehan_suara
    
def tampilkan_hasil(perolehan,rekap):
    border = "=" * 40
    print("\n" + border)
    print("HASIL PEMILIHAN KETUA KELAS".center(40))
    print(border)
    for kandidat, jumlah_suara in perolehan.items():
        print(f"{kandidat} : {jumlah_suara} suara")
            
    total_suara = len(rekap)
    print(f"Total Suara Masuk: {total_suara}")
        
    if total_suara > 0:
        suara_tertinggi = max(perolehan.values())
        pemenang = [kandidat for kandidat, suara in perolehan.items() if suara == suara_tertinggi]
        
        if len(pemenang) > 1:
            daftar_seri = ", ".join(pemenang)
            print(f"Hasil SERI antara: {daftar_seri}")
            print("Perlu dilakukan pemilihan ulang!")
        else:
            print(f"Selamat! Pemenang adalah: {pemenang[0]}")
    else:
        print("Belum ada suara yang masuk.")
    print(border)

print("\n--- FASE REGISTRASI KANDIDAT ---")

while True:
    nama_kandidat = input("Masukkan nama kandidat (Kosongkan untuk selesai) : ").strip()
    # print(nama_kandidat)
    
    if not nama_kandidat:
        if len(daftar_kandidat) < 2:
            print("Kandidat minimal 2 orang! Silakan tambahkan lagi.\n")
            continue
        else:
            break
            
    daftarkan_kandidat(daftar_kandidat, nama_kandidat)
    print(f"'{nama_kandidat.capitalize()}' berhasil ditambahkan.")

print(f"\nDaftar Kandidat Terdaftar: {daftar_kandidat}")
print("--- FASE PEMUNGUTAN SUARA ---")

while True:
    nama_pemilih = input("\nMasukkan Nama Pemilih (Kosongkan Untuk Selesaikan Voting) : ").strip()
    
    if not nama_pemilih:
        print("Pemungutan suara selesai.")
        break
        
    print(f"Kandidat Yang Tersedia : {daftar_kandidat}")
    kandidat_yang_dipilih = input("Pilih Kandidat : ").strip()
    
    berikan_suara(rekap_suara, daftar_kandidat, nama_pemilih, kandidat_yang_dipilih)

hitung_suara(daftar_kandidat, rekap_suara)