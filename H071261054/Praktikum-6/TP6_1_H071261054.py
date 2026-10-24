print("=" * 40)
print("SISTEM INVENTARIS TOKO BUKU BOOKNEST")
print("=" * 40)

database_buku = []

def tambah_buku(judul, penulis, harga, stok):
    judul_clean = judul.lower().strip()
    
    if any(buku["judul"] == judul_clean for buku in database_buku):
        print(f"Buku '{judul.capitalize()}' sudah ada di database!")
        return False
        
    data_buku = {
        "judul": judul_clean,
        "penulis": penulis.lower().strip(),
        "harga": harga,
        "stok": stok
    }
    database_buku.append(data_buku)
    return True

def cari_buku(kata_kunci, database):
    hasil_pencarian = []
    kata = kata_kunci.lower().strip()
    
    for buku in database:
        if kata in buku["judul"] or kata in buku["penulis"]:
            hasil_pencarian.append(buku)
            
    return hasil_pencarian

def update_stok(judul, jumlah):
    ditemukan = False
    judul_clean = judul.lower().strip()
    
    for buku in database_buku:
        if judul_clean in buku["judul"]:
            stok_baru = buku["stok"] + jumlah
            if stok_baru < 0:
                print(f"Gagal! Stok tidak boleh kurang dari 0. Stok saat ini: {buku['stok']}")
            else:
                buku["stok"] = stok_baru
                print(f"Stok buku '{buku['judul'].capitalize()}' berhasil diubah. Stok sekarang: {buku['stok']}")
            ditemukan = True
            # break
        
    if not ditemukan:
        print(f"Buku dengan judul '{judul}' tidak ditemukan.")

def ringkasan_inventaris(database):
    if not database:
        print("Database masih kosong!")
        return

    total_jenis = len(database)
    total_stok = sum(buku["stok"] for buku in database)
    total_nilai_aset = sum(buku["harga"] * buku["stok"] for buku in database)
    buku_termahal = max(database, key=lambda b: b["harga"])
            
    print("=" * 40)
    print("RINGKASAN INVENTARIS BOOKNEST")
    print("=" * 40)
    print(f"Jumlah Jenis Buku  : {total_jenis}")
    print(f"Total Seluruh Stok : {total_stok}")
    print(f"Total Nilai Aset   : Rp{total_nilai_aset:,}")
    print(f"Buku Termahal      : {buku_termahal['judul'].capitalize()} (Rp{buku_termahal['harga']:,})")
    print("=" * 40)


while True:
    print("\nMenu:")
    print("1. Tambah Buku")
    print("2. Cari Buku")
    print("3. Update Stok")
    print("4. Ringkasan Inventaris")
    print("5. Keluar")

    try:
        pilih = int(input("Pilih Menu (1-5): "))
    except ValueError:
        print("Pilihan harus berupa angka!")
        continue

    if pilih == 1:
        judul = input("Masukkan Judul Buku: ")
        penulis = input("Masukkan Penulis Buku: ")
        try:
            harga = int(input("Masukkan Harga Buku: "))
            stok = int(input("Masukkan Stok Buku: "))
            if stok < 0 or harga < 0:
                print("Stok dan harga tidak boleh kurang dari 0!")
                continue
        except ValueError:
            print("Input harga dan stok harus berupa angka!")
            continue
        
        berhasil = tambah_buku(judul, penulis, harga, stok)
        if berhasil:
            print(f"Buku '{judul.capitalize()}' berhasil ditambahkan.")
        
    elif pilih == 2:
        kata_kunci = input("Masukkan Kata Kunci: ")
        hasil = cari_buku(kata_kunci, database_buku)
        if hasil:
            print(f"\nHasil pencarian untuk '{kata_kunci}':")
            for idx, buku in enumerate(hasil, start=1):
                print(f"{idx}. {buku['judul'].capitalize()} | {buku['penulis'].capitalize()} | Rp{buku['harga']:,} | stok: {buku['stok']}")
        else:
            print("Buku tidak ditemukan.")

    elif pilih == 3:
        judul_buku = input("Judul Buku Yang Ingin Di-update: ")
        try:
            jumlah = int(input("Jumlah perubahan (positif=tambah, negatif=kurang): "))
            update_stok(judul_buku, jumlah)
        except ValueError:
            print("Jumlah perubahan harus berupa angka!")

    elif pilih == 4:
        ringkasan_inventaris(database_buku)

    elif pilih == 5:
        print("Terima kasih telah menggunakan BookNest!")
        break
    else:
        print("Pilihan menu tidak valid!")