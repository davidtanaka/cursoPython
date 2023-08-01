s = 0
cont = 0

for c in range(1, 6 + 1):
    n = int(input('digite o {} valor: '.format(c)))
    if n % 2 == 0:
        s += n
        cont += 1
print('você informou {} numeros PARES e a soma foi {}'.format(cont, s))
