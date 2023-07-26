velo = int(input('qual a velocidade do carro: '))
muta = (velo - 80) * 7 

if velo > 80:
    print('voce foi mutado em; {}R$'.format(muta))
else:
    print('siga a viagem')
