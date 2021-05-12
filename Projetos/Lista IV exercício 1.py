from random import randint
vetor = []
for k in range(10):
  vetor.append(randint(1, 100))

maior = menor = vetor[0]

k = 1
while k < 10:
  if vetor[k] > maior:
    maior = vetor[k]
  if vetor[k] < menor:
    menor = vetor[k]
  k = k + 1
  
print ('Vetor:', vetor)
print ('Maior: %d' %maior)
print ('Menor: %d' %menor)

