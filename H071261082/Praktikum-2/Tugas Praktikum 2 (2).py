#nomor 2 
Jarak = int(input("Masukkan Jarak Pengiriman:  "))
Layanan = input("Layanan Express (ya/tidak):  ")
if Jarak < 0 :
   print("invalid")
   exit()
if Jarak < 5 :
   harga = 10000
elif Jarak <= 20 :
   harga = 20000
else : 
   harga = 35000

Layanan = 15000 if Layanan == "ya" else 0
tarif = harga + Layanan
print(f"Harga total Pengiriman : Rp{tarif}")
