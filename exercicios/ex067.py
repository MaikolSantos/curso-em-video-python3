print('-' * 35)
print(f'{"TABUADA": ^35}')
print('-' * 35)

n = 0
while True:
    n = int(input('\033[1;32mDigite o número para a tabuada: \033[m'))
    if n < 0:
        break
    print('-' * 35)
    for c in range(1, 11):
        print(f'\033[1;34m{n} x {c:>2} = {n * c:>2}\033[m')
    print('-' * 35)
print('\n\033[1;35mPrograma de Tabuada Encerrado. Volte Sempre\033[m')
