data = [5, 3, 8, 1, 2]

n = len(data)

for i in range(n - 1):
    for j in range(n - i - 1):
        if data[j] > data[j + 1]:
            data[j], data[j + 1] = data[j + 1], data[j]

print("Hasil pengurutan:", data)

a = 3
b = 5

a,b = b,a
print("Setelah ditukar")
print(a)
print(b)