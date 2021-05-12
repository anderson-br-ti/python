lista = [ ]
k = 0
n = 0
while k < 10:
    consoante = input ('Digite uma letra: ')
    lista.append(consoante)
    if consoante not in 'aeiou':
        n = n + 1
    k = k + 1
print(n)
print(lista)
