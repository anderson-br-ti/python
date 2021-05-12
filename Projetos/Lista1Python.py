#Lista1
#Exercício1
n1 = int(input('1o numero: '))
n2 = int(input('2o numero: '))
print (n1+n2)

#Exercício2
metros = int(input('Valor em metros: '))
print (metros * 1000)

#Exercício3
dias = int(input('Dias: '))
horas = int(input('Horas: '))
minutos = int(input('Minutos: '))
segundos = int(input('Segundos: '))
total = segundos + (minutos * 60) + (horas * 3600) + (dias * 86400)
print (total)

#Exercício4
salario = int(input('Valor do salário: '))
aumento = int(input('Porcentagem do aumento: '))
print (salario * (aumento/100))
print (salario + (salario * (aumento/100)))

#Exercício5
preco = int(input('Preço da mercadoria: '))
desconto = int(input('Percentual de desconto: '))
print (preco * (desconto/100))
print (preco - (preco * (desconto/100)))

#Exercício6
distancia = float(input('Distância: '))
vm = float(input('Velocidade média: '))
tempo = distancia / vm
print ('O tempo será de %.2f horas!' %tempo)

#Exercício7
c = int(input('Temperatura em Celsius: '))
f = 9 * c / 5 + 32
print ('%.2f' %f)

#Exercício8
f = int(input('Temperatura em Fahrenheit: '))
print ('Isso equivale a %.2fºC' % ((f - 32) / 1.8))

#Exercício9
km = int(input('Km percorridos: '))
dias = int(input('Por quantos dias o carro foi alugado? '))
preco = (km * 0.15) + (dias * 60)
print ('R$%.2f' % preco)

#Exercício10
cigarros = int(input('Cigarros por dia: '))
anos = int(input('Anos que fumou: '))
total_cigarros = (anos * 365) * cigarros
dias_perdidos = (total_cigarros * 10) / 24
print ('O fumante perdeu %d dias' % dias_perdidos)

#Exercício11
print(len(str(2**1000000)))
