#1
nota = int(input('Digite um número: '))
while nota > 10:
    print ('Valor incorreto!')
    nota = int(input('Digite um número: '))
#2
usuario = input('Digite um nome de usuario: ')
senha = input('Digite uma senha: ')
while usuario == senha:
    print ('Erro!')
    usuario = input('Digite um nome de usuario: ')
    senha = input('Digite uma senha: ')
#3
a = 80000
b = 200000
ano = 0
while a < b:
    a = a + (a * 0.03)
    b = b + (b * 0.015)
    ano = ano + 1
print ('Foram necessários %d anos!' %(ano))
