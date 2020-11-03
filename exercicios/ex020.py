from random import shuffle
a1 = input('Digite o nome do Aluno 1: ')
a2 = input('Digite o nome do Aluno 2: ')
a3 = input('Digite o nome do Aluno 3: ')
a4 = input('Digite o nome do Aluno 4: ')
deck = [a1, a2, a3, a4]
shuffle(deck)
print('A ordem de apresentação será: {}'.format(deck))

