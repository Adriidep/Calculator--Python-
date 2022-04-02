import math

n1 = float(input('Introduce tu primer número: '))
n2 = float(input('Introduce tu segundo numero: '))

suma = n1 + n2
res = n1 - n2
mul = n1 * n2
div = n1 // n2

l = [suma, res, mul, div]

for i in l:
    print('El valor es: {}'.format(i))

s = input('¿Deseas otros datos? Y/N: ')

if s == 'Y':
    div_ext = n1/n2
    resto = n1 % n2
    exp = n1 ** n2
    sqr1 = math.sqrt(n1)
    sqr2 = math.sqrt(n2)

    print('La división exacta es {}, y de resto {}.'.format(div_ext, resto))
    print('El exponente es: {}'.format(exp))
    print('Las raíces cuadradas de dichos números son, respectivamente: {} y {}'.format(sqr1, sqr2))
