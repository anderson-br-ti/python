import random

vetor = []
for k in range(20):
  vetor.append(random.randint(1, 100))

pares = []
ímpares = []
for x in vetor:
  if x % 2 == 0:
    pares.append(x)
  else:
    ímpares.append(x)
    
print ('Vetor', vetor)
print ('Pares', pares)
print ('Ímpares', ímpares)
