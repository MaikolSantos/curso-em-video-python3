print('Entre com dois valores: ')

v1 = float(input('1º Valor: '))
v2 = float(input('2º Valor: '))

op = 0

while op != 5:
    op = int(input("""\nO que você deseja fazer com esses dois números:
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Saber qual é o maior valor
    [ 4 ] Digitar novos números
    [ 5 ] Sair do programa
    """))
    if op == 1:
        print('A soma é {}'.format(v1 + v2))
    elif op == 2:
        print('O produto é {}'.format(v1 * v2))
    elif op == 3:
        if v1 > v2:
            print('{} é maior'.format(v1))
        elif v1 < v2:
            print('{} é maior'.format(v2))
        else:
            print('São o mesmo valor')
    elif op == 4:
        print('Entre com novo valores')
        v1 = float(input('1º Valor: '))
        v2 = float(input('2º Valor: '))
    elif op != 5:
        print('Opção inválida. Tente novamente')
