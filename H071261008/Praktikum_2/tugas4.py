tujuan = str(input("Masukkan tujuan (Pantai/Pengunungan/Kota): "))
waktu = str(input("Masukkan waktu (Pagi/Malam): "))
tipe_pengunjung = str(input("Masukkan tipe pengunjung (Anak/Dewasa): "))

match tujuan:
    case "Pantai":
        if waktu == "Pagi": 
            paket = "A"
        elif waktu == "Malam" and tipe_pengunjung == "Dewasa":
            paket =  "C"
        else: 
            paket = "Tidak ada paket yang cocok"
    case "Pengunungan":
            if waktu == "Pagi" and tipe_pengunjung == "Dewasa": 
                paket = "B"
            elif waktu == "Malam" and tipe_pengunjung == "Dewasa":
                paket =  "C"
            else: 
                paket = "Tidak ada paket yang cocok"
    case "Kota":
                if waktu == "Malam":
                    paket = "C"
                else: 
                    paket = "Tidak ada paket yang cocok"

print(f"Paket Rekommendasi: Paket {paket}")