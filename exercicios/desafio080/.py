lista = []
for c in range(0, 5):
    valores = int(input(f'Digite o {c}º valor: '))
    if c == 0 or valores > lista[-1]:
        lista.append(valores)
    else:
        pos = 0
        while pos < len(lista):
            if valores <= lista[pos]:
                lista.insert(pos, valores)
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')
        