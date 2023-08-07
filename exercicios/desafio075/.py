
vezes = primeiroTrez = pares = 0
n1 = int(input('digite o primeiro valor: '))
n2 = int(input('digite o segundo valor: '))
n3 = int(input('digite o terceiro valor: '))
n4 = int(input('digite o quarto valor: '))
numeros = (n1, n2, n3, n4)
if numeros[0] == 9:
    vezes += 1
if numeros[1] == 9:
    vezes += 1
if numeros[2] == 9:
    vezes += 1
if numeros[3] == 9:
    vezes += 1
    
if numeros[0] == 3:
    primeiroTrez = 1
if numeros[1] == 3:
    primeiroTrez = 2
if numeros[2] == 3:
    primeiroTrez = 3
if numeros[3] == 3:
    primeiroTrez = 4
    
if numeros[0] % 2 == 0:
    pares += n1
if numeros[1] % 2 == 0:
    pares += n2
if numeros[2] % 2 == 0:
    pares += n3
if numeros[3] % 2 == 0:
    pares += n4
print(f'Os numeros digitados foram: {numeros}')
print(f'O numero nove apareceu {vezes}')
print(f'O numero trez foi digitado pela primeira vez na posição {primeiroTrez}')
print(f'A soma dos numeros pares foram {pares}')