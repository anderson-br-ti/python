n = int(input('n: '))
lista = [ ]
import random
while len (lista) < n:
    x = random.randint(1, 100)
    if x not in lista:
        lista.append(x)
print (lista)
