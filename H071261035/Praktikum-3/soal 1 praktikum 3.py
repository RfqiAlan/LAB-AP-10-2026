print("Rekapitulasi Transaksi Dins Store")
print("Ketik '0' untuk menutup toko dan mengakhiri sesi")

while True:
    try:
        jumlah = int(input("Masukkan jumlah item:"))
        if jumlah == 0:
            print("Toko ditutp. Sesi rekap selesai")
            break
        elif jumlah < 0:
            print("jumlah tidak boleh negatif")
        elif jumlah >100:
            print("maksimal 100 item per transaksi")
        else:
            print("transaksi", jumlah, "item berhasil")

    except:
        print("input harus berupa angka!")