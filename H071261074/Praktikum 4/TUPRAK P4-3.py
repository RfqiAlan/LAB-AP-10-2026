def hitung_mundur(angka):
    
    print(angka)
    
    if angka > 0:
        hitung_mundur(angka - 1)

def main():
    while True:
        try:
            angka_awal = int(input("Masukkan angka awal hitung mundur: "))
            if angka_awal < 0:
                print("Input tidak valid, angka tidak boleh negatif.")
            else:
                hitung_mundur(angka_awal)
                break
        except ValueError:
            print("Input tidak valid, masukkan angka bulat.")

if __name__ == "__main__":
    main()