continuar = True
totM18 = totHm = totMulher20 = 0
cmç = str(input('Voçe já deseja começar? [S/N]')).strip().upper()
while cmç not in 'SsNn':
    str(input('Voçe já deseja começar? [S/N]')).strip().upper()[0]
    if cmç == 'Ss':
        break
if cmç == 'S':
    cmç = True

while cmç == True:
    idade = int(input('Idade: '))
    if idade >= 18:
        totM18 += 1
    sexo = str(input('Sexo: [M/F]')).strip().upper()[0]
    while sexo not in 'MF':
        str(input('Sexo: [M/F]')).strip().upper()[0]
    if sexo == 'M':
        totHm += 1
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continuar == 'N':
        break
    if sexo == 'F' and idade <= 20:
        totMulher20 += 1
print(f'Total de pessoas com mais de 18 anos: {totM18}')
print(f'Ao todo temos {totHm} homens cadrastrados')
print(f'E temos {totMulher20} mulheres com menos de 20 anos cadastradas')
 