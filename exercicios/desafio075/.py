
vezes = primeiroTrez = pares = 0

numeros = (int(input('digite o primeiro valor: ')),
           int(input('digite o segundo valor: ')),
           int(input('digite o terceiro valor: ')),
           int(input('digite o quarto valor: ')))
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
    pares += numeros[0]
if numeros[1] % 2 == 0:
    pares += numeros[1]
if numeros[2] % 2 == 0:
    pares += numeros[2]
if numeros[3] % 2 == 0:
    pares += numeros[3]
print(f'Os numeros digitados foram: {numeros}')
if 9 in numeros:
    print(f'O numero nove apareceu {vezes}')
else:
    print('O numero nove não foi digitado nenhuma vez')
if 3 in numeros:
    print(f'O numero trez foi digitado pela primeira vez na posição {primeiroTrez + 1}')
else:
    print('Não foram encontrado o numero 3')
print(f'A soma dos numeros pares foram {pares}')