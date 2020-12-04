s = c = n = 0
op = 'S'
maior = 0
menor = 0
while op == 'S':
    n = int(input('Digite um número: '))
    c += 1
    s += n
    if c == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    op = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
print('\nVocê digiou {} números '.format(c))
print('\nA média entre eles é de {:.2f}'.format(s / c))
print('\nMaior valor é {}'.format(maior))
print('\nMenor valor é {}'.format(menor))
