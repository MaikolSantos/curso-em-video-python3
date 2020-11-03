from math import sin, cos, tan, radians
a = float(input('Digite o ângulo que você deseja: '))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))
print('O ângulo de {} tem o SENO de {:.2f}'.format(a, s))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(a, c))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(a, t))
