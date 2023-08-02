sexo = str(input('Qual é o seu sexo [M/F]: ')).strip().upper()[0]

while sexo not in 'MmFf':
    sexo = str(input('dados invalidos, porfavor insira novamente seu sexo: '))
print('obrigado pela colaboração')