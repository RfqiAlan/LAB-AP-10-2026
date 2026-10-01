print("--- Rekapitulasi Transaksi Din Store")
print("Ketik 0 untuk menutup toko dan mengakhiri sesi")


while True:
    try:
        dins_store = int(input("Masukkan jumlah item: "))


        if dins_store == 0:

            print("Toko ditutup. Sesi rekap selesai")
            break
            
        elif dins_store < 0:
            print("Jummlah tidak boleh negatif")
            
        elif dins_store > 100:
            print("Maksimal 100 item per transaksi")
            
        else:
            print(f"Transaksi {dins_store} item berhasil")
            
    except ValueError:
        print("Input nilai harus berupa angka!")
        break