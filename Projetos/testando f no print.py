salário = int(input('Salário: '))
porcentagem = int(input('porcentagem: '))

salário_final = salário + (salário * porcentagem/100)
aumento = salário_final - salário

print ('Salário final é %.2f' %(salário_final))
print ('Aumento de %.2f' %(aumento))
