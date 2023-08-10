valores = list()
pares = list()
impares = list()
while True:
    valores.append(int(input('Digite um numero: [999 para parar] ')))
    if 999 in valores:
        break
for i, v in enumerate(valores):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print(f'Lista dos numeros {valores}')
print(f'Lista de numeros pares: {pares}')
print(f'Lista de numeros impares: {impares}')