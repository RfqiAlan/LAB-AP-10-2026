# inputnpresentase cabai
presentase_cabai = float(input("Masukkan presentase cabai (dalam persen): "))

# memerika input dan presentase cabai
if presentase_cabai < 10:
    print("Level Aman")
elif presentase_cabai <0:
    print("Presentase cabai tidak boleh negatif.")
elif presentase_cabai <= 40:
    print("Level Sedang")
elif presentase_cabai <= 70:
    print("Level Pedas")
else:
    print("Level Ekstrem")