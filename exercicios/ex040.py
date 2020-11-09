n1 = float(input('Digite a Primeira Nota: '))
n2 = float(input('Digite a Segunda Nota: '))

m = (n1 + n2) / 2

print('Tirando notas {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1, n2, m))

if m > 7.0:
    print('\033[1;34mAPROVADO')
elif m < 5:
    print('\033[1;31mREPROVADO')
else:
    print('\033[1;32mRECUPERAÇÃO')
