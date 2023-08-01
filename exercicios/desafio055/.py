
maior = 0
menor = 0
for p in range(1, 6):
    peso = int(input('Peso da {} pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O MAIOR peso lido foi de: {}'.format(maior))
print('O MENOR peso lido foi de: {}'.format(menor))