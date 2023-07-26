#nome = str(input('qual é seu nome?'))
#if nome == 'davi':
 #   print('que nome maravilhoso')
#else:
#    print('seu nome é tão normal :(')
#print('bom dia, {}'.format(nome))

n1 = float(input('digite a sua primeira nota: '))
n2 = float(input('digite a sua segunda nota: '))
m = (n1 + n2)/2
print('a sua media foi {:.1f}'.format(m))
if m>= 6.0:
    print('sua media foi noa')
else:
    print('sua media foi ruim')