print("="*25)
print("---Denah Kursi Bioskop---")
print("="*25)

baris = 1
while baris != 0:
    try:
        baris = int(input("Masukkan baris Item : "))
        
        # if baris < 0:
        #     print("baris tidak boleh negatif")   
        #     print("="*26,"\n") 
        
        # if baris > 0:
        kursi = int(input("Masukkan jumlah kursi : "))
            
        for i in range(1,baris + 1):
            # print(i)
            for j in range(1,kursi + 1):
                if j == 13:
                    continue
                
                if i == 1:
                    if j % 2 != 0:
                        print(f"baris {i} - kursi {j}")
                else:
                    print(f"baris {i} - kursi {j}")
        break
                    
    except ValueError:
        print("input harus berupa angka")
        print("="*26,"\n")