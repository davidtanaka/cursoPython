soma = 0
cont =  0
for c in range(1, 500 + 1, 2):
    if c % 3 == 0:
        soma += c
        cont = cont + 1
print('a soma de todos {} valores solicitados é de: {}'.format(cont, soma))
