#nomes e notas
'''f = open ('surf.txt')
for linha in f:
    print (linha.strip())
f.close()
'''
#maior nota
'''f = open ('surf.txt')
maior = 0
for linha in f:
    nome, pontos = linha.split()
    if float(pontos) > maior:
        maior = float (pontos)
f.close()
print (maior)
'''
#três notas
'''f = open ('surf.txt')
notas = [ ]
for linha in f:
    nome, pontos = linha.split()
    notas.append (float (pontos))
f.close()
print (notas[0])
print (notas[1])
print (notas[2])
'''
#agora na ordem certa
'''f = open ('surf.txt')
notas = [ ]
for linha in f:
    nome, pontos = linha.split()
    notas.append (float (pontos))
f.close()
notas.sort()
notas.reverse()
print (notas[0])
print (notas[1])
print (notas[2])
'''
#com os nomes INCOMPLETO
'''f = open ('surf.txt')
notas = [ ]
nomes = [ ]
for linha in f:
    nome, pontos = linha.split()
    notas.append (float (pontos))
    nomes.append (nome)
f.close()
notas.sort (reverse = True)
nomes.sort (reverse = True)
print
'''
#nome e nota certos
'''f = open ('surf.txt')
notas  = { }
for linha in f:
    nome, pontos = linha.split()
    notas [float (pontos)] = nome
f.close()
for nota in sorted (notas, reverse = True):
    print ('%s tem nota %.2f' %(notas [nota], nota))
'''
