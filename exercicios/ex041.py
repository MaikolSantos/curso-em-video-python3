from datetime import date

nasc = int(input('Digite seu ano de nascimento: '))

idade = date.today().year - nasc

print('O atleta tem {} anos. Nessa faixa etária ele é um (a): '.format(idade))

if idade <= 9:
    print('Nadador MIRIM')
elif idade <= 14:
    print('Nadador INFANTIL')
elif idade <= 19:
    print('Nadador JUNIOR')
elif idade <= 25:
    print('Nadador SÊNIOR')
else:
    print('Nadador MASTER')
