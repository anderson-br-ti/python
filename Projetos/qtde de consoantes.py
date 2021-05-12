contad = 0
n = 0
while contad < 10:
    cons = input ('Digite uma letra: ')
    if cons not in 'aeiou':
        n = n + 1
    contad = contad + 1
print(n)
