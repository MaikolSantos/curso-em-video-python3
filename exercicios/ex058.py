from random import randint

comp = randint(0, 10)

print("""Sou seu \033[1;35mCOMPUTADOR\033[m. Vamos jogar?

Acabei de pensar em um número entre 0 e 10. Tente adivinhar!
""")

use = 11
palp = 1

while use != comp:
    use = int(input('Digite seu palpite: '))
    if use == comp:
        print('\033[34mPARABÉNS! Eu pensei em {}\033[m'.format(comp))
    else:
        print('\033[31mERROU! Tente novamente!\033[m')
        palp += 1
        if use > comp:
            print('\033[1;32mDica: é menos\033[m')
        elif use < comp:
            print('\033[1;36mDica: é mais\033[m')
    print(' - ' * 10)
print('Você acertou no {}º palpite'.format(palp))

