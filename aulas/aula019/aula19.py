# pessoas = {'nome': 'Davi', 'Sexo': 'M', 'idade': 15}
# print(f'O {pessoas["nome"]} É do sexo {pessoas["Sexo"]} e tem {pessoas["idade"]} anos')

# brasil = []
# estado1 = {'uf': 'Rio de janeiro', 'sigla': 'rj'}
# estado2 = {'uf': 'são paulo', 'sigla': 'sp'}
# brasil.append(estado1)
# brasil.append(estado2)

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}')
