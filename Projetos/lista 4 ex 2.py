#Lista 4 Exercício 2
'''import random

lista = [ ]
for k in range (20):
    lista.append (random.randint (1, 100))

PAR = [ ]
ÍMPAR = [ ]
for n in lista:
    if n % 2 == 0:
        PAR.append (n)
    else:
        ÍMPAR.append(n)

lista.sort()
PAR.sort()
ÍMPAR.sort()
print (lista)
print (PAR)
print (ÍMPAR)
'''
#Lista 4 Exercício 5

txt = '''The Python Software Foundation and the global Python community welcome and
           encourage participation by everyone. Our community is based on mutual respect,
           tolerance, and encouragement, and we are working to help each other live up to
           these principles. We want our community to be more diverse: whoever you are,
           and whatever your background, we welcome you.'''
import string
txt = txt.lower()
for c in string.punctuation:
    txt = txt.replace (c, ' ')
txt = txt.split()
def tem_uma_letra_python(palavra):
    for x in palavra:
        if x in 'python':
            return True
    return False
    #alinha com o for, só chego aqui se nenhuma
    #letra está em "python"

lista = [ ]
for p in txt:
    if tem_uma_letra_python(p) and len(p) > 4:
        lista.append(p)
print (len (lista))
lista.sort()
print (lista)
