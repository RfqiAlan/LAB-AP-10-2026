print("--- Rekapitulasi Transaksi Dins Store ---")
print("Ketik '0' untuk menutup toko dan mengakhiri sesi.")

while True:
    user_input = input("Masukkan jumlah item: ")

    try:
        jumlah = int(user_input)
    except ValueError:
        print("Input harus berupa angka!")
        continue

    if jumlah == 0:
        print("Toko ditutup. Sesi rekap selesai.")
        break

    elif jumlah < 0:
        print("Jumlah tidak boleh negatif")
        # continue

    elif jumlah > 100:
        print("Maksimal 100 item per transaksi!")
        # continue
    

    print(f"Transaksi {jumlah} item berhasil!")