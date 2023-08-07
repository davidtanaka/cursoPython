total = produtosAcima = menor = cont = 0
continuar = True
barato = ''
nome = str(input('Nome: [Produto] '))
preco = float(input('Preço: [Produto] '))
cont += 1
continuar = str(input('Voçê deseja continuar? [S/N]')).strip().upper()
while continuar not in 'SN':
    continuar = str(input('Voçê deseja continuar? [S/N]')).strip().upper()
if continuar == 'S':
    continuar = True
else:
    continuar = False
while continuar == True:
    nome = str(input('Nome: [Produto] '))
    preco = float(input('Preço: [Produto] '))
    total = total + preco
    if preco >= 1000:
        produtosAcima += 1
    if cont == 1:
        menor = preco
        barato = nome
    else:
        if preco < menor:
            menor = preco
            nome = nome
print(f'O total gasto na compra foi: {total}')
print(f'temos {produtosAcima} produtos acima de 1000R$')
print(f'O produto mais barato foi {barato} que custa: {menor}')
