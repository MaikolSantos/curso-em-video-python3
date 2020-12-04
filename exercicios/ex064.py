i = 0
s = 0
c = 0
while i != 999:
    n = int(input('Digite um número: [999 para parar] '))
    if n == 999:
        i = 999
    else:
        c += 1
        s += n
print('\nVocê digitou {} números'.format(c))
print('\nA soma entre todos é {}'.format(s))
