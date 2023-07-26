a = float(input('digite um numero: '))
b = float(input('digite outro numero: '))
c = float(input('digite outro numero: '))

menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
    
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
    
print('o meno valor digitado foi: {:.1f}'.format(menor))
print('o maior numero digitado foi : {:.1f}'.format(maior))