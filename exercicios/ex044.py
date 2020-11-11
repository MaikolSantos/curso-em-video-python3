p = float(input(' Preço do Produto: R$ '))

op = int(input(""" Digite a opção desejada para pagamento:
[ 1 ] À vista no Dinheiro ou no Cheque - Desconto de 10%
[ 2 ] À vista no Cartão - Desconto de 5%
[ 3 ] A prazo em até 2x no Cartão - Preço Atual
[ 4 ] A prazo em até 3x no Cartão - 20% de Juros"""))

if op == 1:
    print('O produto sairá por: ', end='')
    print('R$ {:.2f}'.format(p * 0.9))
elif op == 2:
    print('O produto sairá por: ', end='')
    print('R$ {:.2f}'.format(p * 0.95))
elif op == 3:
    print('O produto sairá por: ', end='')
    print("""
    2x de R$ {:.2f} OU 
    1x de R$ {:.2f}""".format(p / 2, p))
elif op == 4:
    parc = int(input('Quantas parcelas? '))
    p *= 1.2
    print('O produto sairá por: ', end='')
    print('{}x de R$ {:.2f}'.format(parc, p / parc))
else:
    print('Opção inválida. Tente de novo')
