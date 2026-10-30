def bersihkan_teks(teks):
    teks_bersih = ""
    for karakter in teks:
        if karakter.isalnum():
            teks_bersih += karakter.lower()
            teks_bersih = ''.join([c for c in teks_bersih if not c.isdigit()])
    return teks_bersih

def cek_palindrom(teks):
    palindrom = bersihkan_teks(teks)
    palindrom = "".join(reversed(teks))
    if teks == palindrom:
        return True, -1
    
    for i in range(len(teks)):
        if teks[i] != palindrom[i]:
            pesan = (f"index {i} berbeda")
            return False, pesan
    # print(palindrom)
    
def inti_palindrom(teks):
    teks_bersih = bersihkan_teks(teks)
    len_teks = len(teks_bersih)
    
    if len_teks == 0:
        palindrom = {
            "teks" : "",
            "panjang" : 0,
            "index_awal" : -1
        }
        
    palindrom = {
        "teks" : teks_bersih[0],
        "panjang" : 1,
        "index_awal" : 0
    }
    
    for i in range(len_teks):
        for j in range(i + 1, len_teks + 1):
            substring = teks_bersih[i:j]
            
            if cek_palindrom(substring)[0]:
                panjang_sekarang = len(substring)
                
                if panjang_sekarang >= palindrom["panjang"]:
                    palindrom = {
                        "teks" : substring,
                        "panjang" : panjang_sekarang,
                        "index_awal" : i
                    }
    return palindrom
    
teks = input("Masukkan Teks : ")
teks_bersih = bersihkan_teks(teks)
print("Teks Bersih : ",teks_bersih)
palindrom = inti_palindrom(teks_bersih)    
print(f"Output Terharap {palindrom}")