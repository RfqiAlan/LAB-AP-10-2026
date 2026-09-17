jarak = int(input("Masukkan jarak pengiriman (km) :"))
layanan = (input("Layanan express (ya/tidak) :"))

 
if jarak < 5 :
    tarif = 10000
elif jarak >= 5 and jarak <=20:
    tarif = 20000
elif jarak >20:
    tarif = 35000
else:
    print("Input tidak valid")

biaya_express = 15000 if layanan == "ya" else 0

total_tarif = tarif + biaya_express

print(f"Total tarif pengiriman: Rp{total_tarif}")