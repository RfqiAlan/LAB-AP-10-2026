# Nomor 2
print("TARIF PENGIRIMAN BARANG")
print("=======================")
print("< 5km : Rp.10.000")
print("5km - 10km : Rp.20.000")
print("> 10km : Rp.35.000")
print("=======================")

tarif = 0

jarak = int(input("Masukkan jarak pengiriman (km) : "))
if 0<jarak<5:
    tarif += 10000
elif 5<jarak<=10:
    tarif += 20000
elif jarak>10:
    tarif += 35000
else:
    print("Jarak Tidak Valid")
    exit()

express = input("Layanan express (ya/tidak) : ")
tarif = tarif + 15000 if express == "ya" else tarif

print("Total Tarif Pengiriman : ", tarif)