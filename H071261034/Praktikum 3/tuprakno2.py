print("--- Setup Denah Bioskop Nonton yuk ---")
baris = int(input("Masukkan jumlah baris: "))
kursi = int(input("Masukkan jumlah kursi per baris: "))

while True:
    try:

        if baris <= 0:
            print("Jumlah baris harus lebih dari 0!")
        elif kursi <= 0:
            print("Jumlah kursi harus lebih dari 0!")
        else:
            break

    except ValueError:
        print("Input baris harus berupa angka!")

print("--- Daftar Kursi Tersedia ---")

for b in range(1, baris + 1):
    for k in range(1, kursi + 1):

        if k == 13:
            continue

        if b == 1:
            if k % 2 == 1:
                print(f"Baris {b} - Kursi {k}")

        else:
            print(f"Baris {b} - Kursi {k}")