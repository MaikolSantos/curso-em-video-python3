from random import randint

sorteio = randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)

print(f'Números sorteados: ', end=' ')
for i in sorteio:
    print(f'{i}', end=' ')

print(f'\nO maior número sorteado foi {max(sorteio)}')
print(f'O menor número sorteado foi {min(sorteio)}')