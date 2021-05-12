notas = [ ]
conta = 0
media = 0
while conta < 4:
    nota = float (input ('Digite uma nota: '))
    notas.append(nota)
    conta = conta + 1
    media = media + nota
print (notas)
print (media/4)
