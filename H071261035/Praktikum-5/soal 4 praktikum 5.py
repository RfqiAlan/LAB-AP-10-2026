def deteksi_anomali_email(email):
    anomali = []
    
    jumlah_at = 0
    for char in email:
        if char == "@":
            jumlah_at += 1
    if jumlah_at != 1:
        anomali.append("Harus memiliki tepat satu karakter @.")
        
    if " " in email:
        anomali.append("Tidak boleh mengandung spasi.")
        
    if jumlah_at == 1:
        pos_at = email.find("@")
        local = email[:pos_at]
        domain = email[pos_at + 1:]
        
        if local == "" or domain == "":
            anomali.append("Bagian sebelum @ (local) atau setelah @ (domain) tidak boleh kosong.")
            
        if local != "":
            if local[0] == "." or local[-1] == ".":
                anomali.append("Bagian local tidak boleh diawali atau diakhiri titik.")
            if ".." in local:
                anomali.append("Bagian local tidak boleh mengandung titik berurutan.")
                
        if domain != "":
            if "." not in domain:
                anomali.append("Bagian domain wajib memiliki minimal satu titik.")
            if ".." in domain or domain[-1] == ".":
                anomali.append("Bagian domain tidak boleh mengandung titik berurutan atau diakhiri titik.")
                
        if not (domain.endswith(".com") or domain.endswith(".id") or domain.endswith(".ac.id")):
            anomali.append("Wajib berakhiran dengan .com, .id, atau .ac.id")
            
    return anomali

def cetak_daftar(daftar_email_valid, karakter_border):
    if not daftar_email_valid:
        return ""
        
    panjang_maks = 0
    for email in daftar_email_valid:
        if len(email) > panjang_maks:
            panjang_maks = len(email)
            
    lebar_bingkai = panjang_maks + 4
    garis_border = karakter_border * lebar_bingkai
    
    hasil = garis_border + "\n"
    hasil += "HASIL EMAIL VALID\n"
    hasil += garis_border + "\n"
    
    for email in daftar_email_valid:
        spasi_sisa = panjang_maks - len(email)
        baris = "| " + email + (" " * spasi_sisa) + " |\n"
        hasil += baris
        
    hasil += garis_border
    return hasil

print("--- Sistem Pencatatan email valid ---")
border = input("Masukkan border dengan karakter bebas: ")
print("Ketik 'tutup' untuk mengakhiri masukan dan mencetak email.")

daftar_valid = []

while True:
    email_input = input("Masukkan email: ")
    
    if email_input.lower() == "tutup":
        break
        
    if email_input in daftar_valid:
        print(">> Email DITOLAK karena:")
        print("Email sudah terdaftar (Duplikat).")
        continue
        
    pelanggaran = deteksi_anomali_email(email_input)
    
    if len(pelanggaran) == 0:
        daftar_valid.append(email_input)
        print(">> Email VALID!")
    else:
        print(">> Email DITOLAK karena:")
        for err in pelanggaran:
            print(err)

print(cetak_daftar(daftar_valid, border))