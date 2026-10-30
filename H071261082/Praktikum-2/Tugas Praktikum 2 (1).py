#nomor 1
level_pedas = float(input("Masukkan Persentase Cabai:  "))

if  level_pedas < 0  :
   print("Input tidak valid, tidak boleh dari 0")
elif level_pedas > 100 :
    print("Input tidak valid,tidak boleh dari 100")
elif level_pedas  <= 10 :
   print("Level Aman")
elif  11 <= level_pedas <= 40 :
   print("Level Sedang")
elif 41 <= level_pedas <= 70 :
   print("level pedas")
else :
   print("level ekstrem")

print(level_pedas)
