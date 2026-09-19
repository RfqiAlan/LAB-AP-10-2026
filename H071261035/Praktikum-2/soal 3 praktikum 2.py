# input nilai tes dan pengalaman kerja
nilai_tes = float(input("Masukkan nilai: "))
pengalaman_kerja = float(input("Masukkan pengalaman kerja (dalam tahun): "))

# menentukan kelulusan
if nilai_tes >= 80:
    print("Lolos ke tahap wawancara")
elif nilai_tes >= 65 and pengalaman_kerja >= 2:
    print("Lolos bersyarat'")
else:
    print("Tidak lolos")