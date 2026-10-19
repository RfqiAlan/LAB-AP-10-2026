def cek_kata(teks, kata):
    teks_lower = teks.lower()
    kata_lower = kata.lower()
    indeks_list = []
    
    start = 0
    while True:
        pos = teks_lower.find(kata_lower, start)
        if pos == -1:
            break
        indeks_list.append(pos)
        start = pos + 1
    return indeks_list

def cek_batas_kata(teks, i, panjang):
    alfabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    if i > 0:
        char_sebelum = teks[i - 1]
        if char_sebelum in alfabet:
            return False
            
    if i + panjang < len(teks):
        char_sesudah = teks[i + panjang]
        if char_sesudah in alfabet:
            return False
            
    return True

def sensor_kata(teks, kata, simbol):
    indeks_awal_kata = cek_kata(teks, kata)
    panjang_kata = len(kata)
    
    indeks_valid = []
    for idx in indeks_awal_kata:
        if cek_batas_kata(teks, idx, panjang_kata):
            indeks_valid.append(idx)
            
    teks_hasil = ""
    i = 0
    while i < len(teks):
        if i in indeks_valid:
            teks_hasil += simbol * panjang_kata
            i += panjang_kata
        else:
            teks_hasil += teks[i]
            i += 1
            
    return (teks_hasil, len(indeks_valid), indeks_valid)

teks_input = input("Masukkan Teks: ")
kata_target = input("Masukkan kata target: ")
simbol_input = input("Masukkan simbol: ")

hasil_teks, jumlah, daftar_indeks = sensor_kata(teks_input, kata_target, simbol_input)

print("Hasil Teks:", hasil_teks)
print("Jumlah:", jumlah, " Indeks:", daftar_indeks)