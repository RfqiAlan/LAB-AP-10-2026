print("--- Setup Denah Bioskop NontonYuk ---")

while True:
    try:
        baris = int(input("\nMasukkan jumlah baris: "))
    except:
        print("Input baris harus berupa angka!")
        continue
    else:
        if baris > 0:
            break
        else:
            print("Jumlah baris harus lebih dari 0!")

while True:
    try:
        kursi = int(input("Masukkan jumlah kursi per baris: "))
        break
    except:
        print("Input kursi harus berupa angka!")

print("\n--- Daftar Kursi Tersedia ---")

for b in range(1, baris + 1):
    for k in range(1, kursi + 1):
        if k == 13:
            continue
        if b == 1 and k % 2 == 0:
            continue
        print(f"Baris {b} - Kursi {k}")