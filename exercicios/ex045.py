from random import randint
from time import sleep

print('*°' * 15)
print('{:^30}'.format('JO - KEM - PÔ'))
print('*°' * 15)

maq = randint(1, 3)

usu = int(input("""ESCOLHA SUA JOGADA:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA """))

print('JO')
sleep(1)
print('KEM')
sleep(1)
print('PÔ! \n')
sleep(1)

if maq == 1 and usu == 2:
    print('Computador escolheu PEDRA e você PAPEL')
    print('-' * 30)
    print('VOCÊ VENCEU!')
elif usu == 1 and maq == 2:
    print('Computador escolheu PAPEL e você PEDRA')
    print('-' * 30)
    print('VOCÊ PERDEU!')
elif maq == 2 and usu == 3:
    print('Computador escolheu PAPEL e você TESOURA')
    print('-' * 30)
    print('VOCÊ VENCEU!')
elif usu == 2 and maq == 3:
    print('Computador escolheu TESOURA e você PAPEL')
    print('-' * 30)
    print('VOCÊ PERDEU!')
elif maq == 3 and usu == 1:
    print('Computador escolheu TESOURA e você PEDRA')
    print('-' * 30)
    print('VOCÊ VENCEU!')
elif usu == 3 and maq == 1:
    print('Computador escolheu PEDRA e você TESOURA')
    print('-' * 30)
    print('VOCÊ PERDEU!')
else:
    print('EMPATE!')
