playlist = []
genre_set = set()


def tambah_lagu(playlist, genre_set, judul, artis, genre, durasi):
    for lagu_sama in playlist:
        if lagu_sama[0].lower() == judul.lower() and lagu_sama[1].lower() == artis.lower():
            print(f"Gagal! Lagu {judul} oleh {artis} telah ada dalam playlist!")
            
            return
    lagu = (judul, artis, genre, durasi)
    playlist.append(lagu)
    genre_set.add(genre.capitalize())

    print(f"Lagu '{judul}' oleh {artis} berhasil ditambahkan!")


def tampilkan_playlist(playlist):
    print("\n" + "=" * 65)
    print(f"{'No':<5}{'Judul':<23}{'Artis':<18}{'Genre':<10}Durasi")
    print("=" * 65)

    total_durasi = 0

    for nomor, lagu in enumerate(playlist, 1):
        judul, artis, genre, durasi = lagu

        menit = durasi // 60
        detik = durasi % 60

        print(
            f"{nomor:<5}{judul:<23}{artis:<18}"
            f"{genre:<10}{menit}:{detik:02d}"
        )

        total_durasi += durasi

    print("=" * 65)

    total_menit = total_durasi // 60
    sisa_detik = total_durasi % 60

    print(
        f"Total durasi playlist: "
        f"{total_menit} menit {sisa_detik} detik"
    )


def filter_genre(playlist, genre_target):
    hasil = [
        lagu for lagu in playlist
        if lagu[2].lower() == genre_target.lower()
    ]

    return hasil


def hapus_lagu(playlist, nomor):
    if nomor < 1 or nomor > len(playlist):
        print("Nomor lagu tidak valid.")
        return

    lagu_dihapus = playlist.pop(nomor - 1)

    print(f"Lagu '{lagu_dihapus[0]}' berhasil dihapus!")


def statistik_playlist(playlist, genre_set):
    print("\n" + "=" * 40)
    print("STATISTIK PLAYLIST PLAYTUNE")
    print("=" * 40)

    print(f"Total lagu      : {len(playlist)}")
    print(f"Jumlah genre    : {len(genre_set)}")
    print(f"Daftar genre    : {genre_set}")

    distribusi = {}

    for lagu in playlist:
        genre = lagu[2]

        if genre in distribusi:
            distribusi[genre] += 1
        else:
            distribusi[genre] = 1

    print("\nDistribusi genre:")

    for genre, jumlah in sorted(distribusi.items()):
        print(f"  {genre:<12}: {'#' * jumlah} ({jumlah})")

    if len(playlist) > 0:
        lagu_terpanjang = max(playlist, key=lambda lagu: lagu[3])
        lagu_terpendek = min(playlist, key=lambda lagu: lagu[3])

        durasi_panjang = lagu_terpanjang[3]
        durasi_pendek = lagu_terpendek[3]

        print(
            f"\nLagu terpanjang : {lagu_terpanjang[0]} "
            f"({durasi_panjang // 60}:{durasi_panjang % 60:02d})"
        )

        print(
            f"Lagu terpendek : {lagu_terpendek[0]} "
            f"({durasi_pendek // 60}:{durasi_pendek % 60:02d})"
        )
    else:
        print("\nBelum ada lagu dalam playlist.")

    print("=" * 40)


print("=" * 40)
print("PLAYLIST MUSIK - PLAYTUNE")
print("=" * 40)

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
        genre = genre.capitalize()

        try:
            durasi = int(input("Durasi (dalam detik): "))

            if durasi <= 0:
                print("Durasi harus berupa angka positif.")
            else:
                tambah_lagu(
                    playlist,
                    genre_set,
                    judul,
                    artis,
                    genre,
                    durasi
                )

        except ValueError:
            print("Durasi harus berupa angka.")

    elif pilihan == "2":
        if len(playlist) == 0:
            print("Playlist masih kosong.")
        else:
            tampilkan_playlist(playlist)

    elif pilihan == "3":
        if len(genre_set) == 0:
            print("Belum ada genre tersedia.")
        else:
            print("Genre tersedia:", genre_set)
            genre_target = input("Masukkan genre yang ingin difilter: ")

            hasil = filter_genre(playlist, genre_target)

            if len(hasil) == 0:
                print("Tidak ada lagu dengan genre tersebut.")
            else:
                print(f"\nLagu bergenre '{genre_target.capitalize()}':")

                for nomor, lagu in enumerate(hasil, 1):
                    menit = lagu[3] // 60
                    detik = lagu[3] % 60

                    print(
                        f"  {nomor}. {lagu[0]} - {lagu[1]} "
                        f"({menit}:{detik:02d})"
                    )

    elif pilihan == "4":
        if len(playlist) == 0:
            print("Playlist masih kosong.")
        else:
            tampilkan_playlist(playlist)

            try:
                nomor = int(input("Nomor lagu yang ingin dihapus: "))
                hapus_lagu(playlist, nomor)

                # Memperbarui genre berdasarkan lagu yang tersisa
                genre_set.clear()

                for lagu in playlist:
                    genre_set.add(lagu[2])

            except ValueError:
                print("Nomor lagu harus berupa angka.")

    elif pilihan == "5":
        statistik_playlist(playlist, genre_set)

    elif pilihan == "6":
        print("Terima kasih telah menggunakan PlayTune!")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih 1-6.")