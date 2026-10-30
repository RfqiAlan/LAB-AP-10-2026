# Nomor 4
print("Aplikasi Pemesanan Tiket")
print("========================")
print("Pilihan Wisata Liburan")
print("1. Pantai")
print("2. Pegunungan")
print("3. Kota")
print("========================")

tujuan = int(input("Masukkan tujuan (1/2/3) : "))
waktu = input("Masukkan waktu (Pagi/Malam) : ").capitalize()
tipe = input("Masukkan tipe pengunjung (Anak/Dewasa) : ").capitalize()
paket = ""

if tujuan != [1,2,3] and waktu != ["Pagi", "Malam"] and tipe != ["Anak", "Dewasa"]:
    match tujuan:
        case 1:
            if waktu == "Pagi" and (tipe == "Anak" or tipe =="Dewasa"):
                paket = "A"
            elif waktu == "Malam" and tipe == "Dewasa":
                paket = "C"
        case 2:
            if waktu == "Pagi" and tipe == "Dewasa":
                paket = "B"
            elif waktu == "Malam" and tipe == "Dewasa":
                paket = "C"
        case 3:
            if waktu == "Malam" and (tipe == "Anak" or tipe =="Dewasa"):
                paket = "C"
else:
    exit()

if paket:
    print(f"Paket Rekomendasi : Paket {paket}")
else:
    print("Tidak ada paket yang cocok")
    
# match tujuan:
#     case 1:
#         if waktu == "Pagi" and (tipe == "Anak" or tipe =="Dewasa"):
#             paket = "A"
#         elif waktu == "Malam" and tipe == "Dewasa":
#             paket = "C"
#     case 2:
#         if waktu == "Pagi" and tipe == "Dewasa":
#             paket = "B"
#         elif waktu == "Malam" and tipe == "Dewasa":
#             paket = "C"
#     case 3:
#         if waktu == "Malam" and (tipe == "Anak" or tipe =="Dewasa"):
#             paket = "C"