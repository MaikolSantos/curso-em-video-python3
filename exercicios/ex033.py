n1 = int(input('Digite 1º número: '))
n2 = int(input('Digite 2º númeor: '))
n3 = int(input('Digite 3º número: '))

# menor valor
if n1 < n2 and n1 < n3:
    print(f'\n {n1} é o menor número')
elif n2 < n3 and n2 < n3:
    print(f'\n {n2} é o menor número')
else:
    print(f'\n {n3} é o menor número')

# maior valor
if n1 > n2 and n1> n3:
    print(f'\n {n1} é o maior número')
elif n2 > n1 and n2 > n3:
    print(f'\n {n2} é o maior número')
else:
    print(f'\n {n3} é o maior número')
