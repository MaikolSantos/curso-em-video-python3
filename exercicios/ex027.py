nome = str(input('Digite seu nome completo: ')).strip()
nomes = nome.split()
print(f'Seu primeiro nome é {nomes[0]}')
print((f'Seu último nome é {nomes[len(nomes) - 1]}'))