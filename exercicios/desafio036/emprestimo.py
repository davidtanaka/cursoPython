valorC = float(input('qual é o valor da casa: '))
salario = float(input('Qual é o seu salario: '))
anos = int(input(' Em quantos anos você vai pagar? '))
emprestimo = valorC / (anos * 12)
min = salario * 30 / 100

if emprestimo <= min:
    print('EMPRESTIMO CONCEDIDO')
else:
    print('EMPRESTIMO NEGADO')