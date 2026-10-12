def deteksi_anomali_email(email):
    if email.count("@") != 1:
        return ["Harus memiliki tepat satu karakter @."]

    galat = []
    local, domain = email.split("@")

    if local == "" or domain == "":
        galat.append("Bagian sebelum @ (local) atau setelah @ (domain) tidak boleh kosong.")
    if " " in email:
        galat.append("Tidak boleh mengandung spasi di posisi manapun.")
    if local.startswith(".") or local.endswith(".") or ".." in local:
        galat.append("Bagian local tidak boleh diawali/diakhiri titik atau mengandung titik berurutan (..).")
    if "." not in domain:
        galat.append("Bagian domain wajib memiliki minimal satu titik.")
    if ".." in domain or domain.endswith("."):
        galat.append("Bagian domain tidak boleh mengandung titik berurutan atau diakhiri titik.")
    if not email.endswith((".com", ".id", ".ac.id")):
        galat.append("Wajib berakhiran dengan .com, .id, atau .ac.id")

    return galat


def cetak_daftar(daftar_email_valid, karakter_border):
    terpanjang = max(len(e) for e in daftar_email_valid)
    garis = "+" + karakter_border * (terpanjang + 2) + "+"
    baris = [f"| {e.ljust(terpanjang)} |" for e in daftar_email_valid]
    return "\n".join([garis] + baris + [garis])


print("--- Sistem Pencatatan email valid ---")
border = input("Masukkan border dengan karakter bebas: ")
print("\nKetik 'tutup' untuk mengakhiri masukan dan mencetak email.")

daftar_valid = []
while True:
    email = input("Masukkan email: ")
    if email == "tutup":
        break

    alasan = deteksi_anomali_email(email)
    if not alasan and email in daftar_valid:
        alasan.append("Email sudah terdaftar (Duplikat).")

    if alasan:
        print(">> Email DITOLAK karena:")
        for a in alasan:
            print("   -", a)
    else:
        print(">> Email VALID!")
        daftar_valid.append(email)

print("\n--- HASIL EMAIL VALID ---")
if daftar_valid:
    print(cetak_daftar(daftar_valid, border))
else:
    print("Tidak ada email valid.")