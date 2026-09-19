# input dari pengguna 
tujuan = input("Masukkan tujuan Anda (Pantai, Pegunungan, Kota): ")
waktu = input("Masukkan waktu perjalanan Anda (Pagi, Malam): ")
pengunjung = input("Masukkan tipe pengunjung Anda (Anak, Dewasa): ")

# paket dan tujuan
match tujuan:
    case "Pantai":
        if waktu == "Pagi":
            paket = "Paket A"
        elif waktu == "Malam" and pengunjung == "Dewasa":
            paket = "Paket C"
        else:
            paket = "Tidak ada paket yang cocok"
    case "Pegunungan":
        if waktu == "Pagi" and pengunjung == "Dewasa":
            paket = "Paket B"
        elif waktu == "Malam" and pengunjung == "Dewasa":
            paket = "Paket C"
        else:
            paket = "Tidak ada paket yang cocok"
    case "Kota":
        if waktu == "Malam":
            paket = "Paket C"
        else:
            paket = "Tidak ada paket yang cocok"
            
# Menampilkan hasil rekomendasi paket
print(f"Paket Rekomendasi: {paket}")