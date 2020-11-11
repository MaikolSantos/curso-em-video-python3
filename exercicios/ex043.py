peso = float(input('Peso: (kg)'))
altura = float(input('Altura: (m)'))

imc = peso / (altura * altura)

print('Seu IMC é {:.2f}'.format(imc))

if imc < 18.5:
    print('Você está ABAIXO do peso')
elif imc < 25:
    print('Você está no PESO IDEAL')
elif imc < 30:
    print('Você está com SOBREPESO')
elif imc < 40:
    print('Você está OBESO')
else:
    print('CUIDADO! OBESIDADE MÓRBIDA')



## 53.47  1.7