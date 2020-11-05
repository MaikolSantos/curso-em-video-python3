from random import randint
from time import sleep
np = randint(0, 5)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar! ')
chute = int(input('Em que número pensei? '))
print('PROCESSANDO...')
sleep(3)
if np == chute:
    print(f'Boa! Foi em {np} que eu pensei')
else:
    print(f'Errou! Eu pensei em {np}')
