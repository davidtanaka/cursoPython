situaçao = ''
nomeEmedia = dict()
nome = str(input('Nome: '))
media = int(input('Media: '))
nomeEmedia['nome'] = nome
nomeEmedia['media'] = media
if nomeEmedia['media'] >= 7:
    situaçao = 'Aprovado'
elif nomeEmedia['media'] < 7 and nomeEmedia['media'] >= 5:
    situaçao = 'Recuperação'
else:
    situaçao = 'Reprovado'
print(f'Nome é igual a {nomeEmedia["nome"]}')
print(f'Média é igual a {nomeEmedia["media"]}')
print(f'Situação é igual á {situaçao}')