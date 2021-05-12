#1
a = int(input('Lado A: '))
b = int(input('Lado B: '))
c = int(input('Lado C: '))
if a > (b + c) or b > (a + c) or c > (a + b):
    print ('Não pode ser um triângulo!')
else:
    print ('Pode ser um triângulo!')
    if a == b == c:
        print ('É equilátero!')
    elif lado_a == b or b == c or a == c:
        print ('É isósceles!')
    else:
        print ('É escaleno!')

#2
ano = int(input('Digite um ano: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print ('É um ano bissexto!')
else:
    print ('Não é ano bissexto!')
#3
peso = int(input('Qual é o peso dos peixes? '))
if peso > 50:
    excesso = peso - 50
    multa = 4 * (peso - 50)
    print('Excesso = %d quilos' %(excesso))
    print('Multa = R$%.2f' %(multa))
else:
    print('Excesso = ZERO')
    print('Multa = ZERO')
    
#4
a = int(input('Digite o 1° número: '))
b = int(input('Digite o 2° número: '))
c = int(input('Digite o 3° número: '))

if a > b and a > c:
    print('O 1° número é o maior')
elif b > a and b > c:
    print('O 2° número é o maior')
else:
    print('O 3° número é o maior')

#5
a = int(input('Digite o 1° número: '))
b = int(input('Digite o 2° número: '))
c = int(input('Digite o 3° número: '))

if a > b and a > c:
    print('O 1° número é o maior')
elif b > a and b > c:
    print('O 2° número é o maior')
else:
    print('O 3° número é o maior')

if a < b and a < c:
    print('O 1° número é o menor')
elif b < a and b < c:
    print('O 2° número é o menor')
else:
    print('O 3° número é o menor')

#6
salario_hora = int(input('Quanto você ganha por hora? '))
horas_mes = int(input('Quantas horas você trabalha por mês? '))
salario_bruto = salario_hora * horas_mes
print ('+ Salário Bruto : R$%.2f' %(salario_bruto))
i_r = salario_bruto * 0.11
print ('- IR : R$%.2f' %(i_r))
inss = salario_bruto * 0.08
print ('- INSS : R$%.2f' %(inss))
sind = salario_bruto * 0.05
print ('- Sindicato : R$%.2f' %(sind))
descontos = i_r + inss + sind
salario_liq = salario_bruto - descontos
print ('= Salário Líquido : R$%.2f' %(salario_liq))

#7
m = int(input('Qual o tamanho em metros quadrados da área a ser pintada? '))

if m % 54 != 0:
    latas = int(m / 54) + 1
else:
    latas = m / 54
valor = latas * 80
print('Quantidade de latas a serem compradas: %d' %(latas))
print('Preço total: R$%.2f' %(valor))

final = input('Aperte ENTER para sair')
print('Final do programa!')
print()
print()
print()
print()
