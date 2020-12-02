somaidade = 0
maioridade = 0
nomesmas = ''
mulheres = 0

for p in range(1, 5):
    #dados
    nome = str(input('NOME da {}ª pessoa: '.format(p))).strip().capitalize()
    idade = int(input('IDADE da {}ª pessoa: '.format(p)))
    sexo = str(input('SEXO da {}ª pessoa: (masculino ou feminino) '.format(p))).strip().upper()[0]
    #media idades
    somaidade += idade
    #condição homem mais velho
    if p == 1 and sexo == 'M':
        maioridade = idade
        nomesmas = nome
    else:
        if sexo == 'M' and idade > maioridade:
            maioridade = idade
            nomesmas = nome
    #mulheres com menos de 20 anos
    if sexo == 'F' and idade < 20:
        mulheres += 1


print('\nA média de Idade do grupo é de {:.2f}'.format(somaidade / 4))
print('O homem mais velho se chama {}, sua idade é {}'.format(nomesmas, maioridade))
print('Existem {} mulheres com menos de 20 anos'.format(mulheres))
