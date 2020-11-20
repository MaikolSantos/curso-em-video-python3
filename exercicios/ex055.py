# minha resolução
'''pesos = []

for c in range(1, 6):
    pesos.append(float(input('Peso da {}ª pessoa: '.format(c))))

print('{:.2f} é o maior peso lido e {:.2f} é o menor peso lido.'.format(max(pesos), min(pesos)))'''

# resolução do professor (ajuda mais na lógica)

maior = 0
menor = 0

for pessoas in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(pessoas)))
    if pessoas == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('{} é o maior peso lido e {} é o menor peso lido'.format(maior, menor))
