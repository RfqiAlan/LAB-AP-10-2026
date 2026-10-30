def hitung_mundur(n):
    if n == 0:
        print(0)
        print("Luncurkan!")
        return

    print(n)
    hitung_mundur(n - 1)


# Langsung jalankan perulangan di luar fungsi
while True:
    try:
        angka_awal = int(input("Masukkan angka awal hitung mundur: "))
        
        if angka_awal < 0:
            print("Input tidak valid, angka tidak boleh negatif.")
        else:
            hitung_mundur(angka_awal)
            break
    except ValueError:
        print("Input tidak valid, harap masukkan angka bulat.")