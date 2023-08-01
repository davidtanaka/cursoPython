somaidade = 0
mediaidade = 0
maioridadehomen = 0
nomevelho = 0
totmulher20 = 0
for p in range(1, 5):
    nome = str(input('nome: ')).strip()
    idade = int(input('idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomen = idade
        nomevelho = nome
        if sexo in 'Mm' and idade > maioridadehomen:
            maioridadehomen = idade
            nomevelho = nome
        if sexo in 'Ff' and idade < 20:
            totmulher20 += 1
mediaidade = somaidade / 4
print('a maior idade do grupo é {} anos'.format(mediaidade))
print('O homen mais velho tem {} anos'.format(maioridadehomen, nomevelho))
print('ao todo são {} mulheres com menos de 20 anos '.format(totmulher20))