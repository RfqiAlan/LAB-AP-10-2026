menu = ["Kopi Susu","Matcha Latte","Americano",]
harga = [18000, 22000, 15000]
jumlah = [4,3,5]

sub_kopi = harga[0] * jumlah[0]
sub_mathca = harga[1] * jumlah[1]
sub_americano = harga[2] * jumlah[2]
 
total_seluruh = sub_kopi + sub_mathca + sub_americano

biaya_operasional = 15000
pendapatan_bersih = total_seluruh - biaya_operasional

jumlah_barang = sum(jumlah)
target_tercapai = total_seluruh > 200000 and jumlah_barang > 10

print("\nLAPORAN PENJUALAN KOPI SENJA")
print("===========================================")
print(f"Sub Total untuk americano adalah : {sub_americano}")
print(f"Sub Total untuk matcha latte adalah : {sub_mathca}")
print(f"Sub Total untuk kopi latte adalah : {sub_kopi}")
print(f"\nTotal Seluruh adalah : {total_seluruh}")
print(f"Pendapatan Bersihnya adalah : {pendapatan_bersih}")
print(f"\nTargetnya its {target_tercapai}")
