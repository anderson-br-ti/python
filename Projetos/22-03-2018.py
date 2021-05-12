#sequência de fibonacci: 1 1 2 3 5 8 13 21...
#                                      n: 1 2 3 4 5  6  7  8
#    a    b   a+b
#    1     1    2
#    1     2    3
#    2     3    5                      esta lógica é a, b = b, a+b
#    3     5    8                      se repete n-2 vezes
#    5     8    13                    pois não calculo o 1º nem o 2º
#    8    13   21

n = int(input('a: '))
a, b = 1, 1
cont = 1
while cont <= n-2:
    a, b = b, a+b
    cont = cont + 1
print (b)
