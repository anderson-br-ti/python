#1
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
print ('Soma = %d' %(n1+n2))
#2
m = float(input('Digite um valor em metros: '))
print ('Isso equivale a %.2f milímetros.' %(m*1000))
#3
dias = int(input('Digite a quantidade de dias: '))
horas = int(input('Digite a quantidade de horas: '))
minutos = int(input('Digite a quantidade de minutos: '))
segundos = int(input('Digite a quantidade de segundos: '))
total = segundos + (minutos * 60) + ((horas * 60) * 60) + (((dias * 24) * 60) * 60)
print ('Isso equivale a %d segundos' %total)
#4
salário = int(input('Digite o valor do salário: '))
pctg_aumt = int(input('Digite a porcentagem do aumento: '))
aumento = salário * (pctg_aumt / 100)
novo_salário = salário + aumento
print ('Aumento = R$%.2f' %(aumento))
print ('Novo salário = R$%.2f' %(novo_salário))
#5
mercado_ = int(input('Digite o preço da mercadoria: '))
desconto = int(input('Digite o percentual de desconto: '))
valor_desct = mercado_ * (desconto / 100)
preço = mercado_ - valor_desct
print ('Desconto = R$%.2f' %(valor_desct))
print ('Preço a pagar = R$%.2f' %(preço))
#6
distância = int(input('Qual é a distância a percorrer?: '))
vm = int(input('Qual é a velocidade média esperada para a viagem?: '))
tempo = distância / vm
print ('Tempo da viagem: %.2fh' %(tempo))
#7
C = int(input('Digite a temperatura em °C: '))
F = 9 * C / 5 + 32
print ('Equivale a %.2f°F' %(F))
#8
F = int(input('Digite a temperatura em °F: '))
C = (F - 32) / 1.8
print ('Equivale a %.2fºC' %(C))
#9
km = int(input('Quantos km foram percorridos?: '))
dias = int(input('Por quantos dias o carro foi alugado? '))
preco = (km * 0.15) + (dias * 60)
print ('R$%.2f' %(preco))
#10
cigarros = int(input('Cigarros por dia: '))
anos = int(input('Anos que fumou: '))
total_cigarros = (anos * 365) * cigarros
dias_perdidos = (total_cigarros * 10) / 24
print ('O fumante perdeu %d dias' %(dias_perdidos))
#11
print (len(str(2**1000000)))
