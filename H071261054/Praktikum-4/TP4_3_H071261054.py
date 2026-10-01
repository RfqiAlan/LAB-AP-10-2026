import time

angka_awal = int(input("Masukkan Angka Awal : "))
if angka_awal >= 0:
    for i in range(angka_awal, 0,1):
        print(i)
        time.sleep(1)
    print("luncurkan")
else:
    print('angka tidak boleh negatif')    