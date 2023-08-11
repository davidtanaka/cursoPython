num = [[], []]
valor = 0
for c in range(1, 8):
    valor = (int(input('Digite um numero: ')))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print(f'Os numeros pares são {num[0]}')
print(f'Os numeros impares são: {num[1]}')