print('\n {:=^50}'.format(' Vamos pintar sua parede'))

a = float(input('\n Qual a altura da sua parede em metros? '))
l = float(input('\n Qual a largura da sua parede em metros? '))
area = a * l

print('\n A dimensão de {:.2f}m x {:.2f}m tem a área de {:.2f}m²'.format(a, l, area))

print('\n Você irá precisar de {:.2f} litros de tinta para pintá-la.'.format(area / 2))