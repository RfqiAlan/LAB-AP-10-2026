print("Setup Denah Bioskop NontonYuk")

while True:
    try:
        n = int(input("Masukkan jumlah baris: "))
        if n <= 0:
            print("jumlah baris harus lebih dari 0!")
        else:
            break
    except:
        print("input baris harus berupa angka!")

while True:
    try:
        m = int(input("Masukkan jumlah kursi per baris: "))
        if m <= 0:
            print("jumlah kursi harus lebih dari 0!")
        else:
            break
    except:
        print ("input kursi harus berupa angka")

    print("Daftar kursi tersedia")

for baris in range(1, n+1 ):
    for kursi in range (1, m+1 ):
        if kursi == 13:
            continue

        if baris == 1 and kursi % 2 == 0:
            continue

        print("baris", baris, "- kursi", kursi) 