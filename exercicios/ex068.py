from random import randint

c = 0
while True:
    comp = randint(1, 10)
    usu = int(input('Digite seu número: '))
    soma = comp + usu
    pi = ' '
    while pi not in 'PI':
        pi = str(input('Você quer PAR ou IMPAR?: [P/I] ')).upper().strip()[0]
    if pi == 'P':
        if soma % 2 == 0:
            print(f'Você jogou {usu} e o Computador {comp}. Deu {soma}, é PAR! Você ganhou!')
            c += 1
        else:
            print(f'Você jogou {usu} e o Computador {comp}. Deu {soma}, é IMPAR! Você Perdeu!')
            break
    elif pi == 'I':
        if soma % 2 == 1:
            print(f'Você jogou {usu} e o Computador {comp}. Deu {soma}, é IMPAR! Você Ganhou!')
            c += 1
        else:
            print(f'Você jogou {usu} e o Computador {comp}. Deu {soma}, é PAR! Você Perdeu')
            break

print(f'Você Ganhou {c} vezes')
