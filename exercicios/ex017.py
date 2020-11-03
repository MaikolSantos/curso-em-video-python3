''' from math import hypot
a = float(input('Digite o valor de um cateto: '))
b = float(input('Digite o valor de outro cateto: '))
print('A hipotenusa dos catetos {} e {} é igual a {:.2f}: '.format(a, b, hypot(a, b))) '''

# ou

from math import sqrt
a = float(input('Digite o valor de um cateto: '))
b = float(input('Digite o valor de outro cateto: '))
c = sqrt(pow(a, 2) + pow(b, 2))
print('A hipotenusa dos catetos {} e {} é igual a {:.2f}'.format(a, b, c))
