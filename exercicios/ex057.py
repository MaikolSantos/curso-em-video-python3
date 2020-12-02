sexo = str(input('Digite seu sexo: [M/F] ')).strip().upper()[0]
s = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Dados inválidos. Digite seu sexo: [M/F] ')).strip().upper()[0]
    if sexo == 'M':
        s = 'Homem'
    elif sexo == 'F':
        s = 'Mulher'

print('Você é {}'.format(s))
