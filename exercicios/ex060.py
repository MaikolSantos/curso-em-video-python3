'''n = int(input('Número para Fatorial: '))
c = n
f = 1
while c > 0:
    print(c, end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f)'''

n = int(input('Número para fatorial: '))
f = 1
for c in range(n, 0, -1):
    print(c, end='')
    if c != 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
    f *= c
print(f)
