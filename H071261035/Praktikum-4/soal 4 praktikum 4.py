def konversi_suhu(suhu, asal, tujuan):
    asal = asal.upper()
    tujuan = tujuan.upper()
    skala_valid = ["C", "F", "K"]
    
    if asal not in skala_valid or tujuan not in skala_valid:
        raise ValueError("Skala suhu tidak dikenali.")
    
    if asal == "C":
        celsius = suhu
    elif asal == "F":
        celsius = (suhu - 32) * 5 / 9
    elif asal == "K":
        celsius = suhu - 273.15
        
    if tujuan == "C":
        return celsius
    elif tujuan == "F":
        return (celsius * 9 / 5) + 32
    elif tujuan == "K":
        return celsius + 273.15

print("=== Konversi Suhu ===")

while True:
    input_suhu = input("Masukkan suhu (atau 'selesai' untuk keluar): ")
    
    if input_suhu.lower() == "selesai":
        break
        
    suhu = float(input_suhu)

    while True:
        skala_asal = input("Skala asal (C/F/K): ")
        try:
            konversi_suhu(suhu, skala_asal, "C")
            break
        except ValueError as e:
            print(f"Error: {e}")

    while True:
        skala_tujuan = input("Skala tujuan (C/F/K): ")
        try:
            konversi_suhu(suhu, "C", skala_tujuan)
            break
        except ValueError as e:
            print(f"Error: {e}")