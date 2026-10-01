kuota_kursi = 0


while True:
    try:
        kuota_kursi = int(input("Masukkan maksimal kursi bus: "))
        break
    except ValueError:
        print("Input jumlah kursi harus berupa angka!")

print("--- Sistem Reservasi PO BUS Dimulai ---")

total_pendapatan = 0

while kuota_kursi > 0:
    print(f"Sisa kursi: {kuota_kursi}")
    
    try:
        umur = int(input("Masukkan umur penumpang: "))
    except ValueError:
        print("Input umur harus berupa angka!")
        continue


    if 0 <= umur <= 5:
        kategori = "Balita - Tiket Gratis (Rp 0)"
        harga = 0
    elif 6 <= umur <= 12:
        kategori = "Anak - Harga: Rp 50.000"
        harga = 50000
    elif umur > 12:
        kategori = "Dewasa - Harga: Rp 100.000"
        harga = 100000
    else:
       print("Umur tidak valid")

    print(f"Kategori: {kategori}\n")

    total_pendapatan += harga
    kuota_kursi -= 1

print("--- Semua Kursi Terisi ---")
print(f"Total pendapatan perjalanan PO BUS kali ini: Rp {total_pendapatan}")