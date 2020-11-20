from datetime import date

ano = date.today().year

maior = 0
menor = 0

for c in range(1, 8):
    idade = int(input('Qual o ano de nascimento da {}ª pessoa: '.format(c)))
    if ano - idade >= 21:
        maior += 1
    else:
        menor += 1

print('\n{} pessoa(s) já tem(ê) a maior idade'.format(maior))

print('\n{} pessoa(s) ainda NÃO tem(ê) a maior idade'.format(menor))
