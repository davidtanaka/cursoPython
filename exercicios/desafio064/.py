soma = 0
n =  0
totaldnum = 0
while n != 999:
    n = float(input('digite um numero: [ Digite 999 para parar]'))
    totaldnum += 1
    soma += n
print('foram digitados {} numeros e a soma deles é de: {:.0f}.'.format(totaldnum - 1, soma - 999))
print('FIM')