frase = str(input('Digite uma frase: ')).strip().upper().split()
frase = ''.join(frase)
fraseinv = []

for c in range(1, len(frase) + 1):
    fraseinv.append(frase[len(frase) - c])

fraseinv = ''.join(fraseinv)

print('A frase {} invertida é {}'.format(frase, fraseinv))

if frase == fraseinv:
    print('É Palíndromo')
else:
    print('NÃO É Palíndromo')


