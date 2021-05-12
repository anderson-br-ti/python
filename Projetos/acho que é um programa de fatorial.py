n = int(input('Numero: '))
i = 1
k = 1
fat = [ ]
while len(fat) < n:
    i = i * k
    k = k + 1
    fat.append(i)
print (fat[-1])
