import re

list_no_mentah = []
list_no_valid = []
def bersihkan_no(list_mentah, list_valid):
    hilangkan = r'[- ]'
    replace = ""
    pattern_validasi = r'^08\d{8,11}$'
    
    for idx, item in enumerate(list_mentah, 1):
        if re.match(r"^\+62", item):
            no_baru = re.sub(r'^\+62', '0', item)
        else:
            no_baru = item
        no_bersih = re.sub(hilangkan, replace, no_baru)
        is_valid_no = re.match(pattern_validasi, no_bersih)
        if is_valid_no:
            list_valid.append(no_bersih)
        print(f"\nData: {idx}")  
        print(f"Sebelum : {item}")
        print(f"Sesudah : {no_bersih}")
        print(f"Status  : {'Valid' if is_valid_no else 'Tidak Valid'}")  
    
    
batas = 1
jumlah = int(input("Jumlah Nomor : "))
while batas <= jumlah:
    nomor = input("\nMasukkan Nomor : ")
    list_no_mentah.append(nomor)
    batas += 1
    
bersihkan_no(list_no_mentah, list_no_valid)

print("=== Hasil Akhir Nomor Valid ===")
print(f"{len(list_no_valid)}")