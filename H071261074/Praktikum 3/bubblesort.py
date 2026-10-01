def bubble_sort(arr):
    n = len(arr)
    
    # Perulangan untuk setiap elemen dalam list
    for i in range(n):
        swapped = False
        
        # Perulangan untuk membandingkan elemen yang bersebelahan
        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:
                # Menukar posisi jika urutannya salah
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                
        # Jika tidak ada pertukaran, berarti data sudah terurut
        if not swapped:
            break
            
    return arr

# --- Contoh Penggunaan Program ---
data_angka = [64, 34, 25, 12,]

print("Data sebelum diurutkan:", data_angka)

# Memanggil fungsi bubble_sort
hasil_urut = bubble_sort(data_angka)

print("Data setelah diurutkan:", hasil_urut)

a = 2
b = 3
a,b = b,a
print(a)
print(b)