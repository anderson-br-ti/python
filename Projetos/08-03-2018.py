'''a = int(input('Digite um número inteiro: '))
x = 1
while x <= a:
    print (x)
    x = x + 1


n = int(input('Digite um número inteiro: '))
p = 0
while p <= n:
    if p % 2 == 0:
        print (p)
    p = p + 1

n = 30
p = 3
while p <= n:
    print (p)
    p = p + 3

n = 1
soma = 0
while n <= 10:
    x = float(input('Digite o %d° número: ' %(n)))
    soma = soma + x
    n = n + 1
print ('Média: %.2f' %(soma/10))
'''
#incompleto
'''n = 1
soma = 0
while n <= 10:
    x = float(input('Digite o %d° número: ' %(n)))
    soma = soma + x
    n = n + 1
print (f''Média:{soma/10 :.2f}'')'''
#incompleto
'''
n = int(input('Número inteiro positivo: '))
fat = 1
while fat <= n:
    fat = fat * n
    n = n + 1
print ('Fatorial(%d): %d' %(n, fat))

soma = 0
while True:
    x = int(input('Digite o número (0 sai): '))
    if x == 0:
        break
    soma = soma + x
print ('Soma: %d' %(soma))'''

tabuada = 1
while tabuada <= 10:
    n = 1
    print ('Tabuada do %d' %(tabuada))
    while n <= 10:
        print ('%d x %d = %d' %(tabuada, n, tabuada * n))
        n = n + 1
    tabuada = tabuada + 1
    
