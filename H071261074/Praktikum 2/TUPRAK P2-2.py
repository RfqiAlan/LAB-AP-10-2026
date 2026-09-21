jarak = int(input("Masukkan jarak pengiriman(km): "))
express = (input("Layanan Express (ya/tidak): ")).capitalize()

if jarak == 0:
    print("Gratis ongkir voucher shopee")
elif jarak > 0 and jarak <5 : 
    tarif = 10000
elif jarak >= 5 and jarak <= 20:
    tarif = 20000
elif jarak > 20 : 
    tarif = 35000
else: 
    jarak < 0
    print("TIDAK VALIDD")

if jarak > 0:
    tambahan = 15000 if express == "Ya" else 0
    total = tarif + tambahan
    print("Total tarif pengiriman:Rp", total)
    print(tambahan)