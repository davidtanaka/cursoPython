from statistics import mean
pessoas = list()
pessoa = dict()
while True:
    pessoa['nome'] = input('Nome: ').strip().capitalize()
    while True:
        pessoa['sexo'] = input('Sexo [M/F]: ').strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: ').strip())
    pessoas.append(pessoa.copy())
    while True:
        resposta = input('Quer continuar [S/N]? ').strip().upper()[0]
        if resposta in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resposta == 'N':
        break

media = mean(list(c['idade'] for c in pessoas))
mulheres = ' e '.join(', '.join(list(c['nome'] for c in pessoas if c['sexo'] == 'F')).rsplit(', ', 1))
mqam = list(c for c in pessoas if c['idade'] > media)

print('-=' * 30)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')
print(f'B) A média de idade é de {media:.2f} anos.')
print(f'C) As mulheres cadastradas foram: {mulheres}')
print(f'D) Lista das pessoas que estão acima da média:')
for p in mqam:
    for k, v in p.items():
        print(f'    {k} = {v};', end=' ')
    print()
print('<< ENCERRADO >>')
pessoas = list()
pessoa = dict()
while True:
    pessoa['nome'] = input('Nome: ').strip().capitalize()
    while True:
        pessoa['sexo'] = input('Sexo [M/F]: ').strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: ').strip())
    pessoas.append(pessoa.copy())
    while True:
        resposta = input('Quer continuar [S/N]? ').strip().upper()[0]
        if resposta in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resposta == 'N':
        break

media = mean(list(c['idade'] for c in pessoas))
mulheres = ' e '.join(', '.join(list(c['nome'] for c in pessoas if c['sexo'] == 'F')).rsplit(', ', 1))
mqam = list(c for c in pessoas if c['idade'] > media)

print('-=' * 30)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')
print(f'B) A média de idade é de {media:.2f} anos.')
print(f'C) As mulheres cadastradas foram: {mulheres}')
print(f'D) Lista das pessoas que estão acima da média:')
for p in mqam:
    for k, v in p.items():
        print(f'    {k} = {v};', end=' ')
    print()
print('<< ENCERRADO >>')