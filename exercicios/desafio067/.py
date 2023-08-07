
while True:
    t = int(input('Digite um numero para a tabuada: '))
    if t < 0:
        break
    for c in range(1, 11):
        print(f'{t} x {c} = {t*c}')
print('PROGRAMA DE TABUADA ENCERRADO VOLTE SEMPRE')
