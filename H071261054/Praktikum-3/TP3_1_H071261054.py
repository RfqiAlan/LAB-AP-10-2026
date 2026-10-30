print("="*26)
print("----- Kasir Otomatis -----")
print("="*26)

jumlah = 1
while jumlah != 0:
    try:
        print("Ketik 0 Untuk Keluar")
        jumlah = int(input("Masukkan Jumlah Item : "))
        
        if jumlah < 0:
            print("jumlah tidak boleh negatif")   
            print("="*26,"\n") 
        elif 0<jumlah<=100:
            print("Transaksi Berhasil")
            print("="*26,"\n")
            print(jumlah) 
        elif jumlah > 100:
            print("Maksimal 100 Item Per Transaksi")
            print("="*26,"\n") 
         
    except ValueError:
        print("input harus berupa angka")
        print("="*26,"\n")
else:
    print("Toko Ditutup. Sesi rekap selesai")
        
    