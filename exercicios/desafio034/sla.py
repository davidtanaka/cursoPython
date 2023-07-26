salario = float(input('digite seu salario:'))
dez = salario * 10 / 100
quinze = salario * 15 / 100

if salario <= 1.250:
    print('seu salario agora é de {}'.format(salario + quinze))
else: 
    print('seu salario agora é de: {}'.format(salario + dez))