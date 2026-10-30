tujuan = input("Masukkan tujuan (Pantai/Pegunungan/Kota): ").capitalize()
waktu = input("Masukkan waktu (Pagi/Malam): ").capitalize()
tipe = input("Masukkan tipe pengunjung (Anak/Dewasa): ").capitalize()

match tujuan:
    case "Pantai":
        if waktu == "Pagi" :
            paket = "Paket A"
        else:
            if waktu == "Malam" and tipe == "Dewasa":
                paket = "Paket C"
            else:
                paket = "Tidak ada paket yang cocok"

    case "Pegunungan":
        if waktu == "Pagi" and tipe == "Dewasa":
            paket = "Paket B"
        else:
            if waktu == "Malam" and tipe == "Dewasa":
                paket = "Paket C"
            else:
                paket = "Tidak ada paket yang cocok"

    case "Kota":
        if waktu == "Malam":
            paket = "Paket C"
        else:
            paket = "Tidak ada paket yang cocok"

    case _:
        paket = "Tidak ada paket yang cocok"

print(f"Paket Rekomendasi: {paket}")