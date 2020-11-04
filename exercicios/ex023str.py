n = str(input('Digite um número de 0 a 9999: ')).zfill(4)
print("""O número tem:
    {} unidades;
    {} dezenas;
    {} centenas;
    {} milhares.
""". format(n[3], n[2], n[1], n[0]))

