from time import sleep

print(' CONTAGEM REGRESSIVA \n')

i = int(input(' Iniciando em: '))

for c in range(i, -1, -1):
    print(c)
    sleep(1)

print('POW! BOOM! POW!')
