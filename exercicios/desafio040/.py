n1 = float(input('digite sua primeira nota: '))
n2 = float(input('digite a outra nota: '))
media = (n1 + n2) / 2
 
if media < 5:
    print('REPROVADO')
elif media < 6.9:
    print('RECUPERAÇÃO')
elif media >= 7:
    print('APROVADO')
else:
    print('Bom ano')