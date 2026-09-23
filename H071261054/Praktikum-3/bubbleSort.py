data = [54, 56,23,45,78,33,21]

n = len(data)

for i in range(n-1):
    # print (i)
    for j in range(n - i - 1):
        # print(j)
        if data[j] > data[j + 1]:
            data[j], data[j + 1] = data[j + 1], data[j]
        print(data)        
# print(data)