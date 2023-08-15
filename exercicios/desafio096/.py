def area(l, c):
    print('Controle de terrenos')
    print('-=' * 15)
    s = l * c
    print(f'A área deste terreno {l}x{c} é de {s}²')
    
    
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
area(largura, comprimento)

