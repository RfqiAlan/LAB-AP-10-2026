# input jarak dan pilihan layanan
jarak = float(input("Masukkan jarak (dalam km): "))
express = input("Apakah Anda ingin layanan express? (ya/tidak): ")

# menentukan tarif dasar
if jarak <= 0:
    tarif_dasar = 0
elif jarak <= 5:
    tarif_dasar = 10.000
elif jarak <= 20:
    tarif_dasar = 20.000
else:
    tarif_dasar = 35.000

# biaya tambahan untuk layanan express
express= 15.000 if express == "ya" else 0

# menghitung total biaya
total_biaya = tarif_dasar + express

# menampilkan hasil
print(f"total biaya: Rp {total_biaya:}")
print(express)