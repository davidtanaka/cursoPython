listagem = ('lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9,
            'estojo', 25, 'Transferidor', 4.20, 'Compasso', 9.99,
            'mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.9)

print('-' * 30)
print(f'{"LISTAGEM DE PREÇOS":^15}')
print('-' * 30)

j = 1

for i in range(0, len(listagem), 2):
    print(f'{listagem[i].title()}............... R${listagem[j]:^.2f}')
    j += 2

print('-' * 30)