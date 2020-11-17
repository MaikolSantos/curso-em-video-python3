s = 0
n = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        s += c
        n += 1
print('A soma dos {} números é {}'.format(n, s))
