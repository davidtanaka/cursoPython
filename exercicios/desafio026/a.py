a = str(input('Digite uma frase')).upper().strip()
print('A letra A aparece {} vezes a primeira vez em que ela aperce está na posição {}, e a ultima vez em que a letra A apareceu ela estava na posição {}'.format(a.count('A'), a.find('A')+1, a.rfind('A')))