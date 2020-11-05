v = float(input('Qual a velocidade atual do carro? '))
if v > 80:
    print('\n MULTADO! Você excedeu o limite permitido que é de 80km/h')
    print(f'\n Você deve pagar uma multa de R$ {(v - 80) * 7:.2f}')
else:
    print('Limite permitido')
print('\n TENHA UM BOM DIA! DIRIJA COM CUIDADO')