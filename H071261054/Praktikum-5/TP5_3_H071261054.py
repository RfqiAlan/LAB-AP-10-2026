ALFABET = "abcdefghijklmnopqrstuvwxyz"

def cek_sandi(ch,k):
    if ch.lower() in ALFABET:
        posisi_awal = ALFABET.find(ch.lower())
        posisi_baru = (posisi_awal + k) % 26
        karakter_baru = ALFABET[posisi_baru]
        
        if ch.isupper():
            return karakter_baru.upper()
        else:
            return karakter_baru
    return ch
    
def mesin_enkripsi(teks,k):
    hasil = ""
    for i in teks:
        hasil += cek_sandi(i,k)
        
    return hasil

def mesin_dekripsi(teks,k):
    return mesin_enkripsi(teks,k)
        
def retas_sandi(sandi,kata_kunci):
    hasil_peretasan = []
    
    for k in range(1,26):
        pesan_kemungkinan = ""
        
        for huruf in sandi:
            pesan_kemungkinan += cek_sandi(huruf, -k)
            # print(pesan_kemungkinan)
            
        if pesan_kemungkinan.find(kata_kunci) != -1:
            print(pesan_kemungkinan.find(kata_kunci))
            hasil_peretasan.append((k,pesan_kemungkinan))
                
    return hasil_peretasan
                    
    # print(hasil)
# sandi = input("Masukkan sandi: ")
# kata_kunci = input("Masukkan kata sandi")
print(retas_sandi("zfsl xzfu frfs", "suap")) # => "uang suap aman"