print('-' * 50)
print(f'{"Cadastro de Pessoas": ^50}')
print('-' * 50, '\n')
contidade = homem = mulheresm20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    op = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade > 18:
        contidade += 1
    if sexo == 'M':
        homem += 1
    if sexo == 'F' and idade < 20:
        mulheresm20 += 1
    while op not in 'SN':
        op = str(input('Deseja continuar: [S/N] ')).strip().upper()[0]
    if op == 'N':
        break

print('-' * 50)
print(f'Foram cadastradas {contidade} pessoas acima de 18 anos.')
print(f'Foram cadastrados {homem} homens.')
print(f'Foram cadastradas {mulheresm20} mulheres com menos de 20 anos.')
print('-' * 50)
