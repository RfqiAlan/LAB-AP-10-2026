sambal = int(input("Persentase sambal: "))
if 0 < sambal <= 10:
    print("Level Aman")
elif sambal >= 11 and sambal <= 40:
    print("Level Sedang")
elif sambal >= 41 and sambal <= 70:
    print("Level Pedas")
elif sambal > 70:
    print("Level Ekstrem")
else:
    print("Tidak jelas km")
