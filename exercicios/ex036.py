casa = float(input('Qual o valor da casa? R$ '))
sal = float(input('Qual o salário? R$ '))
ano = int(input('Quantos anos para quitação? '))

prest_mensal = casa / (ano * 12)
prest_max = sal * 0.3

print('Para pagar uma casa de R$ {:.2f} durante {} anos a mensalidade será de {:.2f}'.format(casa, ano, prest_mensal))

if prest_mensal > prest_max:
    print('Desculpe! EMPRÉSTIMO NEGADO!')
else:
    print('O empréstimo pode ser CONCEDIDO')
