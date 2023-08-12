lista = list()
temp = list()
maior = menor = 0
totc = 0
temp.append(str(input('Nome: ')))
temp.append(float(input('Peso: ')))
while True:
    continuar = str(input('Você deseja continuar? [S/N] ')).strip().upper()
    if continuar == 'S':
        totc += 1
        lista.append(str(input('Nome: ')))
        lista.append(float(input('Peso: ')))
    else:
        break
    if len(lista) == 0:
        maior = menor = lista[1]
    else:
        if lista[1] > maior:
            maior = lista[1]
        if lista[1] < maior:
            menor = lista[1]
        temp.append(temp[:])
        lista.clear()
print(f'Ao todo foram cadastrados {totc + 1} Pessoas')
print(f'O maior peso foi de {maior}  peso de ', end='')    
for p in lista:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi de {menor}  peso de ')  
for p in lista:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')
print()