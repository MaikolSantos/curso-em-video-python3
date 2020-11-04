nome = str(input('Digite seu nome completo: '))
print('Analisando seu nome completo...')
print('Seu nome em maiúsulas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
espaco = nome.count(' ')
qtdNome = len(nome)
nomeDiv = qtdNome - espaco
print('Seu nome ao todo tem {} letras'.format(nomeDiv))
nomes = nome.split()
print('Seu primeiro nome é {} e tem {} letras'.format(nomes[0], len(nomes[0])))

