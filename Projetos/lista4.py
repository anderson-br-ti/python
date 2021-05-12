import random
v = [ ]
for k in range (1, 10):
    v.append (random.randint (1, 100))

menor = maior = v[0]
for k in range (1, 10):
    if v[k] > maior:
        maior = v[k]
    if v[k] < menor:
        menor = v[k]

print (f' maior = {maior} menor = {menor} ') 
