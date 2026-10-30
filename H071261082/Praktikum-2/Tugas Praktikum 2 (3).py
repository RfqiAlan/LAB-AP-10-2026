#nomor 3
usia = int(input("Masukkan usia anda:  "))


if 30 <= usia <= 35 :
   print("Lolos ke tahap tes")
   nilai = int(input("Masukkan nilai tes:  "))
   if nilai >= 80 :
      print("Lolos ke Tahap Wawancara")
      exit()
      pengalaman = int(input("Masukkan pengalaman kerja (tahun):  "))
      if nilai >= 65 and pengalaman >= 2 :
         print("Lolos Bersyarat")
else :
   print("Tidak lolos")