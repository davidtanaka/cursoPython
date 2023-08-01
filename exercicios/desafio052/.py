p = int(input('digite um numero: '))
tot = 0
for c in range(1, p + 1):
    if p % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mo numero {} foi divisivel {} vezes'.format(p, tot))
if tot == 2:
    print('Esse numero é PRIMO ')
else:
    print('esse numero NÃO É PRIMO')