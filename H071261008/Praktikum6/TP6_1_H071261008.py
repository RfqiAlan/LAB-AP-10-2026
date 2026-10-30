def tambah_buku(inventaris, judul, penulis, harga, stok):
    buku = {"judul": judul, "penulis": penulis, "harga": harga, "stok": stok}
    inventaris.append(buku)
    print(f"Buku '{judul}' berhasil ditambahkan!")

def cari_buku(inventaris, kata_kunci):
    hasil = [b for b in inventaris if kata_kunci.lower() in b["judul"].lower()]
    if len(hasil) == 0:
        print("Buku tidak ditemukan.")
    else:
        print(f"Ditemukan {len(hasil)} buku:")
        nomor = 1
        for b in hasil:
            print(f" {nomor}. {b['judul']} - {b['penulis']} | Rp{b['harga']} | Stok: {b['stok']}")
            nomor += 1

def update_stok(inventaris, judul, jumlah):
    for b in inventaris:
        if b["judul"].lower() == judul.lower():
            if b["stok"] + jumlah < 0:
                print("Gagal! Stok tidak boleh negatif.")
            else:
                b["stok"] += jumlah
                if jumlah >= 0:
                    print(f"Stok '{b['judul']}' bertambah {jumlah}. Stok sekarang: {b['stok']}")
                else:
                    print(f"Stok '{b['judul']}' berkurang {-jumlah}. Stok sekarang: {b['stok']}")
            return
    print("Error: buku tidak ditemukan.")

def ringkasan_inventaris(inventaris):
    total_stok = 0
    total_aset = 0
    termahal = None
    for b in inventaris:
        total_stok += b["stok"]
        total_aset += b["harga"] * b["stok"]
        if termahal is None or b["harga"] > termahal["harga"]:
            termahal = b
    print("=" * 40)
    print("RINGKASAN INVENTARIS BOOKNEST")
    print("=" * 40)
    print(f"Jumlah jenis buku : {len(inventaris)}")
    print(f"Total seluruh stok: {total_stok}")
    print(f"Total nilai aset : Rp{total_aset}")
    if termahal is not None:
        print(f"Buku termahal : {termahal['judul']} (Rp{termahal['harga']})")
    print("=" * 40)

inventaris = []
print("=" * 40)
print(" SISTEM INVENTARIS TOKO BUKU BOOKNEST")
print("=" * 40)

while True:
    print("\nMenu:")
    print("1. Tambah Buku")
    print("2. Cari Buku")
    print("3. Update Stok")
    print("4. Ringkasan Inventaris")
    print("5. Keluar")
    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        judul = input("Judul buku: ")
        penulis = input("Penulis: ")
        try:
            harga = int(input("Harga: "))
            stok = int(input("Stok awal: "))
            if harga < 0 or stok < 0:
                print("Harga dan stok tidak boleh negatif!")
            else:
                tambah_buku(inventaris, judul, penulis, harga, stok)
        except ValueError:
            print("Harga dan stok harus berupa angka!")
    elif pilihan == "2":
        kata = input("Masukkan kata kunci judul: ")
        cari_buku(inventaris, kata)
    elif pilihan == "3":
        judul = input("Judul buku yang ingin diupdate: ")
        try:
            jumlah = int(input("Jumlah perubahan (positif=tambah, negatif=kurang): "))
            update_stok(inventaris, judul, jumlah)
        except ValueError:
            print("Jumlah harus berupa angka!")
    elif pilihan == "4":
        ringkasan_inventaris(inventaris)
    elif pilihan == "5":
        print("Terima kasih telah menggunakan BookNest!")
        break
    else:
        print("Pilihan tidak valid!")