n1 = int(input('digite um numero: '))
n2 = int(input('digite outro numero: '))

if n1 > n2:
    print('o numero {} é maior do que o numero {} ou seja o PRIMEIRO numero digitado é o maior'.format(n1, n2))
elif n2 > n1:
    print('o numero {} é maior do que o numero {} ou seja o SEGUNDO numero digitado é o maior'.format(n2, n1))
else:
    print('os dois numeros são iguais')