from random import randint

vetor = [randint(1, 100) for x in range(20)]
pares = [x for x in vetor if x % 2 == 0]
ímpares = [x for x in vetor if x % 2 == 1]
print ('Vetor', vetor)
print ('Pares', pares)
print ('Ímpares', ímpares)
