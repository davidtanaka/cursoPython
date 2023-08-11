lista = []
tdboletim = []
tot = 0
nome = str(input('Digite seu nome: '))
n1 = int(input('Digite a sua primeira nota: '))
n2 = int(input('Digite a sua segunda nota: '))
media = n1 + n2 / 2
print(f'Boletim do primeiro aluno: {nome, media}')
while True:
    continuar = str(input('Você quer continuar? [S/N]')).strip().upper()  
    if continuar == 'S':
        tot += 1
        nome = lista.append(str(input('Digite seu nome: ')))
        n1 = lista.append(int(input('Digite a sua primeira nota: ')))
        n2 = lista.append(int(input('Digite a sua segunda nota: ')))
        print(f'Boletim do primeiro aluno: {lista[0], media}')
        tdboletim = lista[:]
        lista.clear
    else:
        break
print(f'O boletim de todos os alunos é: {tdboletim}')
