valor = int(input('digite um numero para saber o fatorial: '))
fatorial = 1
while (valor > 1):
    fatorial = fatorial * valor
    valor = valor -1
print('o fatorial é {}'.format(fatorial))