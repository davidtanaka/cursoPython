num1 = float(input('digite um numero: '))
num2 = float(input('digite outro numero: '))
maiornumero = 0
opcoes =  0
if num1 > num2:
    maiornumero = num1
else:
    maiornumero = num2
while opcoes != 5:
    print('''    [ 1 ]Somar
    [ 2 ]Multiplicar
    [ 3 ]Maior
    [ 4 ]Novos numeros
    [ 5 ]SAIR DO PROGRAMA''')
    opcoes = int(input('Qual é a sua escolha: '))
    if opcoes == 1:
        print('a soma dos numeros fica: {}'.format(num1 + num2))
    elif opcoes == 2:
        print('A multiplicação dos numeros selecionados fica {}'.format(num1 * num2))
    elif opcoes == 3:
        print('O Maior numero digitado é: {}'.format(maiornumero))
    elif opcoes == 4:
        n1 = int(input('digite seu numero novamente: '))
        n2 = int(input('digite seu segungo numero novamente: '))
    elif opcoes == 5:
        print('FINALIZANDO')
    else:
        print('Opção invalida, tente novamente ')
print('Fim do programa, Volte sempre')
