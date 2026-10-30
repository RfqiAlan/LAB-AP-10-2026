jarak = float(input("Masukkan jarak pengiriman: "))
express = input("Layanan express (ya/tidak): ")

if jarak == 5:
    jarak = 10000
elif jarak ==20:
    jarak = 20000
elif jarak == 25:
    jarak = 35000
else:
    print("Input tidak valid")
    

biaya_tambahan = 15000 if express == "ya" else 0
total = biaya_tambahan + jarak






