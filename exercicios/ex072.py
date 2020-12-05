tupla = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze',
         'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    op = ' '
    while True:
        n = int(input('Digite um número entre 0 e 20: '))
        if 0 <= n <= 20:
            break
        print('Tente novamente.')
    print(tupla[n])
    while op not in 'SN':
        op = str(input('Deseja continuar: [S/N]')).strip().upper()[0]
    if op == 'N':
        break

