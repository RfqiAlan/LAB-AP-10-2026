import datetime
import random
import os

def tambah_produk():
    nama_produk = input("Masukkan Nama Produk: ")
    harga = int(input("Masukkan Harga: "))
    jumlah = int(input("Masukkan Jumlah: "))
    
    return {
        "nama" : nama_produk,
        "harga" : harga,
        "jumlah" : jumlah
    }

def format_file(nama_kasir):
    inisial = "".join([kata[0].upper() for kata in nama_kasir.split()])
    sekarang = datetime.datetime.now()
    dua_digit_tahun = sekarang.strftime("%y")
    dua_digit_bulan = sekarang.strftime("%m")
    dua_digit_tanggal = sekarang.strftime("%d")
    jam = sekarang.strftime("%H")
    menit = sekarang.strftime("%M")
    angka_random = str(random.randint(100,999))
    
    format = inisial + dua_digit_tahun + dua_digit_bulan + dua_digit_tanggal + jam + menit + angka_random
    return format

def create_invoice(keranjang, nama_kasir):
    nama_file = format_file(nama_kasir)
    lokasi = f"invoice/{nama_file}"
    total_bayar = sum(produk["harga"] * produk["jumlah"] for produk in keranjang)
    waktu_sekarang = datetime.datetime.now().strftime("%d/%m/%y %H:%M")
    
    os.makedirs("invoice", exist_ok=True)
    
    with open(lokasi, "a") as f:
        lebar_struk = 67
        garis_ganda = "=" * lebar_struk + "\n"

        f.write(f"{'TOKO KELVIN':^{lebar_struk}}\n")
        f.write(garis_ganda)

        f.write(f"Nama kasir      : {nama_kasir}\n")
        f.write(f"Waktu transaksi : {waktu_sekarang}\n")
        f.write(garis_ganda)

        f.write(f"\n{'Daftar Produk':^{lebar_struk}}\n\n")

        f.write(garis_ganda)
        f.write(f"| {'Nama':^20} | {'Harga':^12} | {'Jumlah':^8} | {'Total':^15} |\n")
        f.write(garis_ganda)

        for item in keranjang:
            total_item = item['harga'] * item['jumlah']
            txt_harga = f"Rp{item['harga']}"
            txt_total = f"Rp{total_item}"

            f.write(f"| {item["nama"]:<20} | {txt_harga:>12} | {item['jumlah']:^8} | {txt_total:>15} |\n")

        f.write(garis_ganda)
        txt_total_bayar = f"Rp{total_bayar}"
        f.write(f"| {'TOTAL':^20} | {'':12} | {'':8} | {txt_total_bayar:>15} |\n")
        f.write(garis_ganda)

        f.write("\n" + garis_ganda)
        f.write(f"{'TERIMA KASIH TELAH BERBELANJA':^{lebar_struk}}\n")
        f.write(garis_ganda)
        
    return nama_file, waktu_sekarang, total_bayar