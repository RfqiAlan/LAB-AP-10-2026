
def cek_batas_kata(teks, i, panjang):
    sebelum = teks[i-1] if i > 0 else " "
    sesudah = teks[i+panjang] if i+panjang < len(teks) else " "
    return not sebelum.isalpha() and not sesudah.isalpha()
    

def cek_kata(teks, kata):
    indeks = []
    for i in range(len(teks) - len(kata) + 1):
        if teks[i:i+len(kata)].lower() == kata.lower():
            if cek_batas_kata(teks, i, len(kata)):
                indeks.append(i)
    return indeks


def sensor_kata(teks, kata, simbol):
    indeks = cek_kata(teks, kata)
    hasil = ""
    i = 0

    while i < len(teks):
        if i in indeks:
            hasil += simbol * len(kata)
            i += len(kata)
        else:
            hasil += teks[i]
            i += 1

    return hasil, len(indeks), indeks


teks = input("Masukkan Teks: ")
kata = input("Masukkan kata target: ")
simbol = input("Masukkan simbol: ")

hasil, jumlah, indeks = sensor_kata(teks, kata, simbol)
print("Hasil Teks:", hasil)
print("Jumlah:", jumlah, "| Indeks:", indeks)