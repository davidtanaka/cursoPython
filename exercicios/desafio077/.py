tupla = ('CASA', 'BARRACA', 'MESA', 'BARCO', 'FAROL', 'MARUJO', 'SEREIA')
for palavra in tupla:
    if palavra == tupla[0]:  # SE FOR A PRIMEIRA PALAVRA DA TUPLA, NÃO VAI QUEBRAR LINHA
        print(f'Na palavra {palavra} temos as vogais:', end=' ')
    else:
        print(f'\nNa palavra {palavra} temos as vogais:', end=' ')
    for letra in palavra:
        if letra in 'AEIOU':
            print(f'{letra}', end=' ')