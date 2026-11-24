def tambah_buku(inventaris, judul, penulis, harga, stok):
    for buku_sudah_ada in inventaris:
        if buku_sudah_ada ["judul"] == judul:
            return "ikik"
    buku = {
        "judul": judul,
        "penulis": penulis,
        "harga": harga,
        "stok": stok
    }
    inventaris.append(buku)
    print(f"Buku '{judul}' berhasil ditambahkan!")

def cari_buku(inventaris, kata_kunci):
    hasil = []
    for buku in inventaris:
        if kata_kunci.lower() in buku["judul"].lower():
            hasil.append(buku)
    
    if len(hasil) == 0:
        print("Buku tidak ditemukan.")
    else:
        print(f"Ditemukan {len(hasil)} buku:")
        nomor = 1
        for buku in hasil:
            print(f"{nomor}. {buku['judul']} - {buku['penulis']} | Rp{buku['harga']} | Stok: {buku['stok']}")
            nomor += 1

def update_stok(inventaris, judul, jumlah):
    buku_ditemukan = False
    for buku in inventaris:
        if buku["judul"].lower() == judul.lower():
            buku_ditemukan = True
            stok_baru = buku["stok"] + jumlah
            if stok_baru < 0:
                print("Gagal! Stok tidak boleh menjadi negatif.")
            else:
                buku["stok"] = stok_baru
                if jumlah >= 0:
                    print(f"Stok '{buku['judul']}' bertambah {jumlah}. Stok sekarang: {buku['stok']}")
                else:
                    print(f"Stok '{buku['judul']}' berkurang {abs(jumlah)}. Stok sekarang: {buku['stok']}")
            break
    if not buku_ditemukan:
        print("Error: Buku tidak ditemukan!")

def ringkasan_inventaris(inventaris):
    if len(inventaris) == 0:
        print("Inventaris masih kosong.")
        return
    
    jumlah_jenis = len(inventaris)
    total_stok = 0
    total_aset = 0
    buku_termahal = inventaris[0]
    
    for buku in inventaris:
        total_stok += buku["stok"]
        total_aset += buku["harga"] * buku["stok"]
        if buku["harga"] > buku_termahal["harga"]:
            buku_termahal = buku
            
    print("==============================")
    print("RINGKASAN INVENTARIS BOOKNEST")
    print("==============================")
    print(f"Jumlah jenis buku : {jumlah_jenis}")
    print(f"Total seluruh stok: {total_stok}")
    print(f"Total nilai aset  : Rp{total_aset}")
    print(f"Buku termahal     : {buku_termahal['judul']} (Rp{buku_termahal['harga']})")
    print("==============================")

inventaris = []

print("==========================================")
print("SISTEM INVENTARIS TOKO BUKU BOOKNEST")
print("==========================================")

while True:
    print(" Menu:")
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
        kata_kunci = input("Masukkan kata kunci judul: ")
        cari_buku(inventaris, kata_kunci)
        
    elif pilihan == "3":
        judul = input("Judul buku yang ingin diupdate: ")
        try:
            jumlah = int(input("Jumlah perubahan (positif=tambah, negatif=kurang): "))
            update_stok(inventaris, judul, jumlah)
        except ValueError:
            print("Jumlah perubahan harus berupa angka!")
            
    elif pilihan == "4":
        ringkasan_inventaris(inventaris)
        
    elif pilihan == "5":
        print("Terima kasih telah menggunakan BookNest!")
        break
    else:
        print("Pilihan menu tidak valid!")