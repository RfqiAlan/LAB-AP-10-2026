ALFABET = "abcdefghijklmnopqrstuvwxyz"

def cek_sandi(ch, k):
    ch_lower = ch.lower()
    if ch_lower not in ALFABET:
        return ch
    
    idx = ALFABET.find(ch_lower)
    idx_baru = (idx + k) % 26
    hasil = ALFABET[idx_baru]
    
    return hasil.upper() if ch.isupper() else hasil

def mesin_enkripsi(teks, k):
    return "".join(cek_sandi(ch, k) for ch in teks)

def mesin_dekripsi(teks, k):
    return mesin_enkripsi(teks, k)

def retas_sandi(sandi, kata_kunci):
    hasil = []
    for k in range(26):
        teks_dekripsi = mesin_dekripsi(sandi, k)
        if kata_kunci in teks_dekripsi:
            hasil.append((k, teks_dekripsi))
    return hasil

pesan_tersita = input("Masukkan pesan tersita (enkripsi Caesar): ")
kata_kunci = input("Masukkan kata kunci target: ")

output = retas_sandi(pesan_tersita, kata_kunci)
print("Output Deskripsi:", output)