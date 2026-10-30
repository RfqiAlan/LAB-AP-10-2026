def tambah_buku(inventaris, judul, penulis, harga, stok):
    for buku in inventaris:
        if (buku["judul"].lower() == judul.lower()
                and buku["penulis"].lower() == penulis.lower()
                and buku["harga"] == harga):
            return f"Gagal! Buku '{judul}' sudah ada dalam inventaris."

    buku_baru = {
        "judul": judul,
        "penulis": penulis,
        "harga": harga,
        "stok": stok
    }
    inventaris.append(buku_baru)
    return f"Buku '{judul}' berhasil ditambahkan!"


def cari_buku(inventaris, kata_kunci):
    hasil = []
    for buku in inventaris:
        if kata_kunci.lower() in buku["judul"].lower():
            hasil.append(buku)
    return hasil

def update_stok(inventaris, judul, jumlah):
    for buku in inventaris:
        if buku["judul"].lower() == judul.lower():
            stok_baru = buku["stok"] + jumlah
            if stok_baru < 0:
                return "Gagal: Stok tidak boleh menjadi negatif."
            buku["stok"] = stok_baru
            if jumlah < 0:
                return f"Stok '{buku['judul']}' berkurang {abs(jumlah)}. Stok sekarang: {buku['stok']}"
            else:
                return f"Stok '{buku['judul']}' bertambah {jumlah}. Stok sekarang: {buku['stok']}"
    return "Error: Buku tidak ditemukan."

def ringkasan_inventaris(inventaris):
    if not inventaris:
        return {
            "jumlah_jenis_buku": 0,
            "total_stok": 0,
            "total_aset": 0,
            "buku_termahal": None
        }
    
    jumlah_jenis = len(inventaris)
    total_stok = 0
    total_aset = 0
    buku_termahal = inventaris[0]
    
    for buku in inventaris:
        total_stok += buku["stok"]
        total_aset += buku["harga"] * buku["stok"]
        if buku["harga"] > buku_termahal["harga"]:
            buku_termahal = buku
            
    return {
        "jumlah_jenis_buku": jumlah_jenis,
        "total_stok": total_stok,
        "total_aset": total_aset,
        "buku_termahal": buku_termahal
    }

def main():
    inventaris = []
    print("==========================================")
    print("  SISTEM INVENTARIS TOKO BUKU BOOKNEST")
    print("==========================================")
    
    while True:
        print("\nMenu:")
        print("1. Tambah Buku")
        print("2. Cari Buku")
        print("3. Update Stok")
        print("4. Ringkasan Inventaris")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")
        
        if pilihan == "1":
            judul = input("Judul buku: ").strip()
            penulis = input("Penulis: ").strip()
            try:
                harga = float(input("Harga: "))
                stok = int(input("Stok awal: "))
                if harga < 0 or stok < 0:
                    print("Harga dan stok tidak boleh negatif.")
                    continue
                tambah_buku(inventaris, judul, penulis, harga, stok)
                print(tambah_buku(inventaris, judul, penulis, harga, stok))
            except ValueError:
                print("Error: Harga harus berupa angka dan stok harus berupa bilangan bulat.")
                
        elif pilihan == "2":
            kata_kunci = input("Masukkan kata kunci judul: ")
            hasil_cari = cari_buku(inventaris, kata_kunci)
            if hasil_cari:
                print(f"Ditemukan {len(hasil_cari)} buku:")
                for i, b in enumerate(hasil_cari, 1):
                    harga_int = int(b['harga']) if b['harga'].is_integer() else b['harga']
                    print(f"  {i}. {b['judul']} - {b['penulis']} | Rp{harga_int} | Stok: {b['stok']}")
            else:
                print("Buku tidak ditemukan.")
                
        elif pilihan == "3":
            judul = input("Judul buku yang ingin diupdate: ")
            try:
                jumlah = int(input("Jumlah perubahan (positif=tambah, negatif=kurang): "))
                pesan = update_stok(inventaris, judul, jumlah)
                print(pesan)
            except ValueError:
                print("Error: Jumlah perubahan stok harus berupa angka.")
                
        elif pilihan == "4":
            ringkasan = ringkasan_inventaris(inventaris)
            print("==========================================")
            print("RINGKASAN INVENTARIS BOOKNEST")
            print("==========================================")
            print(f"Jumlah jenis buku : {ringkasan['jumlah_jenis_buku']}")
            print(f"Total seluruh stok: {ringkasan['total_stok']}")
            print(f"Total nilai aset  : Rp{int(ringkasan['total_aset'])}")
            if ringkasan['buku_termahal']:
                bt = ringkasan['buku_termahal']
                harga_termahal = int(bt['harga']) if bt['harga'].is_integer() else bt['harga']
                print(f"Buku termahal     : {bt['judul']} (Rp{harga_termahal})")
            else:
                print("Buku termahal     : -")
            print("==========================================")
                
        elif pilihan == "5":
            print("Terima kasih telah menggunakan BookNest!")
            break
        else:
            print("Pilihan tidak valid, silakan pilih menu 1-5.")

if __name__ == "__main__":
    main()