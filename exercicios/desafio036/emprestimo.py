valorC = float(input('qual é o valor da casa: '))
salario = float(input('Qual é o seu salario: '))
anos = int(input(' Em quantos anos você vai pagar? '))
emprestimo = valorC / anos

if emprestimo == salario * 50:
    print('você vai comprar a casa o valor mensal sera de {}'.format(emprestimo))
elif emprestimo > salario  * 30 / 100:
    print('Você não poderá comprar está casa')
else:
    print('obrigado')