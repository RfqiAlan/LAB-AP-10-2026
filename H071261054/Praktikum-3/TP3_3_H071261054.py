jumlah = 0

input_kursi = input("Masukkan jumlah kursi bus : ")
while input_kursi is not None:

    if input_kursi.isdigit():
        kursi = int(input_kursi)
        
        if kursi == 0:
            print("Program selesai. Terima kasih!")
            break
            
        if kursi > 0:
            print("--- Sistem Reservasi PO BUS Dimulai\n")
                
            while kursi > 0:
                print("Sisa Kursi :", kursi)
                input_umur = input("Masukkan Umur Penumpang: ")
                
                if input_umur.lstrip('-').isdigit():
                    umur = int(input_umur)
                    
                    if umur < 0:
                        print("Umur Tidak Valid (Tidak boleh minus)!\n")
                        continue
                    elif 0 <= umur <= 5:
                        kategori = "Balita"
                        harga = 0
                    elif 6 <= umur <= 12:
                        kategori = "Anak"
                        harga = 50000
                        jumlah += harga
                    else:
                        kategori = "Dewasa"
                        harga = 100000
                        jumlah += harga
                                                                
                    print(f"Kategori: {kategori} - harga : Rp.{harga}\n")
                    kursi -= 1
                    
                else:
                    print("Input Umur Harus Berupa Angka!\n")
                
            print("---Semua Kursi Terisi---")
            print(f"Total pendapatan perjalanan PO BUS hari ini adalah Rp.{jumlah}\n")
            break
else:
    print("\nInput Kursi harus berupa angka!\n")
