n = int(input('Digite um número inteiro: '))
op = int(input("""Conversação. Digite:
1 - para Binário
2 - para Octal
3 - para Hexadecimal
"""))

#IMPORTANTE USAR O FATIAMENTO DE OBJETO

if op == 1:
    print('{} em Binário é {}'.format(n, bin(n)[2:])) #[2:] PEGA DA 3º POSIÇÃO ATÉ O FINAL DO OBJETO
elif op == 2:
    print('{} em Octal é {}'.format(n, oct(n)[2:]))
elif op == 3:
    print('{} em Hexadecimal é {}'.format(n, hex(n)[2:]))
else:
    print('Opção inválida!')
