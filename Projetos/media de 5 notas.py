notas = [ ]
k = 0
media = 0
while k < 5:
    x = int (input ('Digite uma nota: '))
    notas.append(x)
    k += 1
    media = media + x
print (media/5)
    
