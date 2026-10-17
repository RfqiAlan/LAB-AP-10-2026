while True:
    try:
        sisa_kursi = int(input("masukkan maksimal kursi bus: "))
        if sisa_kursi <= 0:
            print("jumlah kursi harus lebih dari 0!")
        else:
            break
    except:
        print("input jumlah kursi harus berupa angka!")

print("Sistem Reservasi PO BUS Dimulai")
total = 0

while sisa_kursi > 0:
    print("sisa kursi:", sisa_kursi)
    try:
        umur = int(input("Masukkan umur penumpang: "))

        if umur < 0:
            print("umur tidak valid")
            continue

        if umur <= 5:
            harga = 0
            print("kategori: balits")
            print("Tiket Gratis (Rp 0)")
        elif umur <= 12:
            harga = 500000
            print("kategori: anak harga: (Rp 50.000)")

        else:
            harga = 100000
            print("kategori: dewasa harga: (RP 100.000)")

        total = total + harga
        sisa_kursi = sisa_kursi -1

    except:
        print("input umur harus berupa angka!")

print("Semua Kursi Terisi")
print("Total pendapatan perjalanan PO BUS kali ini:Rp", total)