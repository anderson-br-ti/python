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

