# Todas informações de uma variável digitada

x = input('Digite algo: ')
print('O tipo primitivo é ', type(x))
print('O que você digitou é letra: ', x.isalpha())
print('O que você digitou é número: ', x.isnumeric())
print('O que você digitou é letras e/ou números: ', x.isalnum())
print('O que você digitou está tudo em maiúsculo: ', x.isupper())
print('O que você digitou está tudo em minúculo: ', x.islower())
