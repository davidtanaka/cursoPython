totn = tot5 = 0
continuar = 'S'
valores = []
while True:
    continuar = str(input('Você deseja continuar? [S/N] ')).strip().upper()
    if continuar == 'S':
        valores.append(int(input('Digite outro numero: ')))
        totn += 1
    else:
        break
print(f'Foram digitados {valores} numeros')
valores.sort(reverse=True)
print(f'Os numeros digitados em ordem dedcrescente fica {valores}')
if 5 in valores:
    print(f'O numero 5 foi digitado')
else:
    print('O numero 5 NÃO foi digitado nenhuma vez')
    