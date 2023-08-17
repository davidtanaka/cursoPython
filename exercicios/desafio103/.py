def ficha(jogador = 'desconhecido', gols = '0'):
    print(f'O jogador {jogador} fez {gols} gols')
    
    
j = str(input('Nome do jogador: '))
if j == '':
    j = '<desconhecido>'
g = str(input('Quantos Gols o jogador fez: '))
if g == '':
    g = '0'
ficha(j, g) 