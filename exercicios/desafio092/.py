from datetime import datetime
apo = {}
apo['nome'] = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
apo['carteira'] = int(input('Carteira de trabalho: '))
idade = ano - datetime.now().year
apo['idade'] = idade
if apo['carteira'] != 0:
    apo['contratação'] = int(input('Ano de contratação: '))
    apo['salario'] = float(input('Salário: '))
    apo['aposentadoria'] = apo['idade'] + ((apo['contratação'] + 35) - datetime.now().year)
for k, v in apo.items():
    print(f'   {k} tem o valor {v}')