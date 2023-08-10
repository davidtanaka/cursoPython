valores = []
for v in range(1, 6):
    valores.append(int(input(f'Digite o valor {v}: ')))
print(f'Os numeros digitados foram: {valores}')
print(f'O maior numero digitado foi {max(valores)} e estava na posição {valores.index(max(valores))+1}')
print(f'O menor numero digitado foi {min(valores)} e estava na posição {valores.index(min(valores))+1}')
