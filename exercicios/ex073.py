tupla = ('Internacional', 'Flamengo', 'Atlético-MG', 'São Paulo', 'Santos',
         'Fluminense', 'Fortaleza', 'Palmeiras', 'Atlético-GO', 'Corinthians',
         'Grêmio', 'Sport Recife', 'Bahia', 'Ceará SC', 'Botafogo', 'Vasco da Gama',
         'Athletico-PR', 'Coritiba', 'Bragantino-SP', 'Goiás')

print(f'Os cinco primeiros colocados são: {tupla[:5]}')
print(f'Os quatro últimos colocados são: {tupla[-4:]}')
print(f'Times em ordem alfabética: {sorted(tupla)}')
print(f'Posição do Bahia {tupla.index("Bahia") + 1}')
