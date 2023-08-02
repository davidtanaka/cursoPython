from random import randint
print('vou pensar em um numero tente adivinha em qual é')
computador = randint(0, 10)
jogador = int(input('qual numeroo de 0 a 10 vc acha que foi: '))
totatent = 1
while jogador != computador:
    totatent += 1
    jogador = int(input('Você errou!! Tente novamente: '))
    
print('Você acertou eu Pensei no numero {} e você no {} você prescisou de {} tentativas para acertar'.format(computador, jogador, totatent))