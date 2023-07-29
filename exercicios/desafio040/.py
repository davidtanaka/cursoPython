n1 = float(input('digite uma nota sua: '))
n2 = float(input('digite outra nota: '))
media = n1 + n2 /2

if media < 5:
    print('REPROVADO')
elif media < 6.9:
    print('RECUPERAÇÃO')
elif media >= 7:
    print('APROVADO')
else:
    print('Bom ano')