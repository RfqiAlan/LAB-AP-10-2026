def bersihkan_teks(teks):
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    teks_bersih = ""
    for char in teks:
        char_lower = char.lower()
        if char_lower in alfabet:
            teks_bersih += char_lower
    return teks_bersih

def cek_palinrome(teks):
    teks_dibalik = "".join(reversed(teks))
    if teks == teks_dibalik:
        return (True, -1)
    else:
        for i in range(len(teks)):
            if teks[i] != teks_dibalik[i]:
                return (False, i)

def inti_palinrome(teks):
    teks_b = bersihkan_teks(teks)
    n = len(teks_b)
    
    palindrom_terpanjang = ""
    indeks_awal = 0
    panjang_maks = 0
    
    for i in range(n):
        for j in range(i + 1, n + 1):
            sub = teks_b[i:j]
            is_palin, _ = cek_palinrome(sub)
            if is_palin:
                if len(sub) > panjang_maks:
                    panjang_maks = len(sub)
                    palindrom_terpanjang = sub
                    indeks_awal = i
                    
    return {"teks": palindrom_terpanjang,
        "panjang": panjang_maks,
        "indeks_awal": indeks_awal}

input_teks = input("Masukkan teks prasasti: ")
teks_bersih = bersihkan_teks(input_teks)
hasil = inti_palinrome(input_teks)

print("Teks Bersih:", teks_bersih)
print("Output Terharap:", hasil)