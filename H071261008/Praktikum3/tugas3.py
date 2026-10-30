while True:
    try:
        kursi = int(input("Masukkan maksimal kursi bus: "))
        break
    except:
        print("Input jumlah kursi harus berupa angka!")

print("\n--- Sistem Reservasi PO BUS Dimulai ---")

sisa_kursi = kursi
total_pendapatan = 0

while sisa_kursi > 0:
    print("\nSisa kursi:", sisa_kursi)

    try:
        umur = int(input("Masukkan umur penumpang: "))

    except:
        print("Input umur harus berupa angka!")
        continue

    if umur < 0:
        print("Umur tidak valid!")
        continue

    if umur <= 5:
        harga = 0
        print("Kategori: Balita - Tiket Gratis (Rp 0)")

    elif umur <= 12:
        harga = 50000
        print("Kategori: Anak - Harga: Rp 50.000")

    else:
        harga = 100000
        print("Kategori: Dewasa - Harga: Rp 100.000")

    sisa_kursi = sisa_kursi - 1
    total_pendapatan = total_pendapatan + harga

print("\n--- Semua Kursi Terisi ---")
print("Total pendapatan perjalanan PO BUS kali ini: Rp", total_pendapatan)