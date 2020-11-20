n = int(input('Digite um número inteiro: '))

cont = 0

for c in range(1, n + 1):
    if n % c == 0:
        print('\033[034m{}\033[m'.format(c), end=' ')
        cont += 1
    else:
        print('\033[031m{}\033[m'.format(c), end=' ')

print('\nO número {} foi divisível {} vezes '.format(n, cont))

if cont == 2:
    print('Portanto, o número {} é PRIMO'.format(n))
else:
    print('Portanto, o número {} NÃO é PRIMO'.format(n))
