level_pedas = int(input("masukkan persentase"))

if level_pedas >= 0 and level_pedas <= 10:
    print("level aman")
elif level_pedas >= 11 and level_pedas <= 40:
    print("level sedang")
elif level_pedas >= 41 and level_pedas <= 70:
    print("level pedas")
elif level_pedas >= 71 and level_pedas <= 100:
    print("level ekstrem")
else: 
    print("input tidak valid")