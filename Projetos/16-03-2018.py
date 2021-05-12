'''palavra = input('Digite uma palavra: ')
cont = 0
while cont < len(palavra):
    print (palavra[cont])
    cont = cont + 1


lista = [3, 1, 10, 2]
cont = 0
while cont < len(lista):
    print (lista[cont])
    cont = cont + 1

n = int(input('Digite um número inteiro: '))
cont = 1
while cont <= n:
        print(cont)
        cont += 1


print ('Soma')
n = int(input('Digite um número inteiro: '))
soma = 0
cont = 1
while cont <= n:
        soma = soma + cont
        cont += 1
print (soma)

print ('Fatorial')
n = int(input('Digite um número inteiro: '))
fat = 1
cont = 1
while cont <= n:
        fat = fat * cont
        cont += 1
print (fat)

for x in 'Lionel':
    print (x)

for k in [0, 2, 4, 6, 8]:
    print (k)

soma = 0
for k in [1, 2, 3, 4, 5]:
    soma = soma + k
print (soma)

n = int(input('n: '))
s = 0
for k in range (1, n+1):
    s = s + k
print (s)

soma = 0
for k in [1, 2, 34, 5]:
    soma = soma + k
print (soma)

n = int(input('n: '))
f = 1
for x in range (1, n+1):
    f = f * x
print (f)

def fat(n):
    f = 1
    for x in range (1, n+1):
        f = f * x
    return fat
'''
#pesquisar o erro

