def cek_kata(teks,kata):
    teks_lower = teks.lower()
    kata_lower = kata.lower()
    
    index_list = []
    start = 0
    
    while True:
        posisi = teks_lower.find(kata_lower,start)
        
        if posisi == -1:
            break
        
        index_list.append(posisi)
        
        start = posisi + 1
    
    return index_list

def cek_batas_kata(teks,i,panjang):
    kiri_aman = False
    if i == 0:
        kiri_aman = True
    else:
        char_kiri = teks[i - 1]
        
        if not (("a" <= char_kiri <= "z") or ("A" <= char_kiri <= "Z")):
            kiri_aman = True
            
    kanan_aman = False
    
    if i + panjang == len(teks):
        kanan_aman = True
    else:
        char_kanan = teks[i + panjang]
        print(char_kanan)
        if not (("a" <= char_kanan <= "z") or ("A" <= char_kanan <= "Z")):
            kanan_aman = True
            
    if kiri_aman and kanan_aman:
        print(True)
        return True
    else:
        print(False)
        return False
        

def sensor_kata(teks,kata,sensor):
    index_kata = cek_kata(teks,kata)
    panjang_kata = len(kata)
    index_kata_valid = []
    
    for i in index_kata:
        if cek_batas_kata(teks,i,panjang_kata):
            index_kata_valid.append(i)
    
    teks_sensor = sensor * panjang_kata
    
    teks_tersensor = teks
    for index_awal in index_kata_valid:
        index_akhir = index_awal + panjang_kata
        
        teks_tersensor = teks_tersensor[:index_awal] + teks_sensor + teks_tersensor[index_akhir:]
        print(teks_tersensor)
        # print(kata_sensor)
        

print(sensor_kata("saya imran anjay imranuddin", "imran", '#'))

# teks = input("Masukkan Teks: ")
# kata = input("Masukkan Kata: ")