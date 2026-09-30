print("Selamat Datang Di Kasir Minimarket")

def sub_total(harga,jumlah,diskon=0.0):
    total_belanja = harga * jumlah
    potongan = total_belanja * diskon
    subtotal = total_belanja - potongan
    return subtotal

def proses_belanja_barang(is_member=False):
    harga_barang = int(input("Masukkan Harga Barang : "))
    jumlah_barang = int(input("Masukkan Jumlah Barang : "))
    
    nilai_diskon = 0.0 if is_member == False else 0.10
    
    subtotal_harga = sub_total(harga_barang,jumlah_barang, nilai_diskon)
    return subtotal_harga

total_belanja = 0
is_member = input("apakah anda member? (y/n)").lower()
while True:
    if is_member == 'y':
        nama_barang = input("Masukkan Nama Barang(kosongkan untuk memberhentikan) : ")
        if nama_barang:
            subtotal_harga = proses_belanja_barang(is_member=True)
            total_belanja += subtotal_harga
            print(f"Subtotal {nama_barang}: Rp.{subtotal_harga}")
        else:
            print("total belanja : ",total_belanja)
            break
    elif is_member == 'n':
        nama_barang = input("Masukkan Nama Barang(kosongkan untuk memberhentikan) : ")
        if nama_barang:
            subtotal_harga = proses_belanja_barang()
            total_belanja += subtotal_harga
            print(f"Subtotal {nama_barang}: Rp.{subtotal_harga}")
        else:
            print("total belanja : Rp.",total_belanja)
            break
    else:
        print("keyword tidak ada")
        
            
        