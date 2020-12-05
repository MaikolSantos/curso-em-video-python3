total = prodmil = cont = barato = 0
nomeprod = ' '
while True:
    prod = str(input('Nome do Produto: ')).strip().capitalize()
    preco = float(input(f'Preço do {prod}: R$ '))
    cont += 1
    op = ' '
    if preco > 1000:
        prodmil += 1

    #trainar mais essa lógica, ao ponto de substituir por um "IF" com o operador "OR", eliminando o "ELIF"
    if cont == 1:
        barato = preco
        nomeprod = prod
    elif preco < barato:
        barato = preco
        nomeprod = prod

    total += preco
    while op not in 'SN':
        op = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if op == 'N':
        break
print(f'Total da Compra: {total}')
print(f'{prodmil} produto (s) acima de R$ 1.000,00')
print(f'{nomeprod} é o produto mais barato da compra; com valor de R$ {barato}')
