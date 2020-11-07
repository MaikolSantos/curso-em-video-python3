print('°*°' * 20)
print('ANALISADOR DE TRIÂNGULOS')
print('°*°' * 20)

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

# solução do professor

if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima PODEM formar um triângulo')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo')

#solução falha
'''
if a > b and a > c:
    if a < b + c:
        print('Os segmentos acima PODEM formar um triângulo')
    else:
        print('Os segmentos acima NÃO PODEM formar um triângulo')

if b > a and b > c:
    if b < a + c:
        print('Os segmentos acima PODEM formar um triângulo')
    else:
        print('Os segmentos acima NÃO PODEM formar um triângulo')

if c > a and c > b:
    if c < a + b:
        print('Os segmentos acima PODEM formar um triângulo')
    else:
        print('Os segmentos acima NÃO PODEM formar um triângulo')
'''