while True:
  try:
    kursi = int(input("Masukkan maksimal kursi bus:  "))
    if kursi <= 0:
      print("Jumlah baris harus lebih dari 0")
    else:
      break
  except:
    print("Input jumlah kursi harus berupa angka!")

print("---Sistem Reservasi PO BUS Dimulai---")
total = 0
sisa = kursi
while sisa > 0:
    print(f"Sisa kursi: {sisa}")
    try:
      umur = int(input("Masukkan umur penumpang:  "))
      if umur < 0:
        print("Umur tidak valid")
        continue
      elif 0 <= umur <= 5:
        harga = 0
        print(f"Kategori: Balita - Tiket Gratis Rp ({harga})")
      elif 6 <= umur <= 12:
        harga = 50000
        print(f"Kategori: Anak - Harga Rp {harga}")
      elif umur > 12:
        harga = 100000
        print(f"Kategori: Dewasa - Harga Rp {harga}")
      else:
        kursi == 0
        break
      sisa-= 1
      total += harga
    except:
      print("Input kursi harus berupa angka")
      continue
print("---Semua Kursi Terisi---")
print(f"Total pendapatan perjalanan PO Bus kali ini: Rp{total}")