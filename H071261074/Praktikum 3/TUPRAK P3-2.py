print("---Setup Denah Bioskop NontonYuk---")
while True:
  try:
    baris = int(input("Masukkan jumlah baris:  "))
    if baris <= 0:
      print("Jumlah baris harus lebih dari 0")
    else:
      break
  except:
    print("Input baris harus berupa angka")
while True:
  try:
    kursi = int(input("Masukkan jumlah kursi:  "))
    if kursi <= 0:
      print("Jumlah kursi harus lebih dari 0")
    else:
      break
  except:
    print("Input kursi harus berupa angka")
bioskop = baris and kursi
if bioskop >0:
  n = 1
  while n <= baris:
    m = 1
    while m <= kursi:
      if m == 13:
        m+= 1
        continue
      elif n == 1 and m % 2 == 0:
        m+= 1
        continue
      print(f"Baris {n} - Kursi {m}")
      m+=1
    n+= 1