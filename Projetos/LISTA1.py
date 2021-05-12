#PRIMEIROLISTA1
'''m = int(input('Digite um número: '))
k = int(input('Digite outro número: '))
print ('Soma = %d' %(m + k))'''
#SEGUNDOLISTA1
'''m = int(input('Digite um valor em metros: '))
print ('Isso equivale a %d milímetros' %(m*1000))'''
#TERCEIROLISTA1
dias = int(input('Digite a quantidade de dias: '))
horas = int(input('Digite a quantidade de horas: '))
minutos = int(input('Digite a quantidade de minutos: '))
segundos = int(input('Digite a quantidade de segundos: '))
#comentando fica  calculo seg         calculo seg p/ hora      calculo seg p/ hora p/ dia
total = segundos + (minutos * 60) + ((horas * 60) * 60) + (((dias * 24) * 60) * 60)
print ('Isso equivale a %d segundos' %total)


