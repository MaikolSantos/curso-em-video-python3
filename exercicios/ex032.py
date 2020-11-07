from datetime import date

ano = int(input('Digite um ano para saber se ele é BISSEXTO: (para analisar o ano atual, digite 0) '))

if ano == 0:
    ano = date.today().year

m4 = (ano % 4) == 0
m100 = (ano % 100) != 0
m400 = (ano % 400) == 0

if m4 == True and m100 == True:
    print(f'\n O ano {ano} é BISSEXTO')
elif m4 == True and m100 == False and m400 == True:
    print(f'\n O ano {ano} é BISSEXTO')
else:
    print(f'\n O ano {ano} não é BISSEXTO')

#resolução do professor
'''
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0
    print(f'\n O ano {ano} é BISSEXTO')
else:
    print(f'\n O ano {ano} não é BISSEXTO')
'''
