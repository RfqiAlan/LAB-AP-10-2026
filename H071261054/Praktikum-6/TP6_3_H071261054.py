database_lagu = []
database_genre = set()

def tambah_lagu(playlist, genre_set, judul, artis, genre, durasi):
    judul_clean = judul.strip()
    artis_clean = artis.strip()
    genre_clean = genre.strip().capitalize()

    for lagu in playlist:
        if lagu[0].lower() == judul_clean.lower() and lagu[1].lower() == artis_clean.lower():
            print(f"Lagu '{judul_clean}' oleh {artis_clean} sudah ada di playlist!")
            return False
    
    data_lagu = (judul_clean, artis_clean, genre_clean, durasi)
    
    playlist.append(data_lagu)
    genre_set.add(genre_clean)
    
    print(f"Lagu '{judul_clean}' oleh {artis_clean} berhasil ditambahkan.")
    return True

def tampilkan_playlist(playlist):
    if not playlist:
        print("Playlist masih kosong.")
        return 0

    header_border = "=" * 55
    print(header_border)
    print(f"{'No':<3} {'Judul':<22} {'Artis':<15} {'Genre':<8} {'Durasi':<6}")
    print(header_border)
    
    total_durasi = 0
    for idx, lagu in enumerate(playlist, start=1):
        judul, artis, genre, durasi = lagu
        menit, detik = divmod(durasi, 60)
        format_durasi = f"{menit}:{detik:02d}"
        total_durasi += durasi
        
        print(
            f"{idx:<3} "
            f"{judul:<22} "
            f"{artis:<15} "
            f"{genre:<8} "
            f"{format_durasi:<6}"
        )
    
    print(header_border)
    return total_durasi
    
def filter_genre(playlist, genre_target):
    hasil = [lagu for lagu in playlist if lagu[2].lower() == genre_target.lower()]
    
    if hasil:
        print(f"\nLagu Bergenre '{genre_target.capitalize()}':")
        for idx, lagu in enumerate(hasil, start=1):
            judul, artis, _, durasi = lagu
            menit, sisa_detik = divmod(durasi, 60)
            print(f"{idx}. {judul} - {artis} ({menit}:{sisa_detik:02d})") 
    else:
        print(f"Tidak ada lagu dengan genre {genre_target.capitalize()}")
        
def hapus_lagu(playlist, genre_set, nomor):
    if not playlist:
        print("Playlist Masih Kosong")
        return
    
    if 1 <= nomor <= len(playlist):
        lagu_dihapus = playlist.pop(nomor - 1)
        genre_dihapus = lagu_dihapus[2]
        print(f"Lagu '{lagu_dihapus[0]}' oleh {lagu_dihapus[1]} berhasil dihapus!")
        
        genre_masih_ada = any(lagu[2].lower() == genre_dihapus.lower() for lagu in playlist)
        
        if not genre_masih_ada:
            genre_dihapus_set = None
            for g in genre_set:
                if g.lower() == genre_dihapus.lower():
                    genre_dihapus_set = g 
                    break
                    
            if genre_dihapus_set:       
                genre_set.discard(genre_dihapus_set)
    else:
        print("Nomor lagu tidak valid.")
        
def statistik_playlist(playlist, genre_set):
    total_lagu = len(playlist)
    total_genre = len(genre_set)
    
    print("=" * 40)
    print("STATISTIK PLAYLIST PLAYTUNE")
    print("=" * 40)
    print(f"Total Lagu  : {total_lagu}")
    print(f"Total Genre : {total_genre}")
    print(f"Daftar Genre: {genre_set}\n")
    
    if total_lagu > 0:
        hitung_genre = {}
        for lagu in playlist:
            g = lagu[2] 
            hitung_genre[g] = hitung_genre.get(g, 0) + 1
            
        print("Distribusi genre:")
        for g, jumlah in hitung_genre.items():
            batang = "#" * jumlah
            print(f"{g:<8} : {batang} ({jumlah})")

print("=" * 40)
print("PLAYLIST MUSIC - PLAYTUNE")
print("=" * 40)

while True:
    print("\nMenu:")
    print("1. Tambahkan Lagu")
    print("2. Tampilkan Playlist")
    print("3. Filter Berdasarkan Genre")
    print("4. Hapus Lagu")
    print("5. Statistik Playlist")
    print("6. Keluar")
    
    try:
        pilih = int(input("Masukkan Pilihan (1-6): "))
    except ValueError:
        print("Input harus berupa angka!")
        continue
        
    if pilih == 1:
        judul = input("Masukkan Judul Lagu: ")
        artis = input("Masukkan Nama Artis: ")
        genre = input("Genre (Pop/Rock/Jazz/RnB/Dangdut): ")
        
        try:
            durasi = int(input("Masukkan Durasi Lagu (dalam detik): "))
            tambah_lagu(database_lagu, database_genre, judul, artis, genre, durasi)
        except ValueError:
            print("Durasi harus berupa angka detik!")
        
    elif pilih == 2:
        total_durasi = tampilkan_playlist(database_lagu)
        if total_durasi > 0:
            menit_total, detik_total = divmod(total_durasi, 60)
            print(f"Total Durasi playlist: {menit_total} menit {detik_total} detik")

    elif pilih == 3:
        print(f"Genre Tersedia : {database_genre if database_genre else 'Belum Ada'}")
        genre = input("Masukkan Genre Yang Ingin Difilter: ").strip()
        filter_genre(database_lagu, genre)

    elif pilih == 4:
        if not database_lagu:
            print("Playlist masih kosong.")
            continue
            
        tampilkan_playlist(database_lagu)
        try:
            nomor = int(input("Masukkan Nomor Lagu Yang Ingin Dihapus: "))
            hapus_lagu(database_lagu, database_genre, nomor)
        except ValueError:
            print("Input harus berupa angka!")

    elif pilih == 5:
        statistik_playlist(database_lagu, database_genre)

    elif pilih == 6:
        print("Terima Kasih Telah Menggunakan PlayTune!")
        break
    else:
        print("Pilihan menu tidak valid!")