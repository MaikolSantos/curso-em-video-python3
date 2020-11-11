a = float(input('Primeiro Seguemento: '))
b = float(input('Segundo Seguemento: '))
c = float(input('Terceiro Seguemento: '))

if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima podem formar um TRIÂNGULO ', end='')
    if a != b and b != c and c != a:  # a != b != c != a
        print('ESCALENO')
    elif a != b and b == c or b != c and c == a or c != a == b:
        print('ISÓSCELES')
    else:  # a == b == c
        print('EQUILÁTERO')
else:
    print('Os segmentos acima não podem formar um TRIÂNGULO')
