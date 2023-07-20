carro = float(input('quantos  dias você utilizou o carro?'))
km = float(input('quantos km vc andou com o carro?'))
calculandoKm = km * 0.15
calculandoDias = carro * 60
somandoTudo = calculandoKm + calculandoDias

print('voce pagara {:.2f} Reais'.format(somandoTudo))
