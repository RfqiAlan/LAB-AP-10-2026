def cek_sandi(ch, k):
    ALFABET = "abcdefghijklmnopqrstuvwxyz"
    ch_lower = ch.lower()
    
    idx = ALFABET.find(ch_lower)
    if idx == -1:
        return ch
        
    idx_baru = (idx + k) % 26
    karakter_baru = ALFABET[idx_baru]
    
    if ch.isupper():
        return karakter_baru.upper()
    else:
        return karakter_baru.lower()

def mesin_enkripsi(teks, k):
    hasil = ""
    for char in teks:
        hasil += cek_sandi(char, k)
    return hasil

def mesin_dekripsi(teks, k):
    return mesin_enkripsi(teks, -k)

def retas_sandi(sandi, kata_kunci):
    hasil_retas = []
    for k in range(26):
        teks_dekripsi = mesin_dekripsi(sandi, k)
        if teks_dekripsi.lower().find(kata_kunci.lower()) != -1:
            hasil_retas.append((k, teks_dekripsi))
    return hasil_retas

sandi_input = input("Masukkan pesan tersita (enkripsi Caesar): ")
kata_kunci_input = input("Masukkan kata kunci target: ")

output = retas_sandi(sandi_input, kata_kunci_input)
print("Output Deskripsi:", output)