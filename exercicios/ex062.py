t = int(input('Digite o primeiro termo: '))
r = int(input('Digite a Razão: '))
c = 1
tot = 0
mt = 10
while mt != 0:
    tot += mt
    while c <= tot:
        print(t, end=' ')
        t += r
        c += 1
    mt = int(input('\nQuanto termos mais? '))
print('\n{} termos vizualizados'.format(tot))

