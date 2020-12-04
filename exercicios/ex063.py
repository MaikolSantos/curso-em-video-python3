termo = int(input('Quantos termos vocêr quer da Sequeência Fibonacci: '))
t1 = 0
t2 = 1
print('{} - {} - '.format(t1, t2), end='')
c = 3
while c <= termo:
    t3 = t1 + t2
    print(t3, end=' - ')
    t1 = t2
    t2 = t3
    c += 1
print('Fim')
