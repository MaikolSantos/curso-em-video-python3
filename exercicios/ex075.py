n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))
tupla = n1, n2, n3, n4

cont9 = 0

for i in tupla:
    if i == 9:
        cont9 += 1

print(f'O número 9 apareceu {cont9} vezes')
print(f'O valor 3 apareceu na posição {tupla.index(3)}')

print(f'Os valores pares digitados foram: ', end='')
for i in tupla:
    if i % 2 == 0:
        print(i, end=' ')
