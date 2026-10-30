def konversi_suhu(suhu, asal, tujuan):
    """Mengonversi suhu antara C, F, dan K. Skala salah -> raise ValueError."""
    if asal not in ("C", "F", "K") or tujuan not in ("C", "F", "K"):
        raise ValueError("Skala suhu tidak dikenali.")

    if asal == "C":
        celsius = suhu
    elif asal == "F":
        celsius = (suhu - 32) * 5 / 9
    else:
        celsius = suhu - 273.15

    if tujuan == "C":
        hasil = celsius
    elif tujuan == "F":
        hasil = celsius * 9 / 5 + 32
    else:
        hasil = celsius + 273.15

    return round(hasil, 2)


print("=== Konversi Suhu ===")
while True:
    teks = input("Masukkan suhu (atau 'selesai' untuk keluar): ")
    if teks.lower() == "selesai":
        break
    try:
        suhu = float(teks)
    except ValueError:
        print("Error: Suhu harus berupa angka.")
        continue

    asal = input("Skala asal (C/F/K): ").upper()
    tujuan = input("Skala tujuan (C/F/K): ").upper()

    try:
        hasil = konversi_suhu(suhu, asal, tujuan)
        print(f"Hasil: {suhu} {asal} = {hasil} {tujuan}")
    except ValueError:
        print("Error: Skala suhu tidak dikenali.")