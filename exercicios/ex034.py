s = float(input('Digite o salário para saber o reajuste: R$ '))

if s > 1250:
    s = s * 1.1
    print(f'O salário passou a ser de R$ {s:.2f} ')
else:
    s = s * 1.15
    print(f'O salário passou a ser de R$ {s:.2f}')
