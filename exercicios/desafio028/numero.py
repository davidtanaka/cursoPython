import random
computador = random.randint(0, 5)
jogador = int(input('qual numeroo de 0 a 5 vc acha que foi: '))

if jogador == computador:
    print('voce acertou o numero aleatorio eu pensei no {}'.format(computador))
else: 
    print('voce errou o numero aleatorio pois eu pensei no numero {} e não no {}'.format(computador, jogador))