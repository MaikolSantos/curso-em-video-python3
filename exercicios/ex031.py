v = float(input('Qual é a distância da sua viagem em km? '))
print(f'\n Sua viagem será de {v} km \n ')
if v <= 200:
    print(f'Sua passagem custará R$ {v * 0.5:.2f}')
else:
    print(f'Sua passagem custará R$ {v * 0.45:.2f}')
