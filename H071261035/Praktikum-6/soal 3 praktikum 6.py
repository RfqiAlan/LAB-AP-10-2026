def tambah_lagu(playlist, genre_set, judul, artis, genre, durasi):
    lagu = (judul, artis, genre, durasi)
    playlist.append(lagu)
    genre_set.add(genre)
    print(f"Lagu '{judul}' oleh {artis} berhasil ditambahkan!")

def format_durasi(detik):
    menit = detik // 60
    sisa_detik = detik % 60
    return f"{menit}:{sisa_detik:02d}"

def tampilkan_playlist(playlist):
    if len(playlist) == 0:
        print("Playlist masih kosong.")
        return
        
    print("\n=======================================================")
    print("No  Judul               Artis               Genre   Durasi")
    print("=======================================================")
    
    total_detik = 0
    nomor = 1
    for lagu in playlist:
        judul, artis, genre, durasi = lagu
        total_detik += durasi
        durasi_str = format_durasi(durasi)
        print(f"{nomor:<3} {judul:<19} {artis:<19} {genre:<7} {durasi_str}")
        nomor += 1
        
    print("=======================================================")
    total_m = total_detik // 60
    total_s = total_detik % 60
    print(f"Total durasi playlist: {total_m} menit {total_s} detik")

def filter_genre(playlist, genre_target):
    return [lagu for lagu in playlist if lagu[2].lower() == genre_target.lower()]

def hapus_lagu(playlist, nomor):
    if 1 <= nomor <= len(playlist):
        lagu_dihapus = playlist.pop(nomor - 1)
        print(f"Lagu '{lagu_dihapus[0]}' berhasil dihapus dari playlist.")
    else:
        print("Nomor lagu tidak valid!")

def statistik_playlist(playlist, genre_set):
    if len(playlist) == 0:
        print("Playlist masih kosong.")
        return
        
    print("\n==============================")
    print("STATISTIK PLAYLIST PLAYTUNE")
    print("==============================")
    print(f"Total lagu   : {len(playlist)}")
    print(f"Jumlah genre : {len(genre_set)}")
    print(f"Daftar genre : {genre_set}")
    
    # Hitung distribusi per genre
    distribusi = {}
    for lagu in playlist:
        g = lagu[2]
        if g in distribusi:
            distribusi[g] += 1
        else:
            distribusi[g] = 1
            
    print("Distribusi genre:")
    for g, jumlah in distribusi.items():
        balok = "#" * jumlah
        print(f"  {g:<8}: {balok} ({jumlah})")
        
    # Cari lagu terpanjang dan terpendek
    lagu_terpanjang = playlist[0]
    lagu_terpendek = playlist[0]
    
    for lagu in playlist:
        if lagu[3] > lagu_terpanjang[3]:
            lagu_terpanjang = lagu
        if lagu[3] < lagu_terpendek[3]:
            lagu_terpendek = lagu
            
    durasi_panjang = format_durasi(lagu_terpanjang[3])
    durasi_pendek = format_durasi(lagu_terpendek[3])
    
    print(f"Lagu terpanjang: {lagu_terpanjang[0]} ({durasi_panjang})")
    print(f"Lagu terpendek : {lagu_terpendek[0]} ({durasi_pendek})")
    print("==============================")
   
playlist = []
genre_set = set()

print("==============================")
print("PLAYLIST MUSIK PLAYTUNE")
print("==============================")

while True:
    print("\nMenu:")
    print("1. Tambah Lagu")
    print("2. Tampilkan Playlist")
    print("3. Filter berdasarkan Genre")
    print("4. Hapus Lagu")
    print("5. Statistik Playlist")
    print("6. Keluar")
    
    pilihan = input("Pilih menu (1-6): ")
    
    if pilihan == "1":
        judul = input("Judul lagu: ")
        artis = input("Artis: ")
        genre = input("Genre (Pop/Rock/Jazz/RnB/Dangdut): ")
        try:
            durasi = int(input("Durasi (dalam detik): "))
            if durasi <= 0:
                print("Durasi harus angka positif!")
            else:
                tambah_lagu(playlist, genre_set, judul, artis, genre, durasi)
        except ValueError:
            print("Durasi harus berupa angka!")
            
    elif pilihan == "2":
        tampilkan_playlist(playlist)
        
    elif pilihan == "3":
        print(f"Genre tersedia: {genre_set}")
        target = input("Masukkan genre yang ingin difilter: ")
        hasil = filter_genre(playlist, target)
        if len(hasil) == 0:
            print(f"Tidak ada lagu dengan genre '{target}'.")
        else:
            print(f"\nLagu bergenre '{target}':")
            n = 1
            for lagu in hasil:
                dur_str = format_durasi(lagu[3])
                print(f"{n}. {lagu[0]} - {lagu[1]} ({dur_str})")
                n += 1
                
    elif pilihan == "4":
        tampilkan_playlist(playlist)
        if len(playlist) > 0:
            try:
                no = int(input("Masukkan nomor lagu yang ingin dihapus: "))
                hapus_lagu(playlist, no)
            except ValueError:
                print("Nomor lagu harus berupa angka!")
                
    elif pilihan == "5":
        statistik_playlist(playlist, genre_set)
        
    elif pilihan == "6":
        print("Terima kasih telah menggunakan PlayTune!")
        break
    else:
        print("Pilihan menu tidak valid!")