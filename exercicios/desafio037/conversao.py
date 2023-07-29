valor = int(input('Digite um numero inteiro: '))
print('''escolha uma das bases para conversão:
[1] converter para BINARIO
[2]converter para OCTAL
[3]CONVERTER PARA HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para BINARIO é igual a {2:}'.format(valor, bin(valor)))
elif opção == 2:
    print('{} convertido para OCTAL é iguala {2:}'.format(valor, oct(valor)))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {2:}'.format(valor, hex(valor)))
else:
    print('opção invalida tente novamente')