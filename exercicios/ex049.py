n = int(input('Digite o número que deseja a tabuada: '))
v = int(input('Digite até quanto deseja ver a multiplicação: '))

for c in range(1, v + 1):
    print(f'{n} X {c:>2} = {n * c:>2}')
