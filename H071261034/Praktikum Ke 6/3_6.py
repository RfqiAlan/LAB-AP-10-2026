def format_durasi(detik):
    """Ubah detik menjadi format menit:detik, contoh 354 -> 5:54"""
    menit, sisa = divmod(detik, 60)
    return f"{menit}:{sisa:02d}"


def tampilkan_menu():
    print("\n" + "=" * 50)
    print("PLAYLIST MUSIK - PLAYTUNE")
    print("=" * 50)
    print("Menu:")
    print("1. Tambah Lagu")
    print("2. Tampilkan Playlist")
    print("3. Filter berdasarkan Genre")
    print("4. Hapus Lagu")
    print("5. Statistik Playlist")
    print("6. Keluar")

def tambah_lagu(playlist, genre_set):
    judul = input("Judul lagu: ").strip()
    artis = input("Artis: ").strip()
    genre = input("Genre (Pop/Rock/Jazz/RnB/Dangdut): ").strip().capitalize()

    try:
        durasi = int(input("Durasi (dalam detik): "))
        if durasi <= 0:
            raise ValueError
    except ValueError:
        print("Error: Durasi harus berupa angka positif!")
        return

    for lagu in playlist:
        if (lagu[0].lower() == judul.lower()
                and lagu[1].lower() == artis.lower()
                and lagu[2].lower() == genre.lower()
                and lagu[3] == durasi):
            print(f"Gagal! Lagu '{judul}' oleh {artis} sudah ada di playlist.")
            return

    lagu_baru = (judul, artis, genre, durasi)
    playlist.append(lagu_baru)
    genre_set.add(genre)  # set: tanpa duplikasi
    print(f"Lagu '{judul}' oleh {artis} berhasil ditambahkan!")


def tampilkan_playlist(playlist):
    if not playlist:
        print("Playlist masih kosong!")
        return

    print("\n" + "=" * 50)
    print(f"{'No':<4}{'Judul':<22}{'Artis':<16}{'Genre':<8}{'Durasi':>6}")
    print("-" * 50)
    total = 0
    for i, (judul, artis, genre, durasi) in enumerate(playlist, start=1):
        print(f"{i:<4}{judul:<22}{artis:<16}{genre:<8}{format_durasi(durasi):>6}")
        total += durasi
    print("=" * 50)
    menit, detik = divmod(total, 60)
    print(f"Total durasi playlist: {menit} menit {detik} detik")


def filter_genre(playlist, genre_set):
    if not playlist:
        print("Playlist masih kosong!")
        return

    print("Genre tersedia:", sorted(genre_set))
    genre = input("Masukkan genre yang ingin difilter: ").strip().capitalize()

    if genre not in genre_set:
        print(f"Genre '{genre}' tidak ditemukan!")
        return

    # list comprehension untuk filter
    hasil = [lagu for lagu in playlist if lagu[2] == genre]

    print(f"\nLagu dengan genre '{genre}':")
    for i, (judul, artis, _, durasi) in enumerate(hasil, start=1):
        print(f"{i}. {judul} - {artis} ({format_durasi(durasi)})")


def hapus_lagu(playlist, genre_set):
    if not playlist:
        print("Playlist masih kosong!")
        return

    tampilkan_playlist(playlist)
    try:
        nomor = int(input("Masukkan nomor lagu yang ingin dihapus: "))
        if not 1 <= nomor <= len(playlist):
            raise IndexError
    except ValueError:
        print("Error: Input harus berupa angka!")
        return
    except IndexError:
        print("Error: Nomor lagu tidak valid!")
        return

    lagu = playlist.pop(nomor - 1)         # hapus berdasarkan index
    print(f"Lagu '{lagu[0]}' oleh {lagu[1]} berhasil dihapus!")

    # perbarui set genre agar sesuai dengan lagu yang tersisa
    genre_set.clear()
    genre_set.update(l[2] for l in playlist)


def statistik(playlist, genre_set):
    if not playlist:
        print("Playlist masih kosong!")
        return

    # dictionary distribusi genre
    distribusi = {}
    for _, _, genre, _ in playlist:
        distribusi[genre] = distribusi.get(genre, 0) + 1

    terpanjang = max(playlist, key=lambda l: l[3])
    terpendek = min(playlist, key=lambda l: l[3])

    print("\n" + "=" * 50)
    print("STATISTIK PLAYLIST PLAYTUNE")
    print("=" * 50)
    print(f"Total lagu    : {len(playlist)}")
    print(f"Jumlah genre  : {len(genre_set)}")
    print(f"Daftar genre  : {sorted(genre_set)}")
    print("\nDistribusi Genre:")
    for genre, jumlah in distribusi.items():
        print(f"  {genre:<8}: {jumlah} lagu")
    print(f"\nLagu terpanjang: {terpanjang[0]} ({format_durasi(terpanjang[3])})")
    print(f"Lagu terpendek : {terpendek[0]} ({format_durasi(terpendek[3])})")
    print("=" * 50)


def main():
    playlist = []        # list of tuples
    genre_set = set()    # set genre unik

    while True:
        tampilkan_menu()
        pilihan = input("\nPilih menu (1-6): ").strip()

        if pilihan == "1":
            tambah_lagu(playlist, genre_set)
        elif pilihan == "2":
            tampilkan_playlist(playlist)
        elif pilihan == "3":
            filter_genre(playlist, genre_set)
        elif pilihan == "4":
            hapus_lagu(playlist, genre_set)
        elif pilihan == "5":
            statistik(playlist, genre_set)
        elif pilihan == "6":
            print("Terima kasih telah menggunakan PlayTune!")
            break
        else:
            print("Pilihan tidak valid! Masukkan angka 1-6.")


if __name__ == "__main__":
    main()