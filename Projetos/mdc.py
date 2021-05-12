#mdc segundo o algoritmo de Euclides
#    a    b    a%b
#   21  15     6        (15        %    21      =      15)
#   15   6      3          menor      maior       resto
#     6   3      0

#a lógica a, b = b, a%b
#repito até que a%b seja 0
#quando a%b for zero mdc é o b

a = int(input('a: '))
b = int(input('b: '))
while a%b != 0:
    a, b = b, a%b
print (b)
