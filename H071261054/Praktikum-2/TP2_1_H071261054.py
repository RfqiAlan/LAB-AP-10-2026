# Nomor 1
print("TINGKAT KEPEDASAN")
print("========================")
print("Level Aman (0% - 10%)")
print("Level Sedang (11% - 40%)")
print("Level Pedas (41% - 70%)")
print("Level Esktrem (> 70%)")
print("========================")

presentase = int(input("Masukkan persentase cabai : "))
# if 0<=presentase<=10:
#     print("Level Aman")
# elif 10<presentase<=40:
#     print("Level Sedang")
# elif 40<presentase<=70:
#     print("Level Pedas")
# elif presentase>70:
#     print("Level Ekstrem")
# else:
#     print("Persentase Tidak Valid")

if presentase > 0 and presentase <= 10:
    print("Level Aman")
elif presentase > 10 and presentase <=40:
    print("Level Sedang")
elif presentase > 40  and presentase <= 70:
    print("Level Pedas")
elif presentase > 70:
    print("Level Ekstrem")
else:
    print("Presentase Tidak Valid")

# ubah semua jadi AND

