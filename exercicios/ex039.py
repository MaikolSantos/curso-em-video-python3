from datetime import date

sexo = str(input('Entre com "m" se você for MULHER ou entre com "h" se for HOMEM: '))

if sexo == 'm':
    print('Você é mulher. Não tem obrigação de alistar')
else:
    print('Por você ser homem, você tem a obrigação de se alistar!')
    nasc = int(input('Digite o ano do seu nascimento: '))
    ano = date.today().year
    idade = ano - nasc

    print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade, ano))

    if idade < 18:
        print('Ainda falta {} ano (s) '.format(18 - idade))
        print('Seu alistamento será em {}'.format(nasc + 18))
    elif idade == 18:
        print('Você precisa se alistar esse ano!')
    else:
        print('Você deveria ter se alistado há {} anos atrás '.format(idade - 18))
        print('Seu alistamento foi em {}'.format(nasc + 18))
