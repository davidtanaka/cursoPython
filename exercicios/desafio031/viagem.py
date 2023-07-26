viagem = float(input('qual a distancia da viagem em km?:  '))
viagemC = viagem * 0.50
viagemL = viagem * 0.45
if viagem <= 200:
    print('o preço da viagem é de {}'.format(viagemC))
else:
    print('O prço dessa viagem é de; {}'.format(viagemL))
    