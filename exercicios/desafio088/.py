from random import randint
mega = [[], [], []]
jogos = int(input('Quantos jogos você quer: '))
for c in range(1, jogos + 1):
    computador = randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60), randint(1, 60)
    print(f'Seu {c}º numeros{computador}')