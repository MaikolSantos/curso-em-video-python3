print('-' * 50)
print(f'{"CAIXA ELETRÔNICO": ^50}')
print('-' * 50)

v = int(input('Digite o valor a sacar: R$ '))

cinq = 0
vinte = 0
dez = 0
um = 0

while True:
    if v > 49:
        cinq = v // 50
        v %= 50
    elif v > 19:
        vinte = v // 20
        v %= 20
    elif v > 9:
        dez = v // 10
        v %= 10
    elif v > 0:
        um = v // 1
        v %= 1
    else:
        break

print('-' * 50)
if cinq != 0:
    print(f'{cinq} notas de R$ 50')
if vinte != 0:
    print(f'{vinte} notas de R$ 20')
if dez != 0:
    print(f'{dez} notas de R$ 10')
if um != 0:
    print(f'{um} notas de R$ 1')
print('-' * 50)
print('\nVolte Sempre!')

