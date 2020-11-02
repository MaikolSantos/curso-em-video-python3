a = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos quilômetros foram percorridos? '))

print('O valor a ser cobrado por {} dia (s) alugado e {} km percorridos é de R$ {:.2f}'.format(a, km, ((a * 60) + (km * 0.15))))